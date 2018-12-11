'''Program to merge two sorted lists'''

def merge(list1, list2):  
    list3 = []
    i=0
    j=0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i=i+1
        else:
            list3.append(list2[j])
            j=j+1
    
    while i < len(list1):
        list3.append(list1[i])
        i=i+1
    
    while j < len(list2):
        list3.append(list2[j])
        j=j+1
        
    return list3

def main():
    list1 = eval(input("Enter the first sorted list: "))
    list2 = eval(input("Enter the second sorted list: "))
    list3 = merge(list1, list2)
    print("The merged sorted list is: ", list3)

main()