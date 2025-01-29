import math
import random

from brain_games.games.common_game_engine import (
    receive_instructions,
    run_engine,
)


def generate_instructions():
    instructions = 'Find the greatest common divisor of given numbers.' 
    return instructions


def generate_question_and_answer_progression():
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    given_numbers = num1, num2
    correct_answer = str(math.gcd(num1, num2))
    question = f'Question: {given_numbers}'
    return correct_answer, question


def run_gcd_game():
    receive_instructions(generate_instructions)
    run_engine(generate_question_and_answer_progression)
 