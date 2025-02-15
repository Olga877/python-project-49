import random

from brain_games.const import PROGRESSION_INSTRUCTIONS
from brain_games.engine import run_engine


def get_math_question_and_result():
    start_number = random.randint(1, 100)
    step = random.randint(1, 5)
    progression_length = random.randint(5, 10)
    index_of_missing_number = random.randint(0, progression_length - 1)
    missed_number = start_number + step * index_of_missing_number
    progression = ' '.join('..' if i == index_of_missing_number else str(start_number + i * step) for i in range(progression_length))
    correct_answer = str(missed_number)
    question = f'Question: {progression}'
    return correct_answer, question


def run_progression_game():
    run_engine(get_math_question_and_result, PROGRESSION_INSTRUCTIONS)
 


