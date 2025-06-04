def show_info(**person):
	for key, value in person.items():
		print(f"{key}: {value}")

show_info(name="Alice", age=28, city="New York")
