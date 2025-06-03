names = ["John", "Alex", "Priya", "Bob", "Suresh"]
long_names = list(filter(lambda name: len(name) > 4, names))
print(long_names)  # Output: ['Priya', 'Suresh']
