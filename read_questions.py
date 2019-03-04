import random

class ReadQuestions():

    def score_questions(self, quest_num, answer, category, correct, score={"results": []}):
        # schema of result
        '''
            {results:[
                {result: answer, correct: correct, right_or_wrong: <1 or 0>, category: category}
                ]
            }
        '''
        ans = set(answer.split(","))
        cor = set(correct.split(","))
        if ans - cor == set():
            right_or_wrong = 1
        else:
            right_or_wrong = 0
        the_result = {"quest_num": quest_num, "result": answer, "correct": correct, "right_or_wrong": right_or_wrong, "category": category}
        score["results"].append(the_result)
        return score

    @staticmethod
    def load_questions():
        quests = open("json_quest_out_v2.txt", "r")
        questions = eval(quests.read())
        return questions["questions"]["question"]

    @staticmethod
    def get_random_questions():
        quest = ReadQuestions.load_questions()
        total = ReadQuestions.get_number_of_questions(quest)
        return random.sample(range(1, total),(total - 1))

    @staticmethod
    def go_through_each_question():
        quests = open("json_quest_out.txt", "r")
        questions = eval(quests.read())
        question_list = questions["questions"]["question"]

        for question in question_list:
            print("Question: {}".format(ReadQuestions.get_question_order(question)))
            print("{}".format(ReadQuestions.get_question_text(question)))
            for answer in question['answers']['answer']:
                print(ReadQuestions.get_all_answers_in_order(answer))
            if 'correct' in question['answers']:
                print(ReadQuestions.get_correct_answers(question['answers']['correct']))
            else:
                print("There is no answer for this question")

    @staticmethod
    def get_number_of_questions(questions):
        return len(questions)

    @staticmethod
    def get_question(questions, num):
        question = questions[num]
        out = ""
        out += "Question: {}".format(ReadQuestions.get_question_order(question)) + "\n"
        out += "{}".format(ReadQuestions.get_question_text(question)) + "\n"
        for answer in question['answers']['answer']:
            out += ReadQuestions.get_all_answers_in_order(answer)  + "\n"
        if 'correct' in question['answers']:
            out += ReadQuestions.get_correct_answers(question['answers']['correct'])
        return out

    @staticmethod
    def get_question_raw_json(questions, num):
        question = questions[num]
        return question

    @staticmethod
    def find_questions_without_answers():
        quests = open("json_quest_out.txt", "r")
        questions = eval(quests.read())
        question_list = questions["questions"]["question"]

        for question in question_list:
            if 'correct' in question['answers']:
                pass
            else:
                print("Question: {}".format(ReadQuestions.get_question_order(question)))
                print("{}".format(ReadQuestions.get_question_text(question)))
                for answer in question['answers']['answer']:
                    print(ReadQuestions.get_all_answers_in_order(answer))

    @staticmethod
    def get_question_order(question):
        return question["order"]

    @staticmethod
    def get_question_text(question):
        return question["question_text"]

    @staticmethod
    def get_answer_type(question):
        return question['answers']['answer_type']

    @staticmethod
    def get_all_answers_in_order(answers):
        return "{}: {}".format(answers['order'], answers["text"])

    @staticmethod
    def get_correct_answers(answer):
        return "corrrect choice: {}".format(answer)

r = ReadQuestions()
# # r.go_through_each_question()
# # r.find_questions_without_answers()
# q = r.load_questions()
# print("The number of questions is: {}".format(r.get_number_of_questions(q)))
# r.get_question(q, 70)
score = r.score_questions("1", "1,2", "Deployment and Provisioning", "1,2")
print(score)
score = r.score_questions("2", "3,4", "Deployment and Provisioning", "3,4")
print(score)