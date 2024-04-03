import re


def trebuchet(filepath):
    total = 0
    with open(filepath, "r") as file:
        for line in file:
            no_letters = re.sub("[a-zA-Z]", "", line)
            no_letters = no_letters.strip()
            print(no_letters)
            if no_letters:
                first = int(no_letters[0])
                last = int(no_letters[-1])
                total += first * 10 + last

    return total


if __name__ == "__main__":
    print(trebuchet("text_file.txt"))
