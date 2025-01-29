import random
import prompt

MIN_NUMBER = 1
MAX_NUMBER = 20 
name = prompt.string('May I have your name? ')

def is_even(number):
    return number % 2 == 0


def generate_question_and_answer_even():
    correct_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(correct_number) else 'no'
    question = f'Question: {correct_number}'

    return correct_answer, question


def run_engine():
    iterations_number = 3
    for _ in range(iterations_number):
       correct_number = random.randint(MIN_NUMBER, MAX_NUMBER)
       correct_answer = 'yes' if is_even(correct_number) else 'no'
       question = f'Question: {correct_number}'

       print(question)
       answer = prompt.string('Your answer: ')
       if answer.lower() == correct_answer:
            print("Correct!")
       else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

def run_even_game():
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
   
    run_engine()
    

