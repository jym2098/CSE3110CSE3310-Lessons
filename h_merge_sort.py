# h_merge_sort.py
'''
title: Merge Sort
author: James Ma
date-created: September 13 2021
'''

from myFunctions import *

def mergeSortedLists(LIST_LEFT, LIST_RIGHT):
    '''
    merge two sorted lists (linear)
    :param LIST_LEfT: (list)
    :param LIST_RIGHT: (list)
    :return: (list)
    '''

    # Special case: one or both of the lists are empty
    if len(LIST_LEFT) == 0:
        return LIST_RIGHT
    elif len(LIST_RIGHT) == 0:
        return LIST_LEFT

    # General cases
    INDEX_LEFT = 0
    INDEX_RIGHT = 0
    LIST_MERGED = [] # list to build and return
    LIST_LEN_TOTAL = len(LIST_LEFT) + len(LIST_RIGHT)
    while len(LIST_MERGED) < LIST_LEN_TOTAL:
        if LIST_LEFT[INDEX_LEFT] <= LIST_RIGHT[INDEX_RIGHT]: # value on the left list is smaller (or equal) so it should be selected
            LIST_MERGED.append(LIST_LEFT[INDEX_LEFT])
            INDEX_LEFT = INDEX_LEFT + 1
        else: # Right value is smaller
            LIST_MERGED.append(LIST_RIGHT[INDEX_RIGHT])
            INDEX_RIGHT = INDEX_RIGHT + 1

        # If we are at the end of one of the lists, we can take a shortcut.
        if INDEX_RIGHT == len(LIST_RIGHT):
            # Reached the end of the right list
            # append the remainder of the left list and break.
            LIST_MERGED = LIST_MERGED + LIST_LEFT[INDEX_LEFT:]
            break
        elif INDEX_LEFT == len(LIST_LEFT):
            LIST_MERGED = LIST_MERGED + LIST_RIGHT[INDEX_RIGHT:]
            break

    return LIST_MERGED

def mergeSort(LIST):
    if len(LIST) <= 1:
        return LIST
    else:
        MIDPOINT = len(LIST) // 2
        LEFT = LIST[:MIDPOINT]
        RIGHT = LIST[MIDPOINT:]
        return mergeSortedLists(mergeSort(LEFT), mergeSort(RIGHT))


if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        mergeSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(i)
    print(getAverage(TIMES))
