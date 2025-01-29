import random
import prompt
from brain_games.games.common_game_engine import run_engine

MIN_NUMBER = 1
MAX_NUMBER = 100 
PRIME_LIST = [2, 3,	5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73,	79,	83,	89,	97] 
INSTRUCTIONS = 'Answer "yes" if given number is prime. Otherwise answer "no".' 
name = prompt.string('May I have your name? ')



def is_prime(number):
    return number in PRIME_LIST


def generate_question_and_answer_progression():
    given_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(given_number) else 'no'
    question = f'Question: {given_number}'
    return correct_answer, question


def run_prime_game(): 
    print(f'Hello, {name}!')
    print(INSTRUCTIONS)
    run_engine(generate_question_and_answer_progression)
    print(f'Congratulations, {name}!')