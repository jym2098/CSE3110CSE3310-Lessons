# d_selection_sort.py
'''
title: selection sort
author: James Ma
date-created: September 9, 2021
'''

from myFunctions import *

def selectionSort(LIST):
    '''
    compares the current index value with the rest of the set. It will find the lowest value and switch it with the current index value.
    :param LIST: (list) unsorted list
    :return: None
    '''
    for i in range(len(LIST) - 1): # for each number up to the last number
        MINIMUM = LIST[i] # Assume the first number is the smallest
        for j in range(i+1, len(LIST)): # test each subsequent number
            if LIST[j] < MINIMUM: # test if the current number is smaller than the minimum
                MINIMUM = LIST[j] # update the minimum with the new smallest value
                PLACE = j # save the index of the new smallest value
        if MINIMUM < LIST[i]: # test of the first number is the smallest number
            TEMP = LIST[i] # save the first number value
            LIST[i] = LIST[PLACE] # update first number value with smallest value
            LIST[PLACE] = TEMP # update index of smallest value with first value
    return

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        selectionSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(i)
    print(getAverage(TIMES))
