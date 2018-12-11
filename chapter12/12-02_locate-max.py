# Liang 12.2

class Location:
    def __init__(self, row, column, maxValue):
        self.row = row
        self.column = column
        self.maxValue = maxValue

def locateLargest(arr):
    maxValue = arr[0][0]
    row = col = 0
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > maxValue:
                maxValue = arr[i][j]
                row = i
                col = j
    return Location(row, col, maxValue)

def main():
    uInput = input('Enter the number of rows and columns in the list: ')
    arrDimn = [int(d) for d in uInput.split(',')]
    arr = []
    nRow = 0    
    
    while nRow < arrDimn[0]:
        cRow = [int(v) for v in input('Enter row %d: ' % nRow).split()]
        if len(cRow) > arrDimn[1]:
            raise RuntimeError('Out of Bound Exception: Row %d' % nRow)
        arr += [cRow]
        nRow += 1

    loc = locateLargest(arr)    
    print ('The location of the largest element is %d at (%d, %d)' % (loc.maxValue, loc.row, loc.column))

if __name__ == '__main__':
    main()
