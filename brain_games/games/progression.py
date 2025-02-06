import random

from brain_games.engine import (
    receive_instructions,
    run_engine,
)


def generate_instructions():
    instructions = 'What number is missing in the progression?' 
    return instructions


def get_math_question_and_result():
    start_number = random.randint(1, 100)
    step = random.randint(1, 5)
    progression_length = random.randint(5, 10)
    progression_list = []
    for i in range(progression_length):
        progression_list.append(start_number + (i - 1) * step)
    missing_number = random.choice(progression_list)
    index_of_missing_number = progression_list.index(missing_number)
    progression_list[index_of_missing_number] = '..'
    correct_answer = str(missing_number)
    progression_list = ' '.join(map(str, progression_list))
    question = f'Question: {progression_list}'
    return correct_answer, question


def run_progression_game():
    receive_instructions(generate_instructions)
    run_engine(get_math_question_and_result)
 


