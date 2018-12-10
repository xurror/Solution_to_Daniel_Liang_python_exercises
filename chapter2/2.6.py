integer = eval(input("Enter an integer between 0 and 1000 : "))
total = 0
while integer > 0:

    digit = integer % 10

    integer = integer // 10

    total += digit
  
print(total)
