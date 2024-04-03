'''

Your task is to create a fence worth $1 million.


You are given the price of the material (per character),


meaning the length of the fence will change depending on the cost of the material.

Create a function which constructs this pricey pricey fence, using the letter "H" to build.

construct_fence("$50,000") ➞ "HHHHHHHHHHHHHHHHHHHHHHHHHHHH"
# 20 fence posts were set up ($1,000,000 / $50,000 = 20)

''' 

def construct_fence(p):
    clean_cost = p.replace("$", "").replace(",", "")

    amount = 1000000 // int(clean_cost)

    return 'H' * amount
