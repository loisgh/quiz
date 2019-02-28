#TODO Make sure that the right question is getting posted.
import os
from read_questions import ReadQuestions
from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.session_cookie_name = 'quiz-WebSession'
app.config['DEBUG'] = False

questions = ReadQuestions.load_questions()
num_quest = ReadQuestions.get_number_of_questions(questions)

@app.route('/')
def main():
    return 'The quiz is up and running'

@app.route('/get_next_question/')
def get_next_question():
    if not 'rands' in session:
        print("we are loading the session data")
        rands = ReadQuestions.get_random_questions()
    elif not len(session['rands']):
        del session['rands']
        return render_template('end_of_questions.html',
                               title="QUIZ")
        return "You've reached the end of the test"
    else:
        rands = session['rands']

    num = rands.pop()
    quest_num = int(num)
    quest_idx = quest_num - 1
    quest = str(ReadQuestions.get_question_raw_json(questions, quest_idx))
    quest = eval(quest)
    session['rands'] = rands
    return render_template('question.html',
                           title="QUIZ",
                           order=quest_num,
                           question_text=quest["question_text"],
                           type=quest['answers']['type'],
                           answers=quest['answers']['answer'],
                           correct=quest['answers']['correct']
                           )

@app.route('/get_a_question/<quest_num>')
def get_a_question(quest_num):
    # quest = ReadQuestions.get_question(questions, int(quest_num))
    quest = str(ReadQuestions.get_question_raw_json(questions, int(quest_num)))
    quest = eval(quest)
    return render_template('question.html',
                           order=quest["order"],
                           question_text=quest["question_text"],
                           type=quest['answers']['type'],
                           answers=quest['answers']['answer'],
                           rand_quest_list=ReadQuestions.get_random_questions()
                           )


@app.route('/total_questions')
def get_num_questions():
    return str(num_quest)
