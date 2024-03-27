# LEARNING DSA
import random

'''
QUICKSORT
https://youtu.be/h8eyY7dIiN4

Quicksort is basically 3 steps.

1st step: CHOOSE A PIVOT, you can choose any number in the array.
2nd step: Move all numbers that are lower than the pivot to the left, and all numbers that are higher to the right.

example:
[3,8,1,9,4,5,(7)] <------ we choose 7 as our pivot
[5,4,3,1,(7),8,9]

as we can see, the numbers to the left are lower, to the right are bigger.

Now, we can partition [5,4,3,(1)], choosing 1 as our pivot (last element in sub array)
[(1),3,4,5]

We do it again [1,3,4,(5)] choosing 5 as our pivot.
'''


def quickSort(arr, lowIndex, highIndex):
    pivot = arr[highIndex]  # choosing last index as our pivot
    leftPointer = lowIndex
    rightPointer = highIndex

    if leftPointer > rightPointer:  # once this happens, we are done
        return

    while leftPointer < rightPointer:
        while arr[leftPointer] <= pivot and leftPointer < rightPointer:
            leftPointer += 1  # walk left pointer to right
        while arr[rightPointer] >= pivot and leftPointer < rightPointer:
            rightPointer -= 1  # walk right pointer to left

        swap(arr, leftPointer, rightPointer)  # swap left and right when conditions are met
    swap(arr, leftPointer, highIndex)  # swap pivot with left pointer (pivot will be in correct spot)

    quickSort(arr, lowIndex, leftPointer - 1)  # sort the subarray left of pivot
    quickSort(arr, leftPointer + 1, highIndex)  # sort the subarray right of pivot


def swap(arr, index1, index2):
    # swap index 1 and 2
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


if __name__ == "__main__":
    data = []
    for i in range(10):
        data.append(random.randint(0, 100))
    print(data)
    quickSort(data, 0, len(data) - 1)
    print(data)
