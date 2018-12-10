# Liang 5.20 (A and B)

LIMIT = 7

def displayPatternA():
    for i in range(1, LIMIT):
        for j in range(1, i + 1):
            print (j, end=' ')
        print ()

def displayPatternB():
    for i in range(1, LIMIT):
        for j in range(1, LIMIT - i + 1):
            print (j, end=' ')
        print ()

def main():
    print ('Pattern A'); displayPatternA()
    print ('\n\nPattern B\n'); displayPatternB()

main()
