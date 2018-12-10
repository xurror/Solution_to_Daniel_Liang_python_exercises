subtotal, gratuity_rate = eval(input("Enter the subtotal and gratuity rate\n"))
gratuity = (gratuity_rate / 100) * subtotal
total = gratuity + subtotal
print("The gratuity is", gratuity, "and the total is", total)
