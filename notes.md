# CSE3110/CSE3310 - Iterative and Recursive Algorithm Lessons

## CSE3310 Iterative Algorithms
Iterative Algorithms use loops to process arge sets of data.

## Linear Search

Linear Search is the easiest to program, but least efficient method of search. It processes the data line by line, similar to how brute force decryption algorithms crack passwords by starting at "a" and attempting every possibility until "zzz..."

```python
FOUND = False
for i in range (len(list)):
        if VALUE == LIST[i]:
            FOUND = True
            break
```

Linear search processing time is dependent on the length of the array. Arrays that are 10 000 indices or higher can take a noticeable amount of time to process.

### Measuring processing time
We use  ```time.perf_counter()```to measure the overall time taken before processing data.

For more accurate results, we use the average of at least 30 trials and then use ```statistics.mean()``` to find the average.

### Binary Search
Binary search follows the _divide and conquer_ technique of finding a value. It takes an ordered set of data and tests the midpoint. Then it cuts the line in half and reruns the process.
__Steps for Dinary Search__
1. Sort the data if unsorted
2. Determine the midpoint of the list
3. Test if the midpoint is the same as the Value?
   * If they're the same, end the program.
4. Is the value larger than the midpoint value?
   * If so, redefine the lowest value in the range of the list to one value above the midpoint and re-run the algorithm.
   * Else, redefine the highest value in the range of the list to one value below the midpoint and re-run the algorithm.
5. Repeat 1-4 until value is found.

* Advantages of Binary Search
    * Significantly faster than linear search.
* Disadvantage of Binary Search
    * List must be in order
    * Harder to program

## Sorting Data
Just like searching algorithms, sorting algorithms have varying levels of efficiency. There are several types of sort including bubble, selection, insertion, and merge. (Python uses Timsort, which is a hybrid of merge and insertion sorted designed by Tim Peters in 2002.)

### Bubble Sort

Bubble sort compares two adjacent values on the list and arranges them from lowest to highest. Then it moves to the next index pair and repeats until it reaches the end of the unsorted list. 

Advantages are that it is easy to program and takes less memory, but the disadvantages are that its processing time is directly proportional to the length of the data set. However, the set is often fully sorted before the last iteration. 

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 5 | 11 | 17 | 7 | 13 | __19__ |
| 1 | 3 | 5 | 11 | 7 | 13 | __17__ | 19 | 
| 1 | 3 | 5 | 7 | 11 | __13__ | 17 | 19 |
| 1 | 3 | 5 | 7 | __11__ | 13 | 17 | 19 |
| 1 | 3 | 5 | __7__ | 11 | 13 | 17 | 19 |
| 1 | 3 | __5__ | 7 | 11 | 13 | 17 | 19 |
| 1 | __3__ | 5 | 7 | 11 | 13 | 17 | 19 |