"""

Create a function that applies a discount d to every number in the list.

"""




def get_discounts(nums, d):
    ans = []
    deci = (float(d.strip("%")) / 100)

    for num in nums:

        ans.append(num * deci)
    return ans