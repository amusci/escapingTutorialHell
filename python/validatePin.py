'''

Create a function to test if a string is a valid pin or not.

A valid pin has:

    Exactly 4 or 6 characters.
    Only numerical characters (0-9).
    No whitespace.

'''

def valid(txt):
    if len(txt)!=4 and len(txt)!=6:
        return False
    if not txt.isdigit():
        return False
    if " " in txt:
        return False
    return True
        
        


if __name__ == "__main__":
    print(valid("451356"))