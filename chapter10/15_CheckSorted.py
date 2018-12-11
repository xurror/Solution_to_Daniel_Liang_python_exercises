'''Program to check if the list is sorted'''

def isSorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def main():
    list1 = eval(input("Enter list: "))
    check = isSorted(list1)
    if(check):
        print("The list is sorted")
    else:
        print("The list is not sorted")

main()            