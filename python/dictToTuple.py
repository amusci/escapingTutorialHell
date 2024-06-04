'''

Write a function that converts a dictionary into a list of keys-values tuples.

'''


def dict_to_list(d):
    return sorted([(k,v) for k, v in d.items()])