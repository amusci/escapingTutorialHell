'''

    first_arg() should return the first parameter passed in.
    last_arg() should return the last parameter passed in.

'''


def first_arg(*nums):
    if nums:

        return nums[0]
    else:
        return None


def last_arg(*nums):
    if nums:

        return nums[-1]
    else:
        return None