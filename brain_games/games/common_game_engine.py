import prompt

name = prompt.string('May I have your name? ')


def receive_instructions(get_instructions):
    print(f'Hello, {name}!')
    instructions = get_instructions()
    print(instructions)


def run_engine(get_question_and_answer):
    iterations_number = 3
    for _ in range(iterations_number):
        correct_answer, question = get_question_and_answer()

        print(question)
        answer = prompt.string('Your answer: ')
        if answer.lower() == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
