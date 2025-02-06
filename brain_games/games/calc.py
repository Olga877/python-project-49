import random

from brain_games.engine import (
    receive_instructions,
    run_engine,
)

from brain_games.random_number import get_random_number


def get_random_math_sign_and_result(first_num, second_num):
    return random.choice([
        ('+', first_num + second_num),
        ('-', first_num - second_num),
        ('*', first_num * second_num)
    ])

def get_math_question_and_result():
    num1, num2 = get_random_number(), get_random_number()
    math_operator, result = get_random_math_sign_and_result(num1, num2)
    math_expression = f'{num1} {math_operator} {num2}'
    correct_answer = str(result)
    question = f'Question: {math_expression}'
    return correct_answer, question

def generate_instructions():
    instructions = 'What is the result of the expression?' 
    return instructions


def run_calc_game():
    receive_instructions(generate_instructions)
    run_engine(get_math_question_and_result)
