'''Program to implement Markov matrix''' 

def checkPositive(matrix):
    check=False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j]>=0):
                check=True
            else:
                check=False
    return check

def checkSumOfElements(matrix):
    check=False
    
    for j in range(len(matrix[0])):
        sum1=0
        for i in range(len(matrix)):
            sum1=matrix[i][j]+sum1
        if(sum1==1):
            check=True
        else:
            check=False
    return check
        
        
        
def main():
    matrix = [] 
    numberOfRows = eval(input("Enter the number of rows  "))
    numberOfColumns = eval(input("Enter the number of columns: "))
    print("Enter a 3 by 3  matrix row by row :")
    
    for i in range(numberOfRows):
        matrix.append([])
        input1 = input()
        eleCol = input1.split(" ")
        k = 0
        for j in range(numberOfColumns):
            matrix[i].append(float(eleCol[k]))
            k +=1

    if checkPositive(matrix) and checkSumOfElements(matrix):
        print("The matrix is Markov ")
    else:
        print("The matrix is not Markov")
        
main()