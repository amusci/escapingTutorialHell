"""

A number n is apocalyptic if 2^n contains a string of 3 consecutive 6s (666 being the presumptive "number of the beast").

Create a function that takes a number n as input. If the number is apocalyptic, find the index of 666 in 2^n,

and return "Repent! X days until the Apocalypse!" (X being the index).

If not, return "Crisis averted. Resume sinning.".

"""

def apocalyptic(n):
    idk = 2 ** n
    satan = '666'
    if satan in str(idk):
        x = str(idk).find(satan)

        return f("Repent! {x} days until the Apocalypse!")
    return "Crisis averted. Resume sinning."