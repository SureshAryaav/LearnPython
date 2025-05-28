employee = {
	"id": 101,
	"name": "David",
	"role": "Developer"
}

print("Employee ID:", employee["id"])
print("Name:", employee.get("name"))


#Add/Update dictionary
employee["age"] = 30
print("Age:", employee["age"])
employee["salary"] = 50000  # Add
employee["role"] = "Senior Developer"  # Update
print(employee)

employee.pop("salary")

print("After deletion:", employee)

employee.clear()
print("After clear:", employee)
