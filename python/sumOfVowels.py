'''

Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers.
Vowel	Number
A	      4
E	      3
I	      1
O	      0
U	      0

'''


def sum_of_vowels(sentence):
    count = 0
    for char in sentence:
        if char == "A" or char == "a":
            count += 4
        elif char == "E" or char == "e":
            count += 3
        elif char == "I" or char == "i":
            count += 1
    return count
        


if __name__ == "__main__":
    print(sum_of_vowels("I love edabit!"))