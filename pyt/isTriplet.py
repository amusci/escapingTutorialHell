def is_triplet(n1, n2, n3):

    nums = [n1, n2, n3]

    nums.sort()
    check = (nums[0] ** 2) + (nums[1] ** 2)
    if check == (nums[2] ** 2):
        return True
    else:
        return False