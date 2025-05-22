# Grading System Program

# Get the user's score
score_input = input("Enter your score (0 - 100): ")

# Validate input
if score_input.isdigit():
	score = int(score_input)
	
	# Grade Logic
	if score >= 90:
		grade = 'A'
	elif score >= 80:
		grade = 'B'
	elif score >= 70:
		grade = 'C'
	elif score >= 60:
		grade = 'D'
	else:
		grade = 'F'
	
	print(f"Your grade is: {grade}")
else:
	print("Invalid input. Please enter a number between 0 and 100.")
