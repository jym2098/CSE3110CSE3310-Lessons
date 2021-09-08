# myFunctions.py
'''
title: common functions for testing
author: James Ma
date-created: September 8, 2021
'''

import random, statistics, time

def getList(SIZE):
    '''
    returns a sorted list of approximately size SIZE
    :param SIZE: (int) Approximate size of list
    :return: (list)
    '''
    NUMBERS = []
    for i in range(SIZE * 2):
        if random.randrange(2) == 1:
            NUMBERS.append(i)

    return NUMBERS

def getRandomList(SIZE):
    '''
    returns a randomized list of approximately size SIZE
    :param SIZE: (int)
    :return: (list)
    '''
    NUMBERS = getList(SIZE)
    NEW_LIST = []
    for i in range(len(NUMBERS)):
        NEW_LIST.append(NUMBERS.pop(random.randrange(len(NUMBERS))))
    return NEW_LIST

def getAverage(LIST):
    '''
    returns the average of the given list
    :param LIST: (list) Times for calculation
    :return: (float) average of times
    '''
    return statistics.mean(LIST)

def getTime():
    '''
    returns the current performance time
    :return: (float)
    '''
    return time.perf_counter()

if __name__ == "__main__":
    NUMBERS = getRandomList(10)
    TIME = getTime()
    AVERAGE = getAverage([4, 5, 6])
    print(NUMBERS, TIME, AVERAGE)