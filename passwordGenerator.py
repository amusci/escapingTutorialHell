import random
import string


def passwordGenerator(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f'Your password {password}')
    return password


if __name__ == "__main__":
    length = int(input('How long would you like your password to be?: '))
    passwordGenerator(length)
