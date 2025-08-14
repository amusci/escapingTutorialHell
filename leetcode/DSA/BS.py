import random

'''

https://www.youtube.com/watch?v=NFhOrxtXXcM

BINARY SEARCH OF A SORTED ARRAY

we are looking for the index of the number 7 in the array

think of a sorted array [1,2,4,5,7,9,10]

choose the middle [1,2,4,(5),7,9,10]

we compare the middle (5) to our chosen value we want (7)

since 7 > 5,  we can cut out all numbers to the LEFT of the middle (1,2,4)

now our array is [7,9,10]

find the middle which is [7,(9),10]


7 < 9, since our array is sorted, we can eliminated the right half of the sub array
[7] == 7 therefore we found our index.


if we choose something like find the number 100 in the array [1,2,4,5,7,9,10]

it would return -1 meaning that it is not in the array.





'''


def quickSort(arr, lowIndex, highIndex):
    pivot = arr[highIndex]
    leftPointer = lowIndex
    rightPointer = highIndex

    if leftPointer > rightPointer:
        return
    while leftPointer < rightPointer:
        while arr[leftPointer] <= pivot and leftPointer < rightPointer:
            leftPointer += 1
        while arr[rightPointer] >= pivot and leftPointer < rightPointer:
            rightPointer -= 1

        swap(arr, leftPointer, rightPointer)
    swap(arr, leftPointer, highIndex)

    quickSort(arr, lowIndex, leftPointer - 1)
    quickSort(arr, leftPointer + 1, highIndex)


def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def binarySearch(arr, value):
    lowPointer = 0 # lowest index
    highPointer = len(arr) - 1 # highest index

    while lowPointer <= highPointer:
        middleIndex = (lowPointer + highPointer) // 2 # find the middle index by averaging
        middleNumber = arr[middleIndex]

        if value == middleNumber:
            return middleIndex
        elif value < middleNumber:
            #[1,2,3] if value 1, 1<2 so we would move our pointer to  the middle - 1 to show [1]
            highPointer = middleIndex - 1
        else:
            # [1,2,3] if value 3, 3>2 so we would move our pointer to the middle + 1 to show [3]
            lowPointer = middleIndex + 1

    return -1 # return -1 if value not in array


if __name__ == "__main__":
    data = []
    for i in range(100):
        data.append(random.randint(1, 100))

    print(data)
    quickSort(data, 0, len(data) - 1)
    print(data)

    print(binarySearch(data, 5))
