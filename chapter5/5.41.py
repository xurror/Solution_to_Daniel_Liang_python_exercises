count = 1
num = eval(input("Enter a number (0: for end of input): "))
num1 = num
num1 = max

while num != 0:
    num = eval(input("Enter a number (0: for end of input): "))

    if num == num1:
        count += 1
    elif num > num1:
        num = max
        num1 = max
        count = 1
    print(num)
print(max(num), count)
