correct_password = "pass123"
attempts = 3

while attempts > 0:
	password = input("Enter password: ")
	if password == correct_password:
		print("Access granted")
		break
	else:
		attempts -= 1
		print(f"Wrong password. Attempts left: {attempts}")

if attempts == 0:
	print("Access denied. Too many attempts.")
