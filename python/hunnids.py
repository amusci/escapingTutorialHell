# code that calculates when user will be 100

name = input('Please give me your name: ')
age = input('Please give me your current age: ')
current_year = input('Please enter the current year: ')

hunnid = int(current_year) - int(age) + 100

print(f"Hello, {name}! You will be 100 years old in the year of {hunnid}")
