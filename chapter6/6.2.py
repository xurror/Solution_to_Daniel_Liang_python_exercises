#Program to write a function to display the sum of digits

def SumOfDigits(num):
    count=0
    total=0
    
    while num!=0:
        count=num%10
        total+=count
        num=num//10
    return total


def main():
    InputNum = eval(input("Enter the number: "))
    print("The sum of digits of ", InputNum, " is: ",SumOfDigits(InputNum))

main()