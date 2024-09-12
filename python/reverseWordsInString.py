'''

Given an input string, reverse the string word by word.

'''

def reverse_words(words):
    split = words.split()
    reversed = split[::-1]
    return " ".join(reversed)
    

if __name__ == "__main__":
    print(reverse_words("the sky is blue"))