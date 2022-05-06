# Recursion is a way to solve problems by calling the same function
# again and again.


# Basic recursion Function

def print_n(n):
    print(n)
    print2n(n+1)

def print2n(n):
    print(n)
    print3n(n+1)

def print3n(n):
    print(n)
    print4n(n+1)

def print4n(n):
    print(n)
    print5n(n+1)

def print5n(n):
    print(n)



# you can see the body of the function is called recursively until it reaches the base case


def printN(n):
    if n == 5:
        return
    print(n)
    printN(n+1)


if __name__ == "__main__":
    print_n(1)
    printN(1)

