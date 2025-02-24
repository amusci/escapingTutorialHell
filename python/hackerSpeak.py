'''

Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.

In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.

'''

def hacker_speak(txt):
    
    ans = ""
    rules = {

        "a" : "4",
        "e" : "3",
        "i" : "1",
        "o" : "0",
        "s" : "5"
    }

    for i in txt:
        if i in rules:
            ans += rules[i]
        else:
            ans += i
    return ans