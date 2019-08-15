import os
import random
from questions import Questions
from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.session_cookie_name = 'quiz-WebSession'
app.config['DEBUG'] = False

# Data to persist is Scores
# Difference between results and scores

questions = Questions.load_questions()
random.shuffle(questions)

@app.route('/')
def main():
    return 'The quiz is up and running'

@app.route('/favicon.ico')
def favico():
    return 'The quiz is up and running'

@app.route('/get_next_question/')
def get_next_question():
    if questions and len(questions):
        quest = str(Questions.get_question_raw_json(questions))
        quest = eval(quest)
        return render_template('question.html',
                           title="QUIZ",
                           order=quest['order'],
                           question_text=quest["question_text"],
                           type=quest['answers']['type'],
                           answers=quest['answers']['answer'],
                           category=quest['category'],
                           correct=quest['answers']['correct'],
                           remain=len(questions),
                           )
    else:
        rq = Questions()
        total = rq.final_tally(session['scores'])
        cat_totals = rq.category_tally(session['scores'])
        cat_quest_numbers = Questions.get_number_of_questions_by_category(Questions.load_questions())
        return render_template('end_of_questions.html',title="QUIZ", total=total, cat_totals=cat_totals,
                               num_per_cat=cat_quest_numbers)


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