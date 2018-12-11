# Liang 8.7

def getNum(uppercaseLetter):
    numMap = (('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', 'I'), ('J', 'K', 'L'),\
              ('M', 'N', 'O'), ('P', 'Q', 'R', 'S'), ('T', 'U', 'V'), ('W', 'X', 'Y', 'Z'))
    for num in numMap:
        for letter in num:
            if letter == uppercaseLetter:
                return numMap.index(num) + 2

def letterToNum(word):
    pNum = ''
    for letter in word:
        pNum += str(getNum(letter.upper()))
    return pNum

def main():
    phoneNum = input('Enter a phone number with/without dashes: ').split('-')

    if len(phoneNum) == 3:
        print ('%s-%s-%s' % (phoneNum[0], phoneNum[1], letterToNum(phoneNum[2])))
    else:
        print ('%s%s' % (phoneNum[0][:6], letterToNum(phoneNum[0][6:])))

if __name__ == '__main__':
    main()
