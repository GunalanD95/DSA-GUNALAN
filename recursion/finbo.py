# Fibonacci numbers is a series of numbers in which each number is the sum of the two preceding numbers.\
# The first two numbers are 1 and 1.
# formula: fib(n) = fib(n-1) + fib(n-2)


def Fibonacci(n):
    if n < 2:
        return n

    return Fibonacci(n-1) + Fibonacci(n-2)                 # recursive call to the function




if __name__ == "__main__":
    k = Fibonacci(3)
    print(k)