#TODO when change is done in read questions, remove load questions where no longer necessary.
import os
from read_questions import Questions
from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.session_cookie_name = 'quiz-WebSession'
app.config['DEBUG'] = False

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
        return render_template('end_of_questions.html',title="QUIZ")
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
    print(quest_num)
    answer = request.args.get('answer')
    print(answer)
    category = request.args.get('category')
    print(category)
    correct = request.args.get('correct')
    print(correct)
    if quest_num and answer and category and correct:
        score = rq.score_questions(quest_num, answer, category, correct)
        print(score)
        return "OK"
    else:
        return "Problem with your data"