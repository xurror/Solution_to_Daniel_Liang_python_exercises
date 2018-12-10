#Program to find the palindrome of a number using functions

def Reverse(N):
    count=""
    str1=""
    while N!=0:
        count=N%10
        str1=str(str1)
        count=str(count)
        str1=str1+count
        count=int(count)
        N=N//10
        
    str1=int(str1)
    return str1
  
  
def isPalindrome():
    inputNum = eval(input("Enter the number: "))
    if Reverse(inputNum) == inputNum:
        print("The number", inputNum,"is a palindrome")
    else:
        print("The number", inputNum,"is not palindrome")

isPalindrome() 