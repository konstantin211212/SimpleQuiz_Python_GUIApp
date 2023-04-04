import json


class QuestProcess:
    def __init__(self):
        # загружаем данные из json файла
        with open("questions.json", encoding="UTF-8") as file:
            self.data = json.load(file)

        self.count_quizes = len(self.data)

        # сохраняем вопросы, варианты ответов и номера верных ответов
        self.question = None
        self.options = None
        self.answer = None

        self.number_question = -1
        self.question_limit = 0  # len(self.question)
        self.selected_answer = None
        self.statistics = [0, 0]
        self.images = None

    def load_list_quiz(self):
        list_quiz = []
        for i in range(1, self.count_quizes + 1):
            list_quiz.append(self.data[f"quiz_{i}"]["name"])
        return list_quiz

    def load_quiz(self, name_quiz):
        index = 0
        for i in range(1, self.count_quizes + 1):
            if self.data[f"quiz_{i}"]["name"] == name_quiz:
                index = i
                break

        # сохраняем вопросы, варианты ответов и номера верных ответов
        self.question = self.data[f"quiz_{index}"]["question"]
        self.options = self.data[f"quiz_{index}"]["options"]
        self.answer = self.data[f"quiz_{index}"]["answer"]
        self.images = self.data[f"quiz_{index}"]["images"]
        self.question_limit = len(self.question)

    def get_question(self):
        """Возвращает кортеж из 3-х элементов:
        Вопрос -> Str
        Ответы -> List
        Номер верного варианта -> Int
        Изображение при наличии -> Str"""
        if self.can_get_question():
            self.number_question += 1
            return (
                self.question[self.number_question],
                self.options[self.number_question],
                self.answer[self.number_question],
                self.get_image(),
            )
        else:
            return 0

    def get_image(self):
        if len(self.images) - 1 >= self.number_question:
            return self.images[self.number_question]
        else:
            return ""

    def can_get_question(self):
        if self.question_limit > self.number_question + 1:
            return True
        else:
            return False

    def reset_quiz(self):
        self.number_question = -1
        self.statistics = [0, 0]
        pass

    def check_answer(self):
        print(
            "Checke answer = ",
            self.options[self.number_question][self.answer[self.number_question] - 1],
        )
        if (
            self.selected_answer
            == self.options[self.number_question][self.answer[self.number_question] - 1]
        ):
            print(True)
            self.statistics[0] += 1
        else:
            self.statistics[1] += 1
            print(False)
