# QuizApp Python (Flask)

A web-based quiz application built with Flask, featuring a hangman-style game where users answer questions and see the hangman image update based on wrong answers.

## Features

- Multiple quiz categories (Science, History, Geography, English)
- Science, History and Geography Questions loaded from SQLite database
- English questions are asked by AI(Gemini)
- Hangman-style game mechanics
- One question at a time display
- Real-time wrong answer tracking
- Responsive design with Bootstrap

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000
   ```

## How to Play

1. Enter your name and select a quiz category
2. Answer questions one by one
3. Each wrong answer adds to the hangman image
4. The game ends when you either:
   - Complete all questions, or
   - Reach the maximum number of wrong answers (7)

## File Structure

```
QuizAppPython/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   └── img/              # Hangman images (hangman0.png to hangman7.png)
├── templates/            # HTML templates
│   ├── index.html        # Start page
│   ├── quiz.html         # Quiz questions
│   └── result.html       # Results page
└── questions/            # Database and question files
    ├── questions.db      # SQLite database with questions
    ├── questions.py      # Question definitions
    └── write_questions_to_db.py  # Script to populate database
```

## Categories Available

- **Fen (Science):** SCI1, SCI2, etc.
- **Tarih (History):** HIST1, HIST2, etc.
- **Coğrafya (Geography):** GEO1, GEO2, etc.
- **İngilizce:** AI asks   
