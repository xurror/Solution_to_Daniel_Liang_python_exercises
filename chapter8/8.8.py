# Liang 8.8

def binaryToDecimal(binaryString):
    i = len(binaryString)
    dec = 0
    while (i > 0):
        if (binaryString[i-1] == '1'):
            dec += 2**(len(binaryString) - i)
        i -= 1
    return dec

def main():
    binary = input('Enter a binary: ')
    print ('Decimal Value: %d' % binaryToDecimal(binary))

if __name__ == '__main__':
    main()
