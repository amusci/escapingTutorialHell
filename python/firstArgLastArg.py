'''

    first_arg() should return the first parameter passed in.
    last_arg() should return the last parameter passed in.

'''


def first_arg(*nums):
    if nums:
        return nums[0]
    return None


def last_arg(*nums):
    if nums:
        return nums[-1]
    return None