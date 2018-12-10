a, b, c, d, e, f = eval(input("Enter values for a, b, c, d, e, f: "))

D = ((a * d) - (b * c))

if D == 0:
    
    print("The equation has no solution")
    exit()

x = ((e * d) - (b * f)) / D
y = ((a * f) - (e * c)) / D

print("The solution to the equation is X =", x, "Y =", y)
 
