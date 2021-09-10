# e_insertion+sort.py

'''
title: insertion sort
author: James Ma
date-created: September 10, 2021
'''

from myFunctions import *

def insertionSort(LIST):
    '''
    splits the list into a sorted and unsorted section and then takes the left-most value from the unsorted section and places it into the sorted section
    :param LIST: (list) unsorted
    :return: (none)
    '''
    for i in range(1, len(LIST)):

        INDEX_VALUE = LIST[i] # stores current value being sorted

        SORTED_INDEX = i - 1

        # Traversing through the sorted index
        while SORTED_INDEX >=0 and INDEX_VALUE < LIST[SORTED_INDEX]:
            LIST[SORTED_INDEX + 1] = LIST[SORTED_INDEX] # move sorted value up one (to make space)
            SORTED_INDEX = SORTED_INDEX - 1
        LIST[SORTED_INDEX + 1] = INDEX_VALUE # The +1 adjusts for the -1 that occurs at the end of the while loop

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        insertionSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(i)
    print(getAverage(TIMES))