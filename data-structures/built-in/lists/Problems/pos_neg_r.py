# Python program to print all positive numbers in a range

# Input: start = -4, end = 5

# 1 Using For Loop

def printpos():
    for i in range(-4,5):
        if i >= 0:
            print("positive numbers are:",i)

printpos()


def printneg():
    for i in range(-4,5):
        if i < 0:
            print("negative numbers are:",i)

printneg()