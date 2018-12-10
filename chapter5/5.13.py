number = 100
numberList = []

for number in range(100, 201):
    if (number % 5 == 0) or (number % 6 == 0):
        if (number % 5 == 0) and (number % 6 == 0):
            continue
        else:
            numberList.append(number)
        
while numberList != []:            
    for i in range(0, 10):
    
        if numberList != []:
            print(min(numberList), end=" ")
            numberList.pop(0)
    print()
        
            


