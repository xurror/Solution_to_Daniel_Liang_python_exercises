#Program to check whether the Credit Card number is valid or not 
import math

def isValid(num):
    if getSize(num)> 16 or getSize(num)<13:
        return False
    elif getPrefix(num,1)==4 or getPrefix(num,1)==5 or getPrefix(num,1)==6 or getPrefix(num,2)==37:
        pass
    else:
        return False
    sum1 = sumOfDoubleEvenPlace(num) + sumOfOddPlace(num)
    return sum1 % 10 == 0

def sumOfDoubleEvenPlace(num):
    sum1=0
    while num>0:
        num=num//10
        digit=getDigit((num % 10) * 2)
        sum1+=digit
        num=num//10
    return sum1
  
def getDigit(num):
    if num>9:
        num -= 9
        return num
    else:
        return num

def sumOfOddPlace(num):
    sum1=0
    while num>0:
        digit=num%10
        digit=getDigit(digit)
        sum1+=digit
        num=num//100
      
    return sum1

def prefixMatched(num,d):
    if d>num:
        return False
    diff=getSize(num)-getSize(d)
    d=num/math.pow(num,diff)
    return d
  
def getSize(num):
    size = 0
    while num>0:
        size+=1
        num=num//10
    
    return size

def getPrefix(num,k):
    if (prefixMatched(num,k)):
        return k,num   
     
def main():
    ccnumber=eval(input("Enter the Credit Card Number: "))
    if (isValid(ccnumber)):
        print("Credit Card number is Valid")
    else:
        print("Credit Card number is not Valid")
    
main()


  
