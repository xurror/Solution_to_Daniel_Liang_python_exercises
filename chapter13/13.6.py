'''Program that counts the number of words in 
President Abraham Lincoln’s Gettysburg Address given in the url'''

import urllib.request

def main():
    readfile = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
    stringFile = readfile.read()
    print("The number of words in the file is " + str(len(stringFile.split())))
    
main()