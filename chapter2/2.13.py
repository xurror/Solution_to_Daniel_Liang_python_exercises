integer = eval(input("Enter a 4 digit integer : "))
total = 0
a = []

while integer > 0:

    digit = integer % 10

    integer = integer // 10

    a.append(digit)

    a[::-1]
    
print(a[3])
print(a[2])
print(a[1])
print(a[0])

    
