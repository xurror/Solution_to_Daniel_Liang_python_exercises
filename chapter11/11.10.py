''' To find the largest sum row and column in a matrix filled with binary numbers'''
import random
    

def printMatrix(m):
        for row in range(len(m)):
            for column in range(len(m[row])):
                print(m[row][column], end = " ")
            print()

def sumofColumn(m, j):#access each column
    sum1 = 0
    for i in range(len(m)):
        sum1 += m[i][j]
    return sum1


def main():
    matrix = []
    row, col = 4,4

    count = 0
    for row in range(row):
        matrix.append([]) # Add an empty new row 
        for column in range(col):
            matrix[row].append(random.randint(0, 1))
            count += 1
    
    printMatrix(matrix)

    # Check rows for largest index
    SumRow = sum(matrix[0])
    ListRow = [0]
    for i in range(1, col):
        if SumRow < sum(matrix[i]):
            SumRow = sum(matrix[i])
            ListRow = [i]
        elif SumRow == sum(matrix[i]):
            ListRow.append(i)
            
    print("The largest row index: ", end = "")
    
    for i in range(len(ListRow) - 1):
        print(ListRow[i], end = ", ")
    print(ListRow[len(ListRow) - 1])

    # Largest Column Index
    SumCol = sumofColumn(matrix, 0)
    ListCol = [0]
    for j in range(1, col):
        if SumCol < sumofColumn(matrix, j):
            SumCol = sumofColumn(matrix, j)
            ListCol = [j]
        elif SumCol == sumofColumn(matrix, j):
            ListCol.append(j)
            
    print("The largest column index: ", end = "")
    for i in range(len(ListCol) - 1):
        print(ListCol[i], end = ", ")
    print(ListCol[len(ListCol) - 1])

main()
