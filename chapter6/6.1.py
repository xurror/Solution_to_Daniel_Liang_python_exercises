def getPentagonalNumber(n):

    getPentagonalNumber = (n * (3*n - 1)) / 2

    return getPentagonalNumber

def main():
    n = eval(input("Enter a number: "))
    print(getPentagonalNumber(n))

main()