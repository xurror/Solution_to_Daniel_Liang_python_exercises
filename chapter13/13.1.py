'''Program to remove a string in the same file'''

def removeWord(filename, word):
    readfile = open(filename,"r")
    read = readfile.read().split()
    
    newString = ""
    for i in read:
        if word.lower() in i.lower():
            newString += ""
        else:
            newString += i
            
    writefile = open(filename,'w')
    writefile.write(str(newString))

    writefile.close()    
    readfile.close() 
    print("The file has been updated !")

def main():
    filename = input("Enter the input path: ")
    word = input("Enter the word you want to remove: ")
    
    removeWord(filename,word)
    
main()
