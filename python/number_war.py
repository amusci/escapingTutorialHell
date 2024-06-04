"""

There's a great war between the even and odd numbers.

Many numbers already lost their lives in this war and it's your task to end this.

You have to determine which group sums larger: the evens or the odds. The larger group wins.

Create a function that takes a list of integers, sums the even and odd numbers separately, then returns the
difference between the sums of the even and odd numbers.

"""




def war_of_numbers(lst):
    even = 0
    odd = 0
    for num in lst:
        if num % 2 == 0:
            even += num
        else:
            odd += num

    return abs(even-odd)