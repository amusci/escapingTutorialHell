# Create a function in Python that accepts a single word and returns the number of vowels in that word. In this
# function, only a, e, i, o, and u will be counted as vowels — not y.

vowels = 'a', 'e', 'i', 'o', 'u'


def vowelCount(string):
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    print(f'There are {count} vowels in this string.')


if __name__ == "__main__":
    inp = input('What is the string you would like to count?: ')
    # This block will only be executed if the script is run directly, not if it's imported as a module
    vowelCount(inp)
