hex_number = eval(input("Enter a hexadecimal value: "))

if hex_number == str:
    if hex_number == 'A' or 'a':
        print("hex_number = 10")
    elif hex_number == 'B' or' b':
        print("hex_number = 11")
    elif hex_number == 'C' or 'c':
        print("hex_number = 12")
    elif hex_number == 'D' or 'd':
        print("hex_number = 13")
    elif hex_number == 'E' or 'e':
        print("hex_number = 14")
    elif hex_number == 'F' or 'f':
        print("hex_number = 15")
    else:
        print("Invalid input")

else:
    print("The hex number is ", hex_number)
