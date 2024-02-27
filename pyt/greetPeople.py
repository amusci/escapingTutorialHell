"""

In this exercise you will have to:

    Take a list of names.
    Add "Hello" to every name.
    Make one big string with all greetings.

The solution should be one string with a comma in between every "Hello (Name)".

"""

def greet_people(names):
    ans = []

    if names:
        for name in names:
            ans.append("Hello " + name)

    return ', '.join(ans)