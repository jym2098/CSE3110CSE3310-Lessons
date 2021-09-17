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

### Selection Sort
Selection sort compares the current index value with the rest of the set. It will find the lowest value and switch positions with the lowest position (index). As it runs through the data set, it will select the lowest values and place them in the lower positions. Therefore, it sorts the list from smallest to largest. 

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __3__ | _5_ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | __*5*__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __7__ | 11 | 17 | _19_ | 13 |
| 1 | 3 | 5 | 7 | __*11*__ | 17 | 19 | 13 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 19 | _17_ |
| 1 | 3 | 5 | 7 | 11 | 13 | __17__ | _19_ |

NOTE: Just like bubble sort, the last column does not need sorting because sorting the second-last column will also sort the last column.


### Insertion Sort
Insertion Sort splits the list into two sections: sorted and unsorted. As it progress through the list, it takes the left-most value from the unsorted section and inserts it into the correct location in the sorted section, This algorithm does not scan the entire list each iteration. Instead, the current value needs to only compare with the value immediately to its left. 

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __*5*__ | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | _3_ | __5__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __*19*__ | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | _11_ | __19__ | 17 | 7 | 13 |
| 1 | 3 | 5 | 11 | _17_ | __19__ | 7 | 13 |
| 1 | 3 | 5 | _7_ | 11 | 17 | __19__ | 13 |
| 1 | 3 | 5 | 7 | 11 | _13_ | 17 | __19__ |

* Insertion sort should be faster than selection sort; however, not to the same degree as bubble sort. 
* For IB, you will need to identify, explain, and compare and contrast various iterative sorts. 

## Recursive Algorithms
A __Recursive Algorithm__ calls itself with smaller or simpler input values. Recursive algorithms have a base case, which receives the simples input values. This base stops the recursive portion of the algorithm. When inputs into a recursive algorithm are more complex the base case, a subprocess simplifies the input and returns the new simplified input into the algorithms to process again. 

All iterative algorithms can be written recursively and vice versa; however, certain functions are easier to write in one form over another. 

### Example 1: Testing for the correct input data
```python
# Recursive

def chkInt(VALUE):
    try:
        VALUE = int(VALUE)
        return VALUE
    except ValueError:
        print("You did not enter a number")
        NEW_VALUE = input('Enter a nmber: ')
        return chkInt(NEW_VALUE) # recursive return

# Iterative

def chkInt2(VALUE):
    IS_INTEGER = False
    while not IS_INTEGER:
        try:
            VALUE = int(VALUE)
            IS_INTEGER = True
        except BalueError:
            print("You did npot enter a number")
            VALUE = input("Enter a number: ")
    return VALUE
```
### Iteratives vs. Recursion*

In general, iterative algorithms require more lines of code and more variables than recursive algorithms. They rely on while and for loops to complete the process. Whereas, recursive algorithms do not use as many lines and rely on returns updated values into the same function. Recursion can use more physical memory than interactive algorithms because each instance of the recursive function stays in memory until the base case is reached. Finally, exclusively iterative functions tend to be faster than exclusively recursive functions. However, hybrid iterative and recursive algorithms are fastest. 

### Example 2: Factorials

#### Calculate 7:
7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1 = 5040

BUT!!!!

6! = 6 * 5 * 4 * 3 * 2 * 1 * 1

Therefore, we can rewrite 7! as

7 * 6! = 7 * (6 * 5 * 4 * 3 * 2 * 1 * 1)

Extending this principle,

7! = 7 * (6 * (5 * (4 * (3 * (2 * (1 * (1)))))))

which then can be generatlized into

f(x) = x * (f(x01)), x >= 0

## Recursive Sorting

Recursive sorting uses both recursive and iterative processes. In general, these hybrid sorts are exponentially faster with longer lists. (They are usually measured in a logarithmic scale).

### Merge Sort
Merge sort follows a divide and conquer method of sorting, where the array is split into its base length and then rebuilt by combining progressively larger sorted lists together. The recursive portion is the act of splitting the list and iterative process is the merging of the two smaller lists together.

Oftentimes, this function is separated into splitting and merging functions. 

