# (Number of files in a directory) Write a program that prompts the user to enter a
# directory and displays the number of files in the directory.

import os

def getNumberOfFiles(path):
    count = 0
    if not os.path.isfile(path):
        lst = os.listdir(path)
        for subdirectory in lst:
            count += getNumberOfFiles(path + "\\" + subdirectory)
    else:
        count += 1
    return count

def test():
    inputDirectory = input("Enter a directory:")

    print("Total number of files inside the directory is", str(getNumberOfFiles(inputDirectory)))

test()