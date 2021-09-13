# f_factorials.py
'''
title: Factorial Recursion
author: James Ma
date-created: September 13, 2021
'''

def factorial(NUMBER):
    '''
    determines the factorial of the given number
    :param NUMBER: (int)
    :return: (int)
    '''
    # base case
    if NUMBER == 1:
        return NUMBER
    else:
        # recursive case
        return NUMBER * factorial(NUMBER - 1)

if __name__ == "__main__":
    NUM = int(input("Enter a number: "))

    # check if the number is negative
    if NUM < 0:
        print("Sorry, factorials do not exist for negative numbers")
    elif NUM == 0:
        print("The factorial of 0 is 1")
    else:
        print(f'The factorial of {NUM} is {factorial(NUM)}.')
