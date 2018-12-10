import random
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)

answer = eval(input("What is the sum of " + str(number1) + " and " + str(number2) + " and " + str(number3) + " is: "))

print("The sum", number1, "+", number2, "+", number3, "=", answer, "is", number1 + number2 + number3 == answer)
