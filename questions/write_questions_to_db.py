import os
import sqlite3
import questions
os.chdir("QuizApp\\questions")

con = sqlite3.connect("questions.db")

cursor = con.cursor()

def create_tab():
    cursor.execute("CREATE TABLE IF NOT EXISTS questions (ID PRIMARY KEY, Question TEXT, OptA TEXT, OptB TEXT, OptC TEXT, OptD TEXT, CorrectAnswer TEXT)")
    con.commit()
create_tab()

def add_question(ID:str, Question:str, OptionA:str, OptionB:str, OptionC:str, OptionD:str, CorrectAnswer:str):
    cursor.execute("INSERT INTO questions VALUES(?,?,?,?,?,?,?)",(ID,Question,OptionA,OptionB,OptionC,OptionD,CorrectAnswer))
    con.commit()


for i in range(len(questions.science_questions_easy)):
    id = "SCI" + str(i+1)
    question = questions.science_questions_easy[i]   
    optionA = questions.science_options_easy["A"][i]
    optionB = questions.science_options_easy["B"][i]
    optionC = questions.science_options_easy["C"][i]
    optionD = questions.science_options_easy["D"][i]
    correct_answer = questions.science_correct_answers_easy[i]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Easy Science questions added to DB!!! ")
last_id_number = len(questions.science_questions_easy)

for j in range(len(questions.science_questions_medium)):
    id = "SCI" + str(last_id_number+(j+1))
    question = questions.science_questions_medium[j]   
    optionA = questions.science_options_medium["A"][j]
    optionB = questions.science_options_medium["B"][j]
    optionC = questions.science_options_medium["C"][j]
    optionD = questions.science_options_medium["D"][j]
    correct_answer = questions.science_correct_answers_medium[j]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Medium Science questions added to DB!!! ")
last_id_number = len(questions.science_questions_easy) + len(questions.science_questions_medium)

for k in range(len(questions.science_questions_uppermid)):
    id = "SCI" + str(last_id_number+(k+1))
    question = questions.science_questions_uppermid[k]   
    optionA = questions.science_options_uppermid["A"][k]
    optionB = questions.science_options_uppermid["B"][k]
    optionC = questions.science_options_uppermid["C"][k]
    optionD = questions.science_options_uppermid["D"][k]
    correct_answer = questions.science_correct_answers_uppermid[k]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Medium-Hard Science questions added to DB!!! ")
last_id_number =  len(questions.science_questions_uppermid) + len(questions.science_questions_easy) + len(questions.science_questions_medium)

for m in range(len(questions.science_questions_hard)):
    id = "SCI" + str(last_id_number+(m+1))
    question = questions.science_questions_hard[m]   
    optionA = questions.science_options_hard["A"][m]
    optionB = questions.science_options_hard["B"][m]
    optionC = questions.science_options_hard["C"][m]
    optionD = questions.science_options_hard["D"][m]
    correct_answer = questions.science_correct_answers_hard[m]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Hard Science questions added to DB!!! ")

for n in range(len(questions.history_questions_easy)):
    id = "HIST" + str(n+1)
    question = questions.history_questions_easy[n]   
    optionA = questions.history_options_easy["A"][n]
    optionB = questions.history_options_easy["B"][n]
    optionC = questions.history_options_easy["C"][n]
    optionD = questions.history_options_easy["D"][n]
    correct_answer = questions.history_correct_answers_easy[n]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Easy History questions added to DB!!! ")
last_id_number_hist = len(questions.history_questions_easy)

for o in range(len(questions.history_questions_medium)):
    id = "HIST" + str(last_id_number_hist+(o+1))
    question = questions.history_questions_medium[o]   
    optionA = questions.history_options_medium["A"][o]
    optionB = questions.history_options_medium["B"][o]
    optionC = questions.history_options_medium["C"][o]
    optionD = questions.history_options_medium["D"][o]
    correct_answer = questions.history_correct_answers_medium[o]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Medium History questions added to DB!!! ")
last_id_number_hist = len(questions.history_questions_easy) + len(questions.history_questions_medium)

for p in range(len(questions.history_questions_uppermid)):
    id = "HIST" + str(last_id_number_hist+(p+1))
    question = questions.history_questions_uppermid[p]   
    optionA = questions.history_options_uppermid["A"][p]
    optionB = questions.history_options_uppermid["B"][p]
    optionC = questions.history_options_uppermid["C"][p]
    optionD = questions.history_options_uppermid["D"][p]
    correct_answer = questions.history_correct_answers_uppermid[p]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Medium-Hard History questions added to DB!!! ")
last_id_number_hist = len(questions.history_questions_easy) + len(questions.history_questions_medium) + len(questions.history_questions_uppermid)

for r in range(len(questions.history_questions_hard)):
    id = "HIST" + str(last_id_number_hist+(r+1))
    question = questions.history_questions_hard[r]   
    optionA = questions.history_options_hard["A"][r]
    optionB = questions.history_options_hard["B"][r]
    optionC = questions.history_options_hard["C"][r]
    optionD = questions.history_options_hard["D"][r]
    correct_answer = questions.history_correct_answers_hard[r]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Hard History questions added to DB!!! ")



for a in range(len(questions.geography_questions_easy)):
    id = "GEO" + str(a+1)
    question = questions.geography_questions_easy[a]
    optionA = questions.geography_options_easy["A"][a]
    optionB = questions.geography_options_easy["B"][a]
    optionC = questions.geography_options_easy["C"][a]
    optionD = questions.geography_options_easy["D"][a]
    correct_answer = questions.geography_answers_easy[a]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Easy Geography questions added to DB!!! ")
last_id_number = len(questions.geography_questions_easy)

for b in range(len(questions.geography_questions_medium)):
    id = "GEO" + str(last_id_number+(b+1))
    question = questions.geography_questions_medium[b]
    optionA = questions.geography_options_medium["A"][b]
    optionB = questions.geography_options_medium["B"][b]
    optionC = questions.geography_options_medium["C"][b]
    optionD = questions.geography_options_medium["D"][b]
    correct_answer = questions.geography_correct_answers_medium[b]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Medium Geography questions added to DB!!! ")
last_id_number = len(questions.geography_questions_easy) + len(questions.geography_questions_medium)

for c in range(len(questions.geography_questions_uppermid)):
    id = "GEO" + str(last_id_number+(c+1))
    question = questions.geography_questions_uppermid[c]
    optionA = questions.geography_options_uppermid["A"][c]
    optionB = questions.geography_options_uppermid["B"][c]
    optionC = questions.geography_options_uppermid["C"][c]
    optionD = questions.geography_options_uppermid["D"][c]
    correct_answer = questions.geography_correct_answers_uppermid[k]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Medium-Hard Geography questions added to DB!!! ")
last_id_number =  len(questions.geography_questions_uppermid) + len(questions.geography_questions_easy) + len(questions.geography_questions_medium)

for z in range(len(questions.geography_questions_hard)):
    id = "GEO" + str(last_id_number+(z+1))
    question = questions.geography_questions_hard[z]
    optionA = questions.geography_options_hard["A"][z]
    optionB = questions.geography_options_hard["B"][z]
    optionC = questions.geography_options_hard["C"][z]
    optionD = questions.geography_options_hard["D"][z]
    correct_answer = questions.geography_correct_answers_hard[z]
    add_question(id, question, optionA, optionB, optionC, optionD, correct_answer)
print("ALL Hard Geography questions added to DB!!! ")

print("All questions added for now... ")


con.close() 