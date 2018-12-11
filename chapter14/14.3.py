'''Program to check the keywords in a python file'''
import os.path
import sys

def main():
    keyWords = {"and", "as", "assert", "break", "class",
    "continue", "def", "del", "elif", "else",
    "except", "False", "finally", "for", "from",
    "global", "if", "import", "in", "is", "lambda",
    "None", "nonlocal", "not", "or", "pass", "raise",
    "return", "True", "try", "while", "with", "yield"}
    
    filename = input("Enter a Python filename: ").strip()
    
    if not os.path.isfile(filename): 
        print("File", filename, "does not exist")
        sys.exit()
    
    readfile = open(filename, "r") 
    words = readfile.read().split() 
    count = 0
    countKeyword={}
    for word in words:
        if word in keyWords:
            count += 1
            countKeyword[word]=count
    
    for key in countKeyword:
        print(key + ":" + str(countKeyword[key]))
    
    readfile.close()

main()