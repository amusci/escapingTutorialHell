"""Create a function that takes three arguments a, b, c
and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive."""


def count_vowels(txt):
    vowels = set('aeiou')
    count = 0
    for i in txt:
        if i in vowels:
            count += 1

    return count

if __name__ == "__main__":
    print(count_vowels("Celebration"))