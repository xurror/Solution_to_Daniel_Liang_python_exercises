import math

a, b, c =eval(input("Enter a, b, and c the coefficients of a quadratic equation: "))

discriminant = math.pow(b, 2) - (4 * a * c)

#r1 = (-b + math.sqrt(discriminant)) / (2 * a)
#r2 = (-b - math.sqrt(discriminant)) / (2 * a)

if discriminant == 0:

    r1 = (-b + math.sqrt(discriminant)) / (2 * a)
    r2 = (-b - math.sqrt(discriminant)) / (2 * a)
    r1 = r2

    print ("The root of the equation is", r1)

elif discriminant > 0:

    r1 = (-b + math.sqrt(discriminant)) / (2 * a)
    r2 = (-b - math.sqrt(discriminant)) / (2 * a)

    print("The roots of the equation are", r1, "and", r2)

else:

    print("The equation has no real roots")
    
