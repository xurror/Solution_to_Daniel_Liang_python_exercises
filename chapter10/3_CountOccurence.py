'''Program to count the occurrences of numbers in a list'''

def CountOccur(list1):
    temp= [0]*100
    
    for num in list1:
        temp[num] +=1
        
    for i in range(len(temp)):
        if(temp[i]>1):
            print(i, "occurs", temp[i], "times")
        elif(temp[i]==1):
            print(i, "occurs", temp[i], "time") 
                 

def main():
    list1 = eval(input("Enter integers between 1 and 100: "))
    CountOccur(list1)

main()