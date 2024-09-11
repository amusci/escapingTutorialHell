'''

In mathematics, interval is the difference between the largest number and the smallest number in a list.

To illustrate:

A = (3, 5, 7, 23, 11, 42, 80)

Interval of A = 80 - 3 = 77

Create a function that takes a list and returns ":)" if the interval of the list is equal to any other element; otherwise return ":(".

'''

def face_interval(num):
    if not isinstance(num, list):
        return ":/"
    sorted_nums = sorted(num)
    interval = sorted_nums[-1] - sorted_nums[0]
    if interval in sorted_nums:
        return ":)"
    else:
        return ":("
        
        


if __name__ == "__main__":
    print(face_interval([5, 2, 8, 3, 11]))