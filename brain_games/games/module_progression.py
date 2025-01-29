import random
import prompt


name = prompt.string('May I have your name? ')

def run_engine():
   iterations_number = 3
   for _ in range(iterations_number):
      final_list = get_progression()
      
      missing_number = random.choice(final_list)
      index_of_missing_number = final_list.index(missing_number)
      final_list[index_of_missing_number] = '..'
      correct_answer = str(missing_number)
      final_list = ' '.join(map(str, final_list))
      question = f'Question: {final_list}'

      print(question)
      answer = prompt.string('Your answer: ')
      if answer.lower() == correct_answer:
            print("Correct!")
      else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n Let's try again, {name}!")
            return
   print(f'Congratulations, {name}!')


def get_progression():
   start_number = random.randint(1, 100)
   step = random.randint(1, 5)
   progression_length = random.randint(5, 10)
   progression_list = []
   for i in range(progression_length):
      progression_list.append(start_number + (i-1)*step)
   return progression_list


def run_progression_game():
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
   
    run_engine()
 


