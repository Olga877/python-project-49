import math

from brain_games.engine import (
    receive_instructions,
    run_engine,
)
from brain_games.random_number import get_random_number


def generate_instructions():
    instructions = 'Find the greatest common divisor of given numbers.' 
    return instructions


def get_math_question_and_result():
    num1, num2 = get_random_number(), get_random_number()
    given_numbers = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    question = f'Question: {given_numbers}'
    return correct_answer, question


def run_gcd_game():
    receive_instructions(generate_instructions)
    run_engine(get_math_question_and_result)
