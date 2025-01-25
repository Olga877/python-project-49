import random
import prompt
import math
name = prompt.string('May I have your name? ')


def run_engine():
    iterations_number = 3
    for _ in range(iterations_number):
       num1 = random.randint(1, 100)
       num2 = random.randint(1, 100)
       given_numbers = num1, num2
       correct_answer = str(math.gcd(num1, num2))
       question = f'Question: {given_numbers}'

       print(question)
       answer = prompt.string('Your answer: ')
       if answer.lower() == correct_answer:
            print("Correct!")
       else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def run_gcd_game():
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
   
    run_engine()
 