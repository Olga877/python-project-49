import random

import prompt
MIN_NUMBER = 1
MAX_NUMBER = 20 

def is_even(number):
    return number % 2 == 0


def run_even_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(correct_number) else 'no'
    iterations_number = 3
    print(f'Question: {correct_number}')
    answer = prompt.string('Your answer: ')
    if answer.lower() == correct_answer:
           print("Correct!")
           print(f'Congratulations, {name}!')
           return
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n Let's try again, {name}!")    
    
    
#     if (x % 2 == 0 and y == 'yes') or (x % 2 != 0 and y == 'no'):
#             while i < 3:
#                 print(message)
#                 x = randint(MIN_NUMBER, MAX_NUMBER)
#                 print(f'Question: {x}')
#                 y = prompt.string('Your answer: ')
#                 i += 1
#             print(message)
#             print(f'Congratulations, {name}!')
#     if x % 2 == 0 and y != 'yes':
#             message = f"'{y}' is wrong answer ;(. Correct answer was 'yes'.\n Let's try again, {name}!"
#             print(message)
#     elif x % 2 != 0 and y != 'no':
#             message = f"'{y}' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {name}!"
#             print(message)

