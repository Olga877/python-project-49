from brain_games.const import PRIME_INSTRUCTIONS
from brain_games.engine import run_engine
from brain_games.utils import get_random_number


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
    math_expression = get_random_number()
    correct_answer = 'yes' if is_prime(math_expression) else 'no'
    return correct_answer, math_expression


def run_prime_game(): 
    run_engine(get_math_question_and_result, PRIME_INSTRUCTIONS)