### Quick Sort
Quick sort (or quicksort) is another divide and conquer method of sorting. Quicksort utilizes an arbitrary value as its pivot, which is then used to place the pivot value in the correct place in the array. It does this by placing all smaller values to the left of the pivot and all larger values to the right of the pivot. Then it places the pivot value where the smaller and larger portions intersect and moves to the next value. It then recurs through the algorithm until the inputted list is one value long. 

NOTE: Quicksorts efficiency is from separating the list into two sections that will never compare values with each other again. 

### Heap Sort

Heap sort uses a binary tree organization of an array to sort higher values to the top of the tree. The process of moving larger values higher in the binary tree is called __heapifying__ (or heapify).

To build the binary tree, each index (starting at 0) will have a left child and right child value (hence binary tree). The index values can be calculated from the following:

```python
left_child = 2 * parentIndex + 1
right_child = 2 * parentIndex + 2

# Sample Tree
LIST = [5, 17, 13, 11, 1, 7, 3]
       5[0]
       /   \
    17[1]  13[2]
    /  \     /  \
11[3]  1[4] 7[5] 3[6]
```

#### Heapify
To heapify the binary tree, the value of the parent index must be higher than the two children. Therefore, the process starts at the bottom of the tree and works its way to the top. If the parent is smaller than one of the children values, it swaps the child and parent values. As heapifying moves throughout the tree, the higher values will progressively get to the top.

When the heapifying process reaches the top, the top value is removed from the tree (and placed at the end of the array) and the value from the highest index (at the bottom of the tree) replaces its position at the top. Then the heapifying process begins again. 

## Big O Notation
Programs have varying levels of efficiency. Big O notation is a means of expressing how efficient an algorithm is in comparison to other algorithms within the same context. The __complexity__ of an algorithm is measured in the amount of time, space, and inputs required to run the algorithm. How long it takes for a program to run is called its __run time__. When measuring efficiency, there is the best case, the worst case, and the average case.

There are many factors that affect run time:
* hardware specifications
* type of data structure
* programming language (complied vs. interpreted)
* competence of the programmer
* complexity of the algorithm
* size of the input

Generally, the complexity of the algorithm and the size of input affects the run time the most. 

Big O notation is the efficiency measurement of the __principle activity__ as the main time measurement. It simplifies activities within the algorithms to the most intensive components. _Big O notation relates the complexity of the algorithm to the size of the input._

### Pigeon Data Transfer Example
Pigeon Transfer Time: 0(1)
Internet Protocol: 0(N) "N is the size of the data"

### Algorithm examples of efficiency

```python
for i in range(len(LIST)):
    print(i)

# Big O Notation: O(N) Linear relationship
```

```python
for i in range(len(LIST)):
    for j in range(len(LIST)):
        print(i,j)

# Big O Notation: O(N * N) or O(N^2) Quadratic Relationship

```
### Examples of Big O Notation

| Notation | Type | Examples | Description |
| --- | --- | --- | --- |
| O(1) | Constant | Hash Table Access | Remain constant regardless of the size of the data set |
| O(log n) | Logarithmic | Binary Search | Increase by a constant. If N doubles, the time to perform increases by a constant, smaller than N amount |
| O(<N) | Sublinear | Search using parallel processing | Performs less than linear and more than logarithmic levels |
| O(N) | Linear | Linear Search | Increase in proportion to N. If N doubles, the time to perform also doubles |
| O( N * log N) | NlogN | quick sort, and merge sort | Increases at a multiple of a constant |
| O(N^2) | Quadratic | bubble sort | Increases in proportion to N * N |
| O(c^N) | Exponential | Traveling salesman problem | Increases based on the exponent N of a constant c |
| O(n!) | Factorial | Traveling salesman problems using brute force | Increases in proportion to the product of all numbers included |

### Rules for Calculating O notation
1. Different steps get added together
2. Drop constants in front ot N
```python
for i in range(len(LIST)):
    print(i + 1)
for i in range(len(LIST)):
    print(i + 2)
   
# O (N + N --> O(2N)
for i in range(len(LIST)):
print(i + 1)
print(i + 2)

# O(N)
```

3. Different Inputs use different variables
```python
for i in range(len(LIST1)):
    print(i)
for i in range(len(LIST2)):
    print(i)

# O(N + M)
```
4. Drop non-dominant terms








