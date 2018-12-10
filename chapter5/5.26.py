n = 1
add = 1 / 3

while n < 100:

    if n % 2 != 0:
        add += n / (n + 2)
    n += 1
#add += 1
print(str(format(add,".1f")))
