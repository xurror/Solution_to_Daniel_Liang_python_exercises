#numberOfPrimes = 50
numberOfPrimesPerLine = 8
count = 0
number = 2
        
print("The prime numbers between 2 and 1000 are:")

for numberOfPrimes in range(2, 1000):

    isPrime = True

    divisor = 2

    while divisor <= number / 2:
        if number % divisor == 0:

            isPrime = False
            break
        divisor += 1

    if isPrime:
        count += 1

        print(number, end= " ")

        if count % numberOfPrimesPerLine == 0:

            print('\r')

    number += 1
