'''

Create a function that takes two arguments: a father's current age f_age and his son's current age s_age. Сalculate how many years ago the father was twice as old as his son, or in how many years he will be twice as old.

'''

def age_difference(f_age, s_age):

    age_diff = abs(f_age - (s_age * 2))

    if age_diff >= 0:
        return age_diff
    else:
        return -age_diff