# i_quick_sort.py
'''
title: quick sort
author: James Ma
date-created: September 15, 2021
'''

from myFunctions import *

def quickSort(LIST, FIRST_INDEX, LAST_INDEX):
    '''
    A quicksort algorithm
    :param LIST: (list)
    :param FIRST_INDEX: (int)
    :param LAST_INDEX: (int)
    :return: (none)
    '''

    if FIRST_INDEX < LAST_INDEX:
        PIVOT_VALUE = LIST[FIRST_INDEX] #  select first number as pivot number.

        LEFT_INDEX = FIRST_INDEX + 1
        RIGHT_INDEX = LAST_INDEX

        DONE = False
        while not DONE:
            while LEFT_INDEX <= RIGHT_INDEX and LIST[LEFT_INDEX] <= PIVOT_VALUE:
                # if the leftmost value is below the right value and below the pivot value, move one index to the right.
                LEFT_INDEX += 1
            while RIGHT_INDEX >= LEFT_INDEX and LIST[RIGHT_INDEX] >=PIVOT_VALUE:
                # if the right most value is above the left value and greater than the pivot value, move one index to the left.
                RIGHT_INDEX -= 1
            if RIGHT_INDEX < LEFT_INDEX: # base/stopping case
                DONE = True
            else:
                # swaps two values
                TEMP = LIST[LEFT_INDEX]
                LIST[LEFT_INDEX] = LIST[RIGHT_INDEX]
                LIST[RIGHT_INDEX] = TEMP
        # move the pivot value to its correct spot on the list
        TEMP = LIST[FIRST_INDEX]
        LIST[FIRST_INDEX] = LIST[RIGHT_INDEX]
        LIST[RIGHT_INDEX] = TEMP

        quickSort(LIST, FIRST_INDEX, RIGHT_INDEX-1)
        quickSort(LIST, RIGHT_INDEX + 1, LAST_INDEX)

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        quickSort(NUMBERS, 0, len(NUMBERS) - 1)
        END = getTime()
        TIMES.append(END - START)
        print(i)
    print(getAverage(TIMES))