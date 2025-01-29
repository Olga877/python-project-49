import random
from brain_games.games.common_game_engine import run_engine, receive_instructions

OPERATORS = ('+', '-', '*')

def generate_instructions():
    instructions = 'What is the result of the expression?' 
    return instructions


def generate_question_and_answer_calc():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    math_operator = random.choice(OPERATORS)
    math_expression = f'{num1} {math_operator} {num2}'
    result = eval(math_expression)
    correct_answer = str(result)
    question = f'Question: {math_expression}'
    return correct_answer, question



def run_calc_game():
    receive_instructions(generate_instructions)
    run_engine(generate_question_and_answer_calc)
