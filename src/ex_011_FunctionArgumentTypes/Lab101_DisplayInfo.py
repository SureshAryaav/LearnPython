def display_info(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

display_info(name="Suresh", age=27, language="Python")
