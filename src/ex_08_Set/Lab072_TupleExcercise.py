# Create a tuple of favorite movies and access the 2nd and 4th item
movies = ("Inception", "Matrix", "Interstellar", "Dune", "Tenet")
print("Second movie:", movies[1])
print("Fourth movie:", movies[3])


# Loop through a tuple and print each element
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
	print(fruit)


# Packing a tuple and unpacking it into variables
person = ("John", 28, "Engineer")

name, age, job = person

print("Name:", name)
print("Age:", age)
print("Job:", job)
