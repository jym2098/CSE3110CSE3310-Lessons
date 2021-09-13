# g_recursiveBinarySearch.py
'''
title: Recursive Binary Search
author: James Ma
date-created: September 13, 2021
'''

from myFunctions import *
from random import randrange

def recurBinarySearch(LIST, VALUE):
    '''
    Uses recursion to search for a value
    :param LIST: (list)
    :param VALUE: (value)
    :return: (none)
    '''

    MIDPOINT = len(LIST) // 2

    # base case

    if LIST[MIDPOINT] == VALUE:
        return
    else:
        # recursive process
        if VALUE < LIST[MIDPOINT]:
            return recurBinarySearch(LIST[:MIDPOINT], VALUE)
        else:
            return recurBinarySearch(LIST[MIDPOINT+1:], VALUE)

if __name__ == "__main__":
    NUMBERS = getList(100000)
    TIMES = []
    for i in range(30):
        NUMBER = NUMBERS[randrange(len(NUMBERS))]
        START = getTime()
        recurBinarySearch(NUMBERS, NUMBER)
        END = getTime()
        TIMES.append(END - START)
        print(i)
    print(getAverage(TIMES))

