n = eval(input("Enter a number: "))
l = []
z = 0
e = n - 1
for a in range(0, n):
    l.append(z + 1)
    z += 1

z -= 1

for i in range(0, n):


    
    for j in range(0, i+1):
        print(l[z], end= " ")
        z -= 1
        l.pop(e)
        e = e - 1
        z = max(l)
    print()
    z -= 1
    
isPrime divisor 
