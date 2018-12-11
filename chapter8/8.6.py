''' Function to count the letters in a string '''

def countLetters(s):
    count = 0
    for i in range(0, len(s)):
            if (ord(s[i].lower())>= 97 and ord(s[i].lower()) <= 122):
                count +=1
    
    return count

def main():
    s = input("Enter a string: ")
    print("The number of letters in ",s,"is: ", countLetters(s))
    
main()