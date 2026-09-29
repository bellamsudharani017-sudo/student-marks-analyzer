print("===== Student Marks Analyzer =====")

name = input("Enter student name: ")

marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if average >= 50:
    result = "Pass"
else:
    result = "Fail"

print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
print("Result:", result)