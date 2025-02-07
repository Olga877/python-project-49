from brain_games.engine import (
    receive_instructions,
    run_engine,
)
from brain_games.random_number import get_random_number


def generate_instructions():
    instructions = ('Answer "yes" if given number is prime. '
    'Otherwise answer "no".')
    return instructions


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        
    return True


def get_math_question_and_result():
    given_number = get_random_number()
    correct_answer = 'yes' if is_prime(given_number) else 'no'
    question = f'Question: {given_number}'
    return correct_answer, question


def run_prime_game(): 
    receive_instructions(generate_instructions)
    run_engine(get_math_question_and_result)
    