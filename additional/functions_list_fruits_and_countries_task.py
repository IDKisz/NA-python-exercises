# You have two lists: list of fruits and list of countries.
# Create a third list, containing pairs (tuples) of fruits and countries that start with same letter:

# place your code here


fruits = ['cherry', 'apple', 'melon', 'grape', 'pomelo', 'strawberry']
countries = ['vietnam', 'poland', 'sweden', 'india', 'canada', 'finland', 'denmark']


# **************
# Using 'for' loop:
# **************

# place your code here

match_list = []

for i in countries:
    for j in fruits:
        if j[0] == i[0]:
            match = (j, i)
            match_list.append(match)

print(match_list)





# **************
# Using list comprehension:
# **************

# place your code here

match_list2 = [(j,i) for j in fruits for i in countries if j[0] == i[0]]
print(match_list2)