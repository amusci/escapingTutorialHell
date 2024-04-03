'''

Create a function that takes a value as an argument and returns the type of this value.

'''


def get_type(value):
    type_of_types = {
        int: "int",
        str: "str",
        bool: "bool",
        list: "list",
        tuple: "tuple",
        dict: "dict",
        set: "set",
        type(None): "NoneType"
    }

    return type_of_types.get(type(value))