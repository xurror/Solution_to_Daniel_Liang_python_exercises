tuition = 10000
years = 0
total = 10000

for years in range(0, 11):
    tuition = tuition * 1.05
    while years < 4:
        total += tuition
        years += 1
print("Tuition at the tenth year will be ", str(format(tuition, ".2f")))
print("The total fees after 4 years is ", str(format(total, ".2f")))
