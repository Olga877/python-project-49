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
        print(message)
        x = randint(1, 20)
        print(f'Question: {x}')
        y = prompt.string('Your answer: ')
    if (x % 2 == 0 and y == 'yes') or (x % 2 != 0 and y == 'no'):
        print(message)
        x = randint(1, 20)
        print(f'Question: {x}')
        y = prompt.string('Your answer: ')
    if (x % 2 == 0 and y == 'yes') or (x % 2 != 0 and y == 'no'):
        print(message)
        print(f'Congratulations, {name}!')
    elif x % 2 == 0 and y == 'no':
            # y = prompt.string('Your answer: ')
            message = f"'no' is wrong answer ;(. Correct answer was 'yes'.\n Let's try again, {name}!"
            print(message)
    elif x % 2 != 0 and y == 'yes':
            # y = prompt.string('Your answer: ')
            # print(f'Your answer: {y}')
            message = f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {name}!"
            print(message)
    
    else:
        print('Try again')

