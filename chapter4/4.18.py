conversion = eval(input("Enter \"0\" to convert dollars to RMB and \"1\" vice versa: "))
exchange_rate = eval(input("Enter the exchange rate from dollars to RMB: "))


if conversion == 0:
    USD = eval(input("Enter the dollar amount: "))
    RMB = exchange_rate * USD
    print(USD, "is", RMB)
elif conversion == 1:
    RMB = eval(input("Enter the Chinese Renminbi amount: "))
    USD = RMB / exchange_rate
    print(RMB, "is", USD)
