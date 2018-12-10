reversedNumber = []

def reverse(number):
    n = 0
    while number > 10:

        reverse = number % 10
        reversedNumber.append(reverse)
        number //= 10
        print(reverse, end= '')
    print(number)

def main():

    number = eval(input("Enter a number: "))
    reverse(number)

main()

