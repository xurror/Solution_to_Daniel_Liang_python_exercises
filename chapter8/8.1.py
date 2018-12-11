# Liang 8.1

def checkSSN(SSN):
    if len(SSN) == 3 and SSN[0]//1000 == 0 and SSN[1]//100 == 0 and SSN[2]//10000 == 0:
        return 'Valid SSN'
    else:
        return 'Invalid SSN'

def main():
    SSN = input('Enter a Social Security Number (ddd-dd-dddd): ').split('-')
    print (checkSSN([int(d) for d in SSN]))
    
if __name__ == '__main__':
    main()
