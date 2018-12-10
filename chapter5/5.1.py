number = eval(input("Enter an integer,"
                        + "the input ends if it is 0: "))
counter = 1
total = 0
positive_numbers = 0
negative_numbers = 0

while number != 0:
    if number < 0:
        negative_numbers += 1
    elif number > 0:
        positive_numbers += 1
    counter += 1
    total = abs(number) + total
    number = eval(input("Enter an integer,"
                        + "the input ends if it is 0: "))
if number != 0:  
    average = total / counter
    print("The number of positives is "
          + str(positive_numbers))
    print("The number of negatives is "
          + str(negative_numbers))
    print("The total is", str(total))
    print("The average is", str(format(average, "0.2f")))
else:
    print("You did not enter any value")
