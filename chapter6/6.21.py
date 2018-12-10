def sqrt(n):
    
    lastGuess = 1
    nextGuess = (lastGuess + (n / lastGuess)) / 2

    if (nextGuess - lastGuess) > 0.0001:
        
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        sqrt = nextGuess

    else:
        sqrt = nextGuess

def main():
    n = eval(input("Enter a number: "))
    sqrt(n)
main()