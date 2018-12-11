'''Program to add two 2D matrix'''

def printMatrix(m):
        for row in range(len(m)):
            for column in range(len(m[row])):
                print(m[row][column], end = " ")
            print()


def addMatrices(m1, m2):
    if(len(m1) == len(m2)):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1)):
                m3[i].append(m1[i][j] + m2[i][j])
    
        printMatrix(m3)
                
    else:
        print("Matrices of different length cannot be added")

def main():
    matrix1 = [] # Create an empty list
    matrix2 = []
    numberOfRows = 3 #eval(input("Enter the number of rows: ")) 
    numberOfColumns = 3 #eval(input("Enter the number of columns: ")) 
    numbers = input("Enter the matrix1: ")
    value = numbers.split(" ")

    count = 0
    for row in range(numberOfRows):
        matrix1.append([]) # Add an empty new row 
        for column in range(numberOfColumns):
            matrix1[row].append(int(value[count]))
            count += 1
    
    numbers2 = input("Enter the matrix2: ")
    value2 = numbers2.split(" ")

    count = 0
    for row in range(numberOfRows):
        matrix2.append([]) # Add an empty new row 
        for column in range(numberOfColumns):
            matrix2[row].append(int(value2[count]))
            count += 1
    


    print("The sum of matrix 1 and 2 is:")
    addMatrices(matrix1,matrix2)

main() 