'''

Write a function that, given the start start_num and end end_num values, return a list containing all the numbers inclusive to that range. See examples below.

'''


def inclusive_list(start_num, end_num):

    if start_num > end_num:
        return [start_num]
    else:
        ans = []

        for num in range(start_num, end_num + 1):
            ans.append(num)

    return ans