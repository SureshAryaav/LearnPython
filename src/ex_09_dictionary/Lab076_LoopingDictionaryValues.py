person = {
	"name": "Alice",
	"age": 30,
	"city": "New York"
}

for key in person:
	print(key, ":", person[key])


for key, value in person.items():
	print(f"{key} => {value}")
