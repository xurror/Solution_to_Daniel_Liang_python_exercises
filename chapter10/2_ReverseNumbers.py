'''Program to reverse a list of integers entered by user'''

def reverse(list1):
    for i in range(len(list1)-1, -1, -1):
        print(list1[i], end = " ")

    
def main():
    list1 = eval(input("Enter list of numbers: "))
    print("Reverse of the entered list is: ", end="")
    reverse(list1)
     
main()