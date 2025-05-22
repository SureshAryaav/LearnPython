name = input("Enter your name: ")

greeting = "Hello"

# String formatting using format() method
print("{}! {}".format(greeting, name))
print("{greet}! {person}".format(greet=greeting, person=name))
print("{0}! This is {1}. Welcome, {1}!".format(greeting, name))

