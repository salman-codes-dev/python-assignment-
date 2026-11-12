#  1. Student Grade Calculator
# Takes a student name as input
student_name = input("Enter student name: ")

# 2. Takes marks for three subjects as input
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# 3. Calculate total marks and average marks
total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3

# 4. Determines the grade using if-elif-else statements
if average_marks >= 80: grade = 'A+'
elif average_marks >= 70: grade = 'A'
elif average_marks >= 60: grade = 'B'
elif average_marks >= 50: grade = 'C'
else: grade = 'F'

# 5. Display all information using f-strings
print("\n--- Student Result Summary ---")
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Grade: {grade}")
