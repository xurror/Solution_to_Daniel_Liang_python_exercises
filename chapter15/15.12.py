# L 15.12

def findLargest(l):
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], findLargest(l[1:]))

def main():
    nums = input('Enter a list of number: ').split(',')
    nList = [int(n) for n in nums]
    print (findLargest(nList))

if __name__ == '__main__':
    main()
