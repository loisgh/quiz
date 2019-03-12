class Questions:

    def category_tally(self, results):
        by_category = {}
        for result in results['results']:
            if 'right_or_wrong' in result:
                if result['category'] in by_category:
                    value = by_category[result['category']]
                    value += 1
                else:
                    value = 1
                by_category[result['category']] = value
        pts = Questions.get_points_per_question()
        by_category_pts = {k: round(v*pts, 2) for k, v in by_category.items()}
        return by_category_pts

    @staticmethod
    def questions_by_category():
        q = Questions.load_questions()
        category_totals = {}
        for quest in q:
            if quest['category'] in category_totals:
                value = category_totals['category']
                value += 1
            else:
                value = 1
            category_totals[quest['category']] = value
        return category_totals

    @staticmethod
    def get_points_per_question():
        q = Questions.load_questions()
        num_questions = Questions.get_number_of_questions(q)
        return round(100 / num_questions, 2)

    def final_tally(self, results):
        total_right = sum([int(result['right_or_wrong']) for result in results['results']])
        pts_per_question = Questions.get_points_per_question()
        return total_right * pts_per_question

    def score_questions(self, quest_num, answer, category, correct, score={"results": []}):
        # schema of result
        """
            {results:[
                {result: answer, correct: correct, right_or_wrong: <1 or 0>, category: category}
                ]
            }
        """
        ans = set(answer.split(","))
        cor = set(correct.split(","))
        if ans - cor == set():
            right_or_wrong = 1
        else:
            right_or_wrong = 0
        the_result = {"quest_num": quest_num, "result": answer, "correct": correct, "right_or_wrong": right_or_wrong,
                      "category": category}
        score["results"].append(the_result)
        return score

    @staticmethod
    def load_questions():
        quests = open("json_quest_out_v2.txt", "r")
        questions = eval(quests.read())
        quests.close()
        return questions["questions"]["question"]

    @staticmethod
    def get_number_of_questions(questions):
        return len(questions)

    @staticmethod
    def get_number_of_questions_by_category(questions):
        num_by_cat = {}
        for question in questions:
            if question['category'] in num_by_cat:
                value = num_by_cat[question['category']]
                value += 1
            else:
                value = 1
            num_by_cat[question['category']] = value
        return num_by_cat

    @staticmethod
    def get_question_raw_json(questions, num):
        question = questions[num]
        return question

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
