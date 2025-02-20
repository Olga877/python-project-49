import math

from brain_games.const import GCD_INSTRUCTIONS
from brain_games.engine import run_engine
from brain_games.utils import get_random_number


def generate_instructions():
    instructions = 'Find the greatest common divisor of given numbers.' 
    return instructions


def get_math_question_and_result():
    num1, num2 = get_random_number(), get_random_number()
    math_expression = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return correct_answer, math_expression


def run_gcd_game():
    run_engine(get_math_question_and_result, GCD_INSTRUCTIONS)