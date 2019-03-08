import os
import json
from questions import Questions
from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.session_cookie_name = 'quiz-WebSession'
app.config['DEBUG'] = False

questions = Questions.load_questions()

@app.route('/')
def main():
    return 'The quiz is up and running'

@app.route('/favicon.ico')
def favico():
    return 'The quiz is up and running'

@app.route('/get_next_question/')
def get_next_question():
    if not 'rands' in session:
        rands = Questions.get_random_questions()
    elif not len(session['rands']):
        del session['rands']
        rq = Questions()
        total = rq.final_tally(session['scores'])
        cat_totals = rq.category_tally(session['scores'])
        return render_template('end_of_questions.html',title="QUIZ", total=total, cat_totals=cat_totals)
    else:
        rands = session['rands']

    num = rands.pop()
    quest_num = int(num)
    quest_idx = quest_num - 1
    quest = str(Questions.get_question_raw_json(questions, quest_idx))
    quest = eval(quest)
    session['rands'] = rands
    return render_template('question.html',
                           title="QUIZ",
                           order=quest_num,
                           question_text=quest["question_text"],
                           type=quest['answers']['type'],
                           answers=quest['answers']['answer'],
                           category=quest['category'],
                           correct=quest['answers']['correct']
                           )


@app.route('/score_questions')
def score_questions():
    rq = Questions()
    quest_num = request.args.get('order')
    answer = request.args.get('answer')
    category = request.args.get('category')
    correct = request.args.get('correct')
    if quest_num and answer and category and correct:
        scores = rq.score_questions(quest_num, answer, category, correct)
        session['scores'] = scores
        return "OK"
    else:
        return "Problem with your data"