'''Recursive method to do sum of digits'''

def SumOfDigits(n):
    if(n==0):
        return n
    else:
        return n%10+ SumOfDigits(n//10)
    
    
def main():
    input1=eval(input("Enter the number: "))
    print("Sum of digits is",SumOfDigits(input1))
    
    
main()