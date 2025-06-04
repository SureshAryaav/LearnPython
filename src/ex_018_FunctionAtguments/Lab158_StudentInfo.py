def student_info(**kwargs):
	for key, value in kwargs.items():
		print(f"{key.capitalize()}: {value}")

student_info(name="Ravi", grade="A", subject="Math")
