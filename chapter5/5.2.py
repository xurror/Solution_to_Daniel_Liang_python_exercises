import random
additionQuestions = 0

while additionQuestions < 10:
    int1 = random.randint(1, 15)
    int2 = random.randint(1, 15)

    total = eval(input("What is the sum of "
                       + str(int1) + " + " + str(int2) + " = "))
    print(str(int1) + " + " + str(int2)
          + " = " + str(total) + " is "
          + str((int1 + int2) == total))
    additionQuestions += 1
