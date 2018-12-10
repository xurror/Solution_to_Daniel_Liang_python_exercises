import random

def printMatrix(n):

    for i in range(0, n):
        for j in range(0, n):
            rand = random.randint(0, 9)
            print(rand, end = " ")

        print()

def main():

    n = eval(input("Enter the order of the matrix: "))
    printMatrix(n)

main()