# (Binary to decimal) Write a recursive function that parses a binary number as a
# string into a decimal integer. The function header is as follows:
# def binaryToDecimal(binaryString):
# Write a test program that prompts the user to enter a binary string and displays its
# decimal equivalent.

def binaryToDecimal(binaryString):
    if len(binaryString) == 0:
        return 0
    else:
        return 2**(len(binaryString) - 1) * (int(binaryString[0])) + binaryToDecimal(binaryString[1:len(binaryString)])

def test():
    binaryString = input("Enter a binary number:")

    print("The decimal equivalent of the binary string is", binaryToDecimal(binaryString))

test()