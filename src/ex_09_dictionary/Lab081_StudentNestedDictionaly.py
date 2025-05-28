students = {
	"S001": {"name": "Ravi", "age": 20, "marks": 85},
	"S002": {"name": "Priya", "age": 21, "marks": 90}
}

for sid, info in students.items():
	print(f"\nStudent ID: {sid}")
	for key, value in info.items():
		print(f"{key}: {value}")
