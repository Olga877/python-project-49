import prompt

name = prompt.string('May I have your name? ')

ROUNDS_NUMBER = 3


def receive_instructions(get_instructions):
    instructions = get_instructions()
    print(f'Hello, {name}!\n{instructions}')
    

def run_engine(get_question_and_answer):
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