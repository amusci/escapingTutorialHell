
'''

October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be lowercase, so write a function to normalize a sentence.

Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end.

'''

# WITH CAPITALIZE()

def normalize(txt):
    if txt.isupper():
        return txt.capitalize() + "!"
    else:
        return txt
        


# WITHOUT CAPITALIZE()

def normalize(txt):
    if txt.isupper():
        return txt[0].upper() + txt[1:].lower() + "!"
    else:
        return txt



if __name__ == "__main__":
    print(normalize("CAPS LOCK DAY IS OVER"))