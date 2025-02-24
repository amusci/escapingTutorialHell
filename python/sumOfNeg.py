'''

Create a function that takes a list of positive and negative numbers. Return a list where the first element is the count of positive numbers and the second element is the sum of negative numbers.

'''

def sum_neg(lst):

    count = 0
    sum_of_neg = 0
    ans = []

    if not lst:
        return []
    
    else:

        for i in lst:
            if i >= 0:
                count += 1
            else:
                sum_of_neg += i
    
    return [count, sum_of_neg]
	
	



if __name__ == "__main__":
    print(sum_neg([91, -4, 80, -73, -28]))
