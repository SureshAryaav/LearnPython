student = {
	"name": "John",
	"age": 21,
	"course": "Python"
}

print(student["name"])   # Output: John
print(student.get("age"))  # Output: 21
print(student.get("course"))  # Output: Python
#✅ Use .get() to safely retrieve values (returns None if key not found)

student["email"] = "john@example.com"  # Add
student["age"] = 22  # Update
del student["course"]  # Delete
