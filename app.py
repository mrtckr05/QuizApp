from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import os
import random
import google.generativeai as genai
import concurrent.futures

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

DB_PATH = os.path.join(os.path.dirname(__file__), 'questions', 'questions.db')
IMG_COUNT = 8  # hangman0.png to hangman7.png
MAX_QUESTIONS = 25  # Maximum questions per game

# Set your Gemini API key (ideally, use an environment variable)
key = "your-api-key-here"
genai.configure(api_key=key)

CATEGORY_PREFIX = {
    'Fen': 'SCI',
    'Tarih': 'HIST',
    'Coğrafya': 'GEO',
    'İngilizce': 'ENG',
}

# Helper to fetch questions by category with progressive difficulty
def get_questions(category):
    if category == "İngilizce":
        # İngilizce kategorisi için AI'den seviye seviye 9 soru üret
        levels = [
            ("A1-A2", 2, "Kolay, temel İngilizce kelime veya basit gramer sorusu üret. Sadece bir doğru cevap olsun."),
            ("B1", 3, "Orta seviye İngilizce kelime veya gramer sorusu üret. Sadece bir doğru cevap olsun."),
            ("B2", 2, "Orta-üstü, İngilizce kelime veya gramer sorusu üret. Sadece bir doğru cevap olsun."),
            ("C1", 2, "Çok zor, İngilizce kelime veya gramer sorusu üret. Sadece ileri düzey öğrencilerin çözebileceği bir soru olsun. Sadece bir doğru cevap olsun.")
        ]
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompts = []
        for level, count, prompt_detail in levels:
            for _ in range(count):
                prompt = (
                    f"Create a multiple-choice English quiz question at {level} level. "
                    f"{prompt_detail} "
                    "The question and all options must be in English. "
                    "Format your response exactly as below (do not add any explanations):\n"
                    "Question: ...\nA) ...\nB) ...\nC) ...\nD) ...\nAnswer: ..."
                )
                prompts.append(prompt)

        import re

        def fetch_question(prompt):
            try:
                response = model.generate_content(prompt)
                text = response.text.strip()
                # Sıkı regex ile ayıkla
                match = re.search(
                    r"Question:\s*(.+?)\s*A\)\s*(.+?)\s*B\)\s*(.+?)\s*C\)\s*(.+?)\s*D\)\s*(.+?)\s*Answer:\s*([A-D])",
                    text, re.DOTALL | re.IGNORECASE
                )
                if match:
                    question_text = match.group(1).strip()
                    options = [match.group(i).strip() for i in range(2, 6)]
                    correct = match.group(6).strip().upper()
                    return {
                        'question': question_text,
                        'options': options,
                        'correct': correct
                    }
            except Exception:
                return None

        questions = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(fetch_question, prompts))
            for idx, q in enumerate(results, 1):
                if q:
                    q['id'] = f'AI_ENG_{idx}'
                    questions.append(q)
        random.shuffle(questions)
        return questions[:MAX_QUESTIONS]

    # Diğer kategoriler için mevcut kod çalışmaya devam eder
    prefix = CATEGORY_PREFIX.get(category, '')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Question, OptA, OptB, OptC, OptD, CorrectAnswer FROM questions WHERE ID LIKE ?", (f'{prefix}%',))
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        return []
    questions_by_level = {
        'easy': [],
        'medium': [],
        'upper': [],
        'hard': []
    }
    for row in rows:
        question = {
            'id': row[0],
            'question': row[1],
            'options': [row[2], row[3], row[4], row[5]],
            'correct': row[6]
        }
        if prefix == 'SCI':
            if 'SCI' + str(1) <= row[0] <= 'SCI' + str(10):
                questions_by_level['easy'].append(question)
            elif 'SCI' + str(11) <= row[0] <= 'SCI' + str(20):
                questions_by_level['medium'].append(question)
            elif 'SCI' + str(21) <= row[0] <= 'SCI' + str(30):
                questions_by_level['upper'].append(question)
            else:
                questions_by_level['hard'].append(question)
        elif prefix == 'HIST':
            if 'HIST' + str(1) <= row[0] <= 'HIST' + str(9):
                questions_by_level['easy'].append(question)
            elif 'HIST' + str(10) <= row[0] <= 'HIST' + str(18):
                questions_by_level['medium'].append(question)
            elif 'HIST' + str(19) <= row[0] <= 'HIST' + str(27):
                questions_by_level['upper'].append(question)
            else:
                questions_by_level['hard'].append(question)
        else:
            questions_by_level['easy'].append(question)
    # --- EŞSİZ SORU SEÇİMİ ---
    selected_questions = []
    used_ids = set()
    total_needed = MAX_QUESTIONS

    # Sırasıyla easy, medium, upper, hard seviyelerinden soruları seç
    for level, count in zip(['easy', 'medium', 'upper', 'hard'], [8, 8, 5, 4]):
        available = [q for q in questions_by_level[level] if q['id'] not in used_ids]
        if len(available) > count:
            chosen = random.sample(available, count)
        else:
            chosen = available
        selected_questions.extend(chosen)
        used_ids.update(q['id'] for q in chosen)

    # Eğer hala eksik varsa, kalan tüm seviyelerden rastgele ve tekrar etmeyen şekilde tamamla
    while len(selected_questions) < total_needed:
        all_remaining = [q for level in ['easy', 'medium', 'upper', 'hard'] for q in questions_by_level[level] if q['id'] not in used_ids]
        if not all_remaining:
            break
        needed = total_needed - len(selected_questions)
        chosen = random.sample(all_remaining, min(needed, len(all_remaining)))
        selected_questions.extend(chosen)
        used_ids.update(q['id'] for q in chosen)

    # Son olarak karıştır
    random.shuffle(selected_questions)
    return selected_questions[:MAX_QUESTIONS]

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        category = request.form.get('category')
        if not username or not category:
            error = 'İsim ve kategori seçilmelidir.'
        else:
            session.clear()
            session['username'] = username
            session['category'] = category
            session['wrong_count'] = 0
            session['current'] = 0
            session['hint_count'] = 3  # Reset hint count
            questions = get_questions(category)
            session['questions'] = questions
            session['answers'] = []
            return redirect(url_for('quiz'))
    return render_template('index.html', error=error)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = session.get('questions', [])
    current = session.get('current', 0)
    wrong_count = session.get('wrong_count', 0)
    max_wrong = IMG_COUNT - 1
    if not questions or current >= len(questions) or wrong_count >= max_wrong:
        return redirect(url_for('result'))
    question = questions[current]
    selected = None
    if request.method == 'POST':
        selected = request.form.get('option')
        session['answers'].append(selected)
        if selected != question['correct']:
            session['wrong_count'] = wrong_count + 1
        session['current'] = current + 1
        return redirect(url_for('quiz'))
    img_name = f'hangman{wrong_count}.png'
    return render_template('quiz.html', question=question, qnum=current+1, total=len(questions), img_name=img_name, wrong_count=wrong_count, max_wrong=max_wrong)

@app.route('/result')
def result():
    username = session.get('username')
    category = session.get('category')
    questions = session.get('questions', [])
    answers = session.get('answers', [])
    score = 0
    for i, q in enumerate(questions):
        if i < len(answers) and answers[i] == q['correct']:
            score += 1
    total = len(questions)
    wrong_count = session.get('wrong_count', 0)
    max_wrong = IMG_COUNT - 1
    ended_by_hangman = wrong_count >= max_wrong
    return render_template('result.html', username=username, category=category, score=score, total=total, wrong_count=wrong_count, ended_by_hangman=ended_by_hangman)

@app.route('/ai_hint', methods=['POST'])
def ai_hint():
    if session.get('hint_count', 0) <= 0:
        return jsonify({'hint': 'İpucu hakkınız kalmadı.'}), 403

    session['hint_count'] -= 1  # Hakkı azalt

    data = request.get_json()
    question = data.get('question', '')
    if not question:
        return jsonify({'hint': 'No question provided.'}), 400

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(
            f"Provide a helpful hint (not the answer) for this quiz question: {question}"
        )
        hint = response.text.strip()

        return jsonify({'hint': hint, 'hint_count': session['hint_count']})
    except Exception as e:
        return jsonify({'hint': f'AI error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)