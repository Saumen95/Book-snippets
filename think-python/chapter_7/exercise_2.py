import math


def eval_loop():
    while True:
        response = input('please enter a statement to be evaluated: ')
        if response == 'done':
            print('quitting. your most recent input was', oldresponse)
            break
        print(eval(response))
        oldresponse = response

eval_loop()