def sum(i1, i2):
    result = 0
    for i in range(i1, i2 + 1):
        result += i

    return result

def main():
    print("The sum from 1 to 10 is", sum(1, 10))
    print("The sum from 20 to 37 is", + sum(20, 37))
    print("The sum from 35 to 49 is", + sum(35, 49))

main()
