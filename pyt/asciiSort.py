

'''

Create a function that compares two words based on the sum of their ASCII codes and

returns the word with the smaller ASCII sum.
Examples

ascii_sort(["hey", "man"]) ➞ "man"
# ["h", "e", "y"] ➞ sum([104, 101, 121]) ➞ 326
# ["m", "a", "n"] ➞ sum([109, 97, 110]) ➞ 316

ascii_sort(["majorly", "then"]) ➞ "then"

ascii_sort(["victory", "careless"]) ➞ "victory"

'''


def ascii_sort(lst):
    word1_sum = 0
    word2_sum = 0
    word1 = lst[0]
    word2 = lst[1]
    for i in word1:
        word1_sum += ord(i)
    for j in word2:
        word2_sum += ord(j)
    print(word1_sum, word2_sum)
    if word1_sum < word2_sum:
        return word1
    else:
        return word2