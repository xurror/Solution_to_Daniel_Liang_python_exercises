kilometers = 20
miles = 1
print("MILES \t KILOMETERS \t | \t KILOMETERS \t MILES")

while (miles in range(1, 11)) and (kilometers in range(20, 70)):
    kilometer = miles * 1.609
    mile = kilometers * 0.621
    print(str(format(miles, "<4.0f")) + str(format(kilometer, "15.3f"))
          + " \t |"
          + str(format(kilometers, "10.0f")) + str(format(mile, "15.3f")))

    kilometers += 5
    miles += 1
    
