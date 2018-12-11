''' Program to sort a list using Bubble sort'''

def BubbleSort(lst):
    for x in range(len(lst)):
        for y in range(len(lst)-1):
            if(lst[y] > lst[y+1]):
                temp = lst[y+1]
                temp1 = lst[y]
                lst[y+1] = temp1
                lst[y] = temp
    
    print("The sorted list is: ", lst)
    

def main():
    list1 = eval(input("Enter 10 numbers: "))
    BubbleSort(list1)

main()