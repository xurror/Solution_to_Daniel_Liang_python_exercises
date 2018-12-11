'''Program to process scores'''

def main():
    file1 = input("Enter a filename: ").strip()
    readfile = open(file1, "r")
    
    
    stringFile = readfile.read() 
    word=stringFile.split()
    
    Scores=[eval(x) for x in word]
    total = len(Scores)
    sum1 = 0
    for i in Scores:
        sum1 += i
    
    average=sum1/total
    
    print("There are",total," Scores")
    print("The Total is",sum1)
    print("The Average is",average)
    
    readfile.close()

main()
