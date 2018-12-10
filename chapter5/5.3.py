kilogram = 1
print("KILOGRAMS \t POUNDS")

for kilogram in range(1, 200, 2):
    pounds = kilogram * 2.2
    print(str(format(kilogram, "<4.0f")) + str(format(pounds, "20.1f")))
    
