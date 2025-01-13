from random import randint



def is_even():
    message = 'Correct!'
    x = randint(1, 20)
    print(f'Question: {x}')
    y = input()
    i = 1
    print(f'Your answer: {y}')
    if (x % 2 == 0 and y == 'yes') or (x % 2 != 0 and y == 'no'):
        while (i < 3) and ((x % 2 == 0 and y == 'yes') or (x % 2 != 0 and y == 'no')):
            print(message)
            x = randint(1, 20)
            print(f'Question: {x}')
            y = input()
            i+=1 
        print('Congratulations, name!')
    elif x % 2 == 0 and y == 'no':
            message = "'no' is wrong answer ;(. Correct answer was 'yes'./n Let's try again, Bill!"
            print(message)
    elif x % 2 != 0 and y == 'yes':
            message = "'yes' is wrong answer ;(. Correct answer was 'no'./n Let's try again, Bill!"
            print(message)
    
    else:
        print('Try again')


    

# def even():
#     print('Answer "yes" if the number is even, otherwise answer "no".')
#     # message = 'Correct!'
#     i = 1
#     while (i <= 3) and (message == 'Correct!'):
#         is_even()
#         i+=1
#     print('Congratulations, name!')



is_even()

