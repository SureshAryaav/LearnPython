# Create a set and add new elements, then remove one
colors = {"red", "green", "blue"}
print(colors)

colors.add("yellow")
colors.remove("green")
print(colors)


# Find common and all elements between two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
