import json


with open("questions.json", encoding="UTF-8") as file:
    data = json.load(file)
print(len(data))
print(data)
quize = data['quiz_1']
# сохраняем вопросы, варианты ответов и номера верных ответов
question = quize["question"]
options = quize["options"]
answer = quize["answer"]
print(question)
print(options)
print(answer)
