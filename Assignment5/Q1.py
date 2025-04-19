import os
studentmarks={}
number_of_students = int(input("Enter number of students: "))
for  i in range( number_of_students):
    name = input("Enter student name:")
    marks = float(input("Enter student marks: "))
    studentmarks[name] = marks

#print(studentmarks)

inputStudentName = input("Enter the student''s name: ")

expectedOutput = studentmarks.get(inputStudentName)

if expectedOutput == None:
    print("Student not found.")
else:
    print(inputStudentName +"'s marks: ",expectedOutput)
    



