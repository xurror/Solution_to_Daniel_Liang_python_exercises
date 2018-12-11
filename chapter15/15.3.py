'''Program to do GCD recursive method'''

def GCD(a,b):
    if a%b ==0:
        return b
    else:
        GCD(b,a%b)
        
        
def main():
    num1,num2=eval(input("Enter two numbers: "))
    if(num1 < num2):
        num1,num2=num2,num1
    print("GCD :", GCD(num1, num2))
    
    
main()