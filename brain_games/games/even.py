from brain_games.engine import (
    receive_instructions,
    run_engine,
)
from brain_games.random_number import get_random_number


def generate_instructions():
    instructions = 'Answer "yes" if the number is even, otherwise answer "no".' 
    return instructions


def is_even(number):
    return number % 2 == 0


def get_math_question_and_result():
    correct_number = get_random_number()
    correct_answer = 'yes' if is_even(correct_number) else 'no'
    question = f'Question: {correct_number}'

    return correct_answer, question


def run_even_game():
    receive_instructions(generate_instructions)
    run_engine(get_math_question_and_result)
    

