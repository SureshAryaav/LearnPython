list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "cherry", "date"]

common = []

for item in list1:
	if item in list2:
		common.append(item)

print("Common items:", common)
