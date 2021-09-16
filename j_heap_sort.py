# j_heap_sort.py
'''
title: heap sort
author: James Ma
date-created: September 16, 2021
'''

from myFunctions import *

def heapify(LIST, LEN_ARRAY, ROOT_INDEX):
    '''
    moves highest value to index 0 (top of the binary tree)
    :param LIST: (list)
    :param LEN_ARRAY: (int)
    :param ROOT_INDEX: (int)
    :return: (none)
    '''

    LARGEST_INDEX = ROOT_INDEX

    LEFT_INDEX = 2 * ROOT_INDEX + 1
    RIGHT_INDEX = 2 * ROOT_INDEX + 2

    # check if left child is greater than the parent
    if LEFT_INDEX < LEN_ARRAY and LIST[ROOT_INDEX] < LIST[LEFT_INDEX]:
        LARGEST_INDEX = LEFT_INDEX

    # check if rigt child is greater than the parent
    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX

    # Change the root/parent if needed
    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP

        heapify(LIST, LEN_ARRAY, LARGEST_INDEX)

# The main functuon to sort an array

def heapSort(LIST):
    LEN_ARRAY = len(LIST)

    # build a max heap (highest number of the tree is at the top)
    for i in range(LEN_ARRAY, -1, -1):
        heapify(LIST, LEN_ARRAY, i)

    # extract highest element
    for i in range(LEN_ARRAY-1, 0, -1):
        LIST[i], LIST[0] = LIST[0], LIST[i] # swap variable values, not for IB
        heapify(LIST, i, 0)

if __name__ =="__main__":
    TIMES = []
    for i in range(1):
        NUMBERS = getRandomList(10000)
        START = getTime()
        heapSort(NUMBERS)
        END = getTime()
        TIMES.append(END-START)
        print(i)
    print(getAverage(TIMES))