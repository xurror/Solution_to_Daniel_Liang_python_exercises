w1, p1 = eval(input("Enter the weight and price for package 1: "))
w2, p2 = eval(input("Enter the weight and price for package 2: "))

pricePerKilo1 = p1 / w1
pricePerKilo2 = p2 / w2

print(pricePerKilo1)
print(pricePerKilo2)

if pricePerKilo1 < pricePerKilo2:
    print("Package 2 has a better price")
else:
    print("Package 1 has a better price")
