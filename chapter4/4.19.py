e1, e2, e3 = eval(input("Enter three edges of a triangle: "))

if (e1 + e2 > e3) and (e1 + e3 > e2) and (e3 + e2 > e1):
    print("The perimeter is", (e1 + e2 + e3))

else :
    print("THe input is invalid")
