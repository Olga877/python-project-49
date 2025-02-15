import prompt

from brain_games.const import ROUNDS_NUMBER


def run_engine(get_question_and_answer, game_instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{game_instruction}')

    for _ in range(ROUNDS_NUMBER):
        correct_answer, question = get_question_and_answer()

        print(question)
        answer = prompt.string('Your answer: ')
        if answer.lower() == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n" 
                  f" Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')