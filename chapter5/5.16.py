n1, n2 = eval(input("Enter two numbers n1 and n2: "))
l = []
l.append(n1)
l.append(n2)
d = min(l)

while d >= 1:
    if n1 % d == 0 and n2 % d == 0:
        break
    d -= 1

print("The GCD is " + str(d))
