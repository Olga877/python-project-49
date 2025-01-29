import random

from brain_games.games.common_game_engine import (
    receive_instructions,
    run_engine,
)

MIN_NUMBER = 1
MAX_NUMBER = 20 


def generate_instructions():
    instructions = 'Answer "yes" if the number is even, otherwise answer "no".' 
    return instructions


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer_even():
    correct_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(correct_number) else 'no'
    question = f'Question: {correct_number}'

    return correct_answer, question


def run_even_game():
    receive_instructions(generate_instructions)
    run_engine(generate_question_and_answer_even)
    

