import os
import shelve
from questions import Questions
from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.session_cookie_name = 'quiz-WebSession'
app.config['DEBUG'] = False


#TODO sort out why final question isn't being displayed
#TODO double totals problem

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
        print("create the rands")
        rands = Questions.get_random_questions()
        print(rands)
    else:
        rands = session['rands']
        print(rands)

    if len(rands):
        remain = len(rands)
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
                               correct=quest['answers']['correct'],
                               remain=remain
                               )
    else:
        del session['rands']
        rq = Questions()
        total = rq.final_tally(session['scores'], session)
        cat_totals = rq.category_tally(session['scores'])
        cat_quest_numbers = Questions.get_number_of_questions_by_category(Questions.load_questions())
        if 'scores' in session:
            del session['scores']
        if 'results' in session:
            del session['results']
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