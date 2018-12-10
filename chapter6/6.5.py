def displaySortedNumbers(num1, num2, num3):
    
    print(max(num1, num2, num3), end = ", ")
    
    if num1 != (max(num1, num2, num3) and min(num1, num2, num3)):
        print(num1, end = ", ")
    
    elif num2 != (max(num1, num2, num3) and min(num1, num2, num3)):
        print(num2, end = ", ")
    
    elif num3 != (max(num1, num2, num3) and min(num1, num2, num3)):
        print(num3, end = ", ")
    
    print(min(num1, num2, num3))

def main():
    num1, num2, num3 = eval(input("Enter three numbers: "))
    displaySortedNumbers(num1, num2, num3)

main()