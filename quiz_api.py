from read_questions import ReadQuestions
from flask import Flask
app = Flask(__name__)


questions = ReadQuestions.load_questions()
num_quest = ReadQuestions.get_number_of_questions(questions)


@app.route('/')
def main():
    return 'The quiz is up and running'


@app.route('/get_a_question/<quest_num>')
def get_a_question(quest_num):
    quest = ReadQuestions.get_question(questions, int(quest_num))
    return quest


@app.route('/total_questions')
def get_num_questions():
    return str(num_quest)
