# b_binarySearch.py
'''
title: Binary Search
author: James Ma
date-created: September 7, 2021
'''

import time, random, statistics

def binarySearch(LIST, VALUE)  :
    '''
    Searches through the data to find the value
    :param LIST: SORTED Data to be searched
    :param VALUE: Data to be found
    :return: (None)
    '''
    START = 0
    END = len(LIST) - 1

    while START <= END:
        MIDPOINT = (START + END) // 2
        #print(LIST[MIDPOINT])
        if LIST[MIDPOINT] == VALUE:
            return
        elif VALUE > LIST[MIDPOINT]:
            START = MIDPOINT + 1
        else:
            END = MIDPOINT - 1
    return

# Make a large data set
NUMBERS = []
START_TIME = time.perf_counter()
for i in range(200000):
    if random.randrange(2) == 1:
        NUMBERS.append(i)
END_TIME = time.perf_counter()
TOTAL_TIME = END_TIME - START_TIME
print(len(NUMBERS), TOTAL_TIME)

# TEST binary search


TIMES = []

NUMBER = NUMBERS[random.randrange(len(NUMBERS))]
print(NUMBER)
START_TIME = time.perf_counter()
binarySearch(NUMBERS, NUMBER)
END_TIME = time.perf_counter()
TOTAL_TIME = END_TIME - START_TIME
TIMES.append(TOTAL_TIME)

print(statistics.mean(TIMES))
