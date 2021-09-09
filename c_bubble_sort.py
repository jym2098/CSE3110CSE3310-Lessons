# c_bubble_sort.py
'''
title: bubble sort
author: James Ma
date-cretaed: September 8, 2021
'''

from myFunctions import *

def bubbleSort(LIST):
    '''
    compares two adjacent values and moves the highest one to the end of the list.
    :param LIST: (list) unsorted
    :return:
    '''
    for i in range(len(LIST) - 1, 0 , -1): # going backwards from second-last value to first value.
        for j in range(i): # start from the first value and move to the highest number
            if LIST[j] > LIST[j + 1]:
                TEMP = LIST [j]
                LIST[j] = LIST[j + 1]
                LIST[j + 1] = TEMP

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        #print(NUMBERS)
        START = getTime()
        bubbleSort(NUMBERS)
        END = getTime()
        #print(NUMBERS)
        TIMES.append(END-START)
        print(i)
    print(getAverage(TIMES))
