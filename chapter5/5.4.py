miles = 1
print("MILES \t KILOMETERS")

for miles in range(1, 10):
    kilometers = miles * 1.609
    print(str(format(miles, "<10.0f")) + str(kilometers))
    
