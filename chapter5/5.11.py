numberOfStudents = eval(input("Enter the number of students: "))
numberOfScores = 0
scores = []

while numberOfScores < numberOfStudents:
    score = eval(input("\nEnter the student scores: "))
    scores.append(score)
    numberOfScores += 1
print("\nThe maximum score is " + str(max(scores)))
scores.pop(numberOfStudents - 1)
print("\nThe second highest is " + str(max(scores)))
    
