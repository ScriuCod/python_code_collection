by Tim Ruscica

## Solution and explication
### This is a brute force approach:
```python
def sortedSquaredArray(array):
    result = [i*i for i in array]
    result.sort()
    return result
```
#### Time complexity 
Is **O(n log n)**, where n is the length of the input array. This is because the list comprehension creates a new list of squared values in O(n) time, and the subsequent sorting operation using the sorted function has a time complexity of O(n log n).

#### Space complexity 
Is **O(n)**, where n is the length of the input array. This is because the list comprehension creates a new list of squared values with the same length as the input array. Therefore, the space required is proportional to the size of the input array.


### Solution with more optimal time complexity
```python
def sortedSquaredArray(array):
    result = []
    while array:
        if abs(array[0]) >= abs(array[-1]):
            biggest_number = array.pop(0)
        else:
            biggest_number = array.pop(-1)
        result.insert(0, biggest_number * biggest_number)
    return result
```
#### Time complexity  
Is O(n), where n is the length of the input array.

The algorithm uses a while loop that continues until the input array is empty. In each iteration, it performs constant-time operations such as accessing the first and last elements of the array, comparing their absolute values, popping elements from the array, and inserting elements into the result list using the `insert` method.

The key observation is that each element in the input array is removed once using either `pop(0)` or `pop(-1)`, and the result list is updated with the squared value of that element. Since each element is processed only once, the time complexity is linear in the size of the input array, resulting in O(n) time complexity.

#### Space complexity
Is also O(n), where n is the length of the input array.

The algorithm creates an empty result list initially. During each iteration of the while loop, it inserts an element at the beginning of the result list using the `insert` method. The size of the result list grows in proportion to the number of iterations, which is equal to the size of the input array.

Therefore, the space complexity is O(n) since the space usage grows linearly with the size of the input array.