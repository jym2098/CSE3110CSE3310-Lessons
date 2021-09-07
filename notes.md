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

