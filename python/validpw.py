'''

Create a function to test if a string is a valid pin or not.

A valid pin has:

    Exactly 4 or 6 characters.
    Only numerical characters (0-9).
    No whitespace.

'''


def valid(txt):
    if len(txt) == 4 or len(txt) == 6:
        return txt.isdigit()
    else:
        return False

if __name__ == "__main__":
    print(valid("1234aa"))