n = 50000
add = 0

while n > 0:
    add += 1 / n
    n -= 1
add += 1
print(str(format(add,".1f")))
