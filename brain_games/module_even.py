from random import randint
import prompt


def is_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    message = 'Correct!'
    x = randint(1, 20)
    print(f'Question: {x}')
    y = prompt.string('Your answer: ')
    i = 1
    
    if (x % 2 == 0 and y == 'yes') or (x % 2 != 0 and y == 'no'):
            while i < 3:
                print(message)
                x = randint(1, 20)
                print(f'Question: {x}')
                y = prompt.string('Your answer: ')
                i += 1
                print(message)
                print(f'Congratulations, {name}!')
    if x % 2 == 0 and y != 'yes':
            message = f"'{y}' is wrong answer ;(. Correct answer was 'yes'.\n Let's try again, {name}!"
            print(message)
    elif x % 2 != 0 and y != 'no':
            message = f"'{y}' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {name}!"
            print(message)

