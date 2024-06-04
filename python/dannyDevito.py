"""

I'm trying to watch some lectures to study for my next exam but I keep getting distracted by meme compilations, vine compilations, anime, and more on my favorite video platform.

Your job is to help me create a function that takes a string and checks to see if it contains the following words or phrases:

    "anime"
    "meme"
    "vines"
    "roasts"
    "Danny DeVito"

If it does, return "NO!". Otherwise, return "Safe watching!".

"""


def prevent_distractions(txt):
    distractions = ["anime",
                    "meme",
                    "vines",
                    "roasts",
                    "Danny",
                    "DeVito"]
    words = txt.split()
    print(words)

    for i in words:
        if i in distractions:
            return "NO!"
    return "Safe Watching!"