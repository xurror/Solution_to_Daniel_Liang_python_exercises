'''Program to find the sum of major diagonal of a given matrix'''

def sumMajorDiagonal(m):
    sumMajorDiag = 0
    for i in range(len(m)):
        for j in range(len(m)):
            if(i==j):
                sumMajorDiag += m[i][j]
    
    return sumMajorDiag

def main():
    matrix = [] # Create an empty list
    numberOfRows = eval(input("Enter the number of rows: ")) 
    numberOfColumns = eval(input("Enter the number of columns: "))

    for i in range(numberOfRows):
        matrix.append([])
        print("Enter row ", i, " :", end = " ")
        input1 = input()
        eleCol = input1.split(" ")
        k = 0
        for j in range(numberOfColumns):
            matrix[i].append(int(eleCol[k]))
            k +=1

    
    for row in range(numberOfRows):
        for column in range(numberOfColumns):
            print(matrix[row][column], end = " ")
        print()

    print("The sum of major diagonal is :", sumMajorDiagonal(matrix))

main() 
