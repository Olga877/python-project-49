import random
import prompt
name = prompt.string('May I have your name? ')

OPERATORS = ('+', '-', '*')


def run_engine():
    iterations_number = 3
    for _ in range(iterations_number):
       num1 = random.randint(1, 100)
       num2 = random.randint(1, 100)
       math_operator = random.choice(OPERATORS)
       math_expression = f'{num1} {math_operator} {num2}'
       result = eval(math_expression)
       correct_answer = str(result)
       question = f'Question: {math_expression}'

       print(question)
       answer = prompt.string('Your answer: ')
       if answer.lower() == correct_answer:
            print("Correct!")
       else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def run_calc_game():
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
   
    run_engine()
