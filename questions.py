import json


class QuestProcess:
    def __init__(self):
        # загружаем данные из json файла
        with open("questions.json", encoding="UTF-8") as file:
            data = json.load(file)

        # сохраняем вопросы, варианты ответов и номера верных ответов
        self.question = data["question"]
        self.options = data["options"]
        self.answer = data["answer"]

        self.number_question = -1
        self.question_limit = len(self.question)
        self.selected_answer = None

    def get_question(self):
        """Возвращает кортеж из 3-х элементов:
        Вопрос -> Str
        Ответы -> List
        Номер верного варианта -> Int"""
        if self.can_get_question():
            self.number_question += 1
            return (
                self.question[self.number_question],
                self.options[self.number_question],
                self.answer[self.number_question],
            )
        else:
            return 0

    def can_get_question(self):
        if self.question_limit > self.number_question + 1:
            return True
        else:
            return False
