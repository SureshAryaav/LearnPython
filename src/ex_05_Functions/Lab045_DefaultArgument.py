def greet(name="Guest"):
	print(f"Hello, {name}!")

greet()             # Uses default value
greet("Suresh")     # Uses provided value


def describe(name, age):
	print(f"{name} is {age} years old.")

describe(age=25, name="Aryaav")  # Keyword arguments
