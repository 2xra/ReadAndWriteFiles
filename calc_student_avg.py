import csv

students = open("Student_Scores.csv", "r")

student_file = csv.reader(students, delimiter=",")

output = open("student_avg.csv", "w")

for index in student_file:
    St_Average = (int(index[1]) + int(index[2]) + int(index[3])) / 3
    output.write(index[0] + "," + round(St_Average, 2).__str__() + "\n")
