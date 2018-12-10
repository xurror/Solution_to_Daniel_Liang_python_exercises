kilogram = 1
pound = 20
print("KILOGRAMS \t POUNDS \t | \t POUNDS \t KILOGRAMS")

while (kilogram in range(1, 200)) or (pound in range(20, 520)):
    pounds = kilogram * 2.2
    kilograms = pound / 2.2
    print(str(format(kilogram, "<4.0f")) + str(format(pounds, "20.1f"))
          + " \t |"
          + str(format(pound, "20.0f")) + str(format(kilograms, "20.2f")))

    kilogram += 2
    pound += 5
    
