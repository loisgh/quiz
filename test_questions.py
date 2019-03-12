import unittest
from unittest import mock
from questions import Questions


class TestQuestions(unittest.TestCase):

    def test_questions_by_category(self):

        data = [
                    {
                        "order": "1",
                        "category": "Monitoring and Reporting",
                    },
                    {
                        "order": "2",
                        "category": "Monitoring and Reporting",
                    },
                    {
                        "order": "3",
                        "category": "High Availability",
                    },
                    {
                        "order": "4",
                        "category": "Deployment and Provisioning",
                    },
                    {
                        "order": "5",
                        "category": "Deployment and Provisioning",
                    },
                    {
                        "order": "6",
                        "category": "Storage and Data Management",
                    },
                    {
                        "order": "7",
                        "category": "Storage and Data Management",
                    },
                    {
                        "order": "8",
                        "category": "Storage and Data Management",
                    },
                    {
                        "order": "9",
                        "category": "Security and Compliance",
                    },
                    {
                        "order": "10",
                        "category": "Security and Compliance",
                    },
                    {
                        "order": "11",
                        "category": "Security and Compliance",
                    },
                    {
                        "order": "12",
                        "category": "Networking",
                    },
                    {
                        "order": "13",
                        "category": "Networking",
                    },
                    {
                        "order": "14",
                        "category": "Automation and Optimization",
                    },
                    {
                        "order": "15",
                        "category": "Automation and Optimization",
                    },
                    {
                        "order": "16",
                        "category": "Automation and Optimization",
                    },
                    {
                        "order": "17",
                        "category": "Networking",
                    }
                ]
        exp_category_totals = {'Monitoring and Reporting': 2,
                               'High Availability': 1,
                               'Deployment and Provisioning': 2,
                               'Storage and Data Management': 3,
                               'Security and Compliance': 3,
                               'Networking': 3,
                               'Automation and Optimization': 3}
        category_totals = Questions.get_number_of_questions_by_category(data)
        self.assertTrue(TestQuestions.compare_dict(exp_category_totals, category_totals))

    @staticmethod
    def compare_dict(exp_totals, cat_totals):
        match = False
        keys = exp_totals.keys()
        for k in keys:
            if k in cat_totals and cat_totals[k] == exp_totals[k]:
                match = True
            else:
                match = False
                break
        return match

    @mock.patch('questions.Questions.get_number_of_questions')
    def test_get_points_per_question(self, mock_get_number_of_questions):
        mock_get_number_of_questions.return_value = 49
        expected_result = round(100 /49 , 2)
        self.assertEqual(Questions.get_points_per_question(),expected_result)

    def test_score_questions(self):
        exp_result = {'Monitoring and Reporting': 4.62, 'Storage and Management': 4.62}
        results = {'results': [
        {"quest_num": 1, "result": 1, "correct": 1, "right_or_wrong": 1, "category": 'Monitoring and Reporting'},
        {"quest_num": 2, "result": 2, "correct": 3, "right_or_wrong": 0, "category": 'Monitoring and Reporting'},
        {"quest_num": 3, "result": 3, "correct": 3, "right_or_wrong": 1, "category": 'Monitoring and Reporting'},
        {"quest_num": 4, "result": 1, "correct": 1, "right_or_wrong": 1, "category": 'Storage and Management'},
        {"quest_num": 5, "result": 2, "correct": 3, "right_or_wrong": 0, "category": 'Storage and Management'},
        {"quest_num": 6, "result": 3, "correct": 3, "right_or_wrong": 1, "category": 'Storage and Management'}
        ]}
        rq = Questions()
        cat_result = rq.category_tally(results)
        self.assertTrue(TestQuestions.compare_dict(exp_result, cat_result))

    # @mock.patch('questions.Questions.get_Questions.get_number_of_questions')
    # def test_category_tally(self, mock_get_number_of_questions):
    #     # mock_get_number_of_questions.return_value = 50
    #     pass
    #
    # def test_final_tally(self):
    #     pass
    #
