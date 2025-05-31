fruits = ["apple", "banana", "cherry"]

print(fruits)

fruits[1] = "blueberry"  #['apple', 'blueberry', 'cherry']
print(fruits)

fruits.append("orange")        # Add to the end ['apple', 'blueberry', 'cherry', 'orange']
print(fruits)

fruits.insert(1, "grape")      # Add at index 1 ['apple', 'grape', 'blueberry', 'cherry', 'orange']
print(fruits)

fruits.remove("apple")         # Removes "apple"
print(fruits)
popped = fruits.pop()          # Removes last item and returns it
print(fruits)
del fruits[0]                  # Deletes item at index 0
print(fruits)