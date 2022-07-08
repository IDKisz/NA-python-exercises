# You have two lists, both randomly ordered: list of integers and list of string integers.
# Create a dictionary with numbers that match: {1: '1', 3: '3', 10: '10'}


integers = [3, 1, 4, 6, 10]
strings = ['1', '5', '10', '3']


# **************
# Using 'for' loop:
# **************

# place your code here
pair = {}

for k in sorted(integers):
    for v in strings:
        if int(v) == k:
            pair[k] = v

print(pair)

# **************
# Using dict comprehension:
# **************

# place your code here

pair1 = {k:v for k in sorted(integers) for v in strings if int(v) == k}
print(pair1)
