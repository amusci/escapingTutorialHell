# word guessing game ig
import random

wordList = ['yup', 'sup', 'one', 'two', 'three', 'population', 'bomb']
count = 0


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    # print(wordIndex)
    return wordList[wordIndex]

def showBoard(missed,correct,secret):

    blanks = '_' * len(secret)




if __name__ == "__main__":
    getRandomWord(wordList)
