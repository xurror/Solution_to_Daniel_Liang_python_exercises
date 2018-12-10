#Find 100 Palindrome prime numbers 

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


def isPrime(num):
    temp=2
    while temp<=num/2:
        if num%temp==0:
            return False
        temp+=1
    return True


def isPalindromePrime():
    cnt=0
    num=2
    while cnt<=100:
        if isPrime(num)==True and Reverse(num)==num:
            cnt+=1
            if cnt<=10:
                print(num,end="   ")
            elif cnt>10 and cnt<=20:
                print(num,end="  ")
            elif cnt>20 and cnt<=30:
                print(num,end="  ")
            elif cnt>30 and cnt<=40:
                print(num,end="  ")
            elif cnt>40 and cnt<=50:
                print(num,end="  ")
            elif cnt>50 and cnt<=60:
                print(num,end="  ")
            elif cnt>60 and cnt<=70:
                print(num,end="  ")
            elif cnt>70 and cnt<=80:
                print(num,end="  ")
            elif cnt>80 and cnt<=90:
                print(num,end="  ")
            elif cnt>90 and cnt<=100:
                print(num,end="  ")
            else: 
                print(num,end=" ")
            
            if cnt%10==0:
                print()
        num+=1
 

isPalindromePrime() 
