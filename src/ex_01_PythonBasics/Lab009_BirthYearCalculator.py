# Ask the user for their name and age
name = input("What is your name? ")
age_input = input("How old are you? ")

# Validate age input
if age_input.isdigit():
	age = int(age_input)
	current_year = 2025
	birth_year = current_year - age
	
	print(f"{name}, you were probably born in {birth_year}.")
else:
	print("Please enter a valid number for age.")
	
