'''Program to count the characters lines and words'''

def main():
    file1 = input("Enter a filename: ").strip()
    readfile = open(file1, "r")
    
    stringFile = readfile.read() 
    word=stringFile.split()
    sum1=0
    for i in word:
        sum1+=len(i)
    print(str(sum1) + " characters") 
    print(str(len(stringFile.split())) + " words") 
    print(str(len(stringFile.split('\n'))) + " lines")
    
    
    readfile.close() 
main()
