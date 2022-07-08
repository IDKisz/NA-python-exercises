# Create a function calculating sum for any number of integers given to that function as arguments

# put your code here

def calculate_sum(*arguments):
    sum = 0
    for number in arguments:
        sum += number
    return sum

print(calculate_sum(4, 6, 2, 5, 4, 2, 4))