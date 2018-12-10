num = eval(input("Enter an integer: "))
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
factors = []

while num != 1:
    if num % 2 == 0:
        num /= 2
        factors.append(2)
        counter1 += 1
        if num % 3 == 0:
            num /= 3
            factors.append(3)
            counter2 += 1
            if num % 5 == 0:
                num /= 5
                factors.append(5)
                counter3 += 1
                if num % 7 == 0:
                    num /= 7
                    factors.append(7)
                    counter4 += 1
while factors  != []:
    
    print(min(factors), end=", ")
    factors.pop(0)
