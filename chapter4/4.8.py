num1, num2, num3 = eval(input("Enter three integers: "))

if num1 < num2 and num2 < num3:
    print(str(num1) + "\n" + str(num2) + "\n" + str(num3))
elif num2 < num1 and num1 < num3:
    print(str(num2) + "\n" + str(num1) + "\n" + str(num3))

elif num3 < num1 and num1 < num2:
    print(str(num3) + "\n" + str(num1) + "\n" + str(num2))
elif num1 < num3 and num3 < num2:
    print(str(num1) + "\n" + str(num3) + "\n" + str(num2))

elif num3 < num2 and num2 < num1:
    print(str(num3) + "\n" + str(num2) + "\n" + str(num1))
elif num2 < num3 and num3 < num1:
    print(str(num2) + "\n" + str(num3) + "\n" + str(num1))
