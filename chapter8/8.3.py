''' Write a program to check passwords based on following rules:
A password must have at least eight characters.
A password must consist of only letters and digits.
A password must contain at least two digits.
'''

def CheckPassword(str1):
    countChr = 0
    countNum = 0
    
    if(len(str1)>=8):
        for i in range(0, len(str1)):
            if (ord(str1[i].lower())>= 97 and ord(str1[i].lower()) <= 122):
                countChr +=1
            elif ord(str1[i]) >=48 and ord(str1[i])<=57:
                countNum +=1
            else:
                return False
        if(countNum >=2 and countChr> 0):
            return True
        else:
            return False
    else:
        return False


def main():
    pwd = input("Enter your password: ")
    if (CheckPassword(pwd)):
        print("Valid Password")
    else:
        print("Invalid Password")

main()