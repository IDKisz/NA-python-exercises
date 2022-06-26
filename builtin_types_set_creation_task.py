# Create a list of unique numbers from lists given:

l1 = [1, 2, 3, 4]
l2 = [1, 2, 12, 44]
l3 = [12, 4, 5, 9]

# put your code here

summary_list = l1 + l2 + l3
unique_list = list(set(summary_list))

print(unique_list)
