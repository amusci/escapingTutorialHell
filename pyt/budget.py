"""

Create the function that takes a list of dictionaries and returns the sum of people's budgets

"""




def get_budgets(lst):
    return sum(budget["budget"] for budget in lst)