# Program to create a function to check if number is prime or not
def isPrime(num):
    temp=2
    while temp<=num/2:
        if num%temp==0:
            return False
        temp+=1
    return True

def main():
    num=2

    while num<10000:
        if isPrime(num):
            print(num,end="\n")
        num = num + 1

main()