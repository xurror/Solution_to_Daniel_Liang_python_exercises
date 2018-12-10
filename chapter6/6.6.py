def displayPattern(n):

    k = 1

    for i in range(0, n):
        
        print(k, end = "")

        for j in range(0, k):
        print()

        k += 1

def main():

    n = eval(input("Enter a number: "))
    displayPattern(n)

main()

            