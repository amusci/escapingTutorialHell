"""

Create a function that returns the list of numbers from a given range.

But for multiples of three, return “Eda” instead of the number
and for the multiples of five, return “Bit”.
For numbers which are multiples of both three and five, return “EdaBit”.

"""

def eda_bit(start, end):
    ans = []
    for i in range(start,end + 1):
        if i % 3 == 0 and i % 5 == 0:
            ans.append("EdaBit")
        elif i % 3 == 0:
            ans.append("Eda")
        elif i % 5 == 0:
            ans.append("Bit")
        else:
            ans.append(i)
    return ans