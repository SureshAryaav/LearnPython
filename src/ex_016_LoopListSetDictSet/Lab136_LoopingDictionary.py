person = {"name": "Alice", "age": 25}

for key in person:
	print(key, "=>", person[key])


for key, value in person.items():
	print(f"{key} = {value}")

#Only values:
for value in person.values():
	print(value)
