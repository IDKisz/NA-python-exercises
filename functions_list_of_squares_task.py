# Create a list of squares of first 10 integers:
# [1, 4, 9, ..., 100]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# **************
# Using 'for' loop:
# **************

# place your code here
list_square_1 = []

for i in range(1, 11):
    list_square_1.append(i * i)

print(list_square_1)

# **************
# Using built-in 'map':
# **************

# place your code here

def square_number(number):
    return number * number

list_square_2 = list(map(square_number, numbers))

print(list_square_2)

# **************
# Using list comprehension:
# **************

# place your code here

list_square_3 = [a*a for a in numbers]

print(list_square_3)







