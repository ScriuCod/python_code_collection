# time complexity
# O(nLogn)time - big O of n logarithm of n time
# used for merge sort, heap sort, quick sort algorithms
# O(n)time - big O of n time


# this is a brute force approach:
# it's a non-optimal time complexity, but it's the simplest to implement
# O(nLogn)time | O(n)space
def sortedSquaredArray(array):
    result = [i * i for i in array]
    result.sort()
    return result


# solution with more optimal time complexity
# solve the problem in a linear time,
# this can be made because our input is sorted in ascending order
# O(n)time | O(n)space
def sortedSquaredArray(array):
    result = []
    while array:
        if abs(array[0]) >= abs(array[-1]):
            biggest_number = array.pop(0)
        else:
            biggest_number = array.pop(-1)
        result.insert(0, biggest_number * biggest_number)

    return result


# another one
# O(n^2)time | O(n)space
def sortedSquaredArray(array):
    result = [0 for _ in array]
    for count, value in enumerate(result):
        if abs(array[0]) >= abs(array[-1]):
            biggest_number = array.pop(0)
        else:
            biggest_number = array.pop(-1)
        result[-1 - count] = biggest_number * biggest_number

    return result


# their solutions
# O(nLogn)time | O(n)space
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()
    return sortedSquares


# you need to go to this array one time, and you create the array that you will return
# O(n)time | O(n)space
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallervalueIdx = 0
    largervalueIdx = len(array) - 1

    for indx in reversed(range(len(array))):
        smallervalue = array[smallervalueIdx]
        largervalue = array[largervalueIdx]

        if abs(smallervalue) > abs(largervalue):
            sortedSquares[indx] = smallervalue * smallervalue
            smallervalueIdx += 1
        else:
            sortedSquares[indx] = largervalue * largervalue
            largervalueIdx -= 1

    return sortedSquares