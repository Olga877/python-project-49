import random
from brain_games.games.common_game_engine import run_engine, receive_instructions


def generate_instructions():
    instructions = 'What number is missing in the progression?' 
    return instructions


def get_progression():
   start_number = random.randint(1, 100)
   step = random.randint(1, 5)
   progression_length = random.randint(5, 10)
   progression_list = []
   for i in range(progression_length):
      progression_list.append(start_number + (i-1)*step)
   return progression_list


def generate_question_and_answer_progression():
   final_list = get_progression()
   missing_number = random.choice(final_list)
   index_of_missing_number = final_list.index(missing_number)
   final_list[index_of_missing_number] = '..'
   correct_answer = str(missing_number)
   final_list = ' '.join(map(str, final_list))
   question = f'Question: {final_list}'
   return correct_answer, question


def run_progression_game():
    receive_instructions(generate_instructions)
    run_engine(generate_question_and_answer_progression)
 


