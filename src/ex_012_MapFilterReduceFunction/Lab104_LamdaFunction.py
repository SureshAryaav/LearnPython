#A lambda is an anonymous function (no def, no name) used for short-term operations.

# Regular function
def square(x):
	return x * x


# Lambda version
#lambda arguments: expression
square = lambda x: x * x
print(square(5))  # Output: 25

add = lambda a, b: a + b
print(add(2, 3))  # Output: 5

