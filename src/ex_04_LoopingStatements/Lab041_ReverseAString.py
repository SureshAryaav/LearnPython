original = input("Enter a string: ")
reversed_str = ""

for char in original:
	reversed_str = char + reversed_str  # Prepend character

print(f"Reversed string: {reversed_str}")
