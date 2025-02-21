from brain_games.const import EVEN_INSTRUCTIONS
from brain_games.engine import run_engine
from brain_games.utils import get_random_number


def is_even(number):
    return number % 2 == 0


def get_math_question_and_result():
    math_expression = get_random_number()
    correct_answer = 'yes' if is_even(math_expression) else 'no'

    return correct_answer, math_expression


def run_even_game():
    run_engine(get_math_question_and_result, EVEN_INSTRUCTIONS)