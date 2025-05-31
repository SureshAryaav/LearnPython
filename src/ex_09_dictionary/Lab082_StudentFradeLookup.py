# Dictionary of student grades
grades = {
	"Alice": 85,
	"Bob": 92,
	"Charlie": 78
}

name = input("Enter student name: ")

# Check if name exists
if name in grades:
	print(f"{name}'s grade: {grades[name]}")
else:
	print("Student not found.")
