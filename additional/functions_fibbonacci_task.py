### Create function that calculates Fibonacci sequence for given N:
      # Fib(0) == 0
      # Fib(1) == 1
      # Fib(N) == Fib(N-1) + Fib(N-2)

# **************
# Do it with iteration
# **************
# place your code here


def calculate_fib(number):
    sequence = []
    if number < 0:
        warning = "Incorrect input"
        return warning
    elif number == 1:
        sequence = [0]
    else:
        sequence = [0, 1]
        for n in range(2, number-1):
            sequence.append(sequence[n-1] + sequence[n-2])
    return sequence


number = int(input("Enter a number"))

if number <= 0:
    print("Please type positive intiger")
else:
    print("Fibonacci sequence:")
    print(calculate_fib(number))


# **************
# Do the same but using recursion
# **************
# place your code here


def calculate_fib_recursion(n):
    if n == 1 or n == 0:
        return n
    else:
        return (calculate_fib_recursion(n-1) + calculate_fib_recursion(n-2))


number = int(input("Enter a number"))

if number <= 0:
    print("Please type positive intiger")
else:
    print("Fibonacci sequence:")
    for x in range(number-1):
        print(calculate_fib_recursion(x))
