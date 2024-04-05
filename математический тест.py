import random  # импорт расскоментируй в своём проекте, но здесь оставь закомментированным


# Генератор случайного математического примера
def generate_math_question(a, b):
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice(["+", "-", "*", "/"])
    return f"{num1} {operator} {num2}"
# импорт расскоментируй в своём проекте, но здесь оставь закомментированны
def check_answer(question, answer):
    try:
        answer = float(answer)
        return answer == eval(question)
    except ValueError:
        return False

def math_quiz(number_of_questions=6):
    try:
        print("Добро пожаловать в математический тест!")
        correct_answers = 0

        for i in range(number_of_questions):
            vopros = generate_math_question(1, 10)
            otvet = input(f"{vopros} = ")
            if check_answer(vopros, otvet):
                correct_answers += 1

        print("Тест завершен.")
        print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

        if correct_answers >= number_of_questions * 0.8:
            print("Отлично! Вы получаете оценку A.")
        elif correct_answers >= number_of_questions * 0.6:
            print("Хорошо! Вы получаете оценку B.")
        else:
            print("Попробуйте еще раз. Вы получаете оценку C.")
    except ValueError:
        print("Ответ нужен только в виде числа")

# Запуск теста
math_quiz()