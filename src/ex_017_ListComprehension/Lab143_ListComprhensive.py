squares = [x*x for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]


evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]


labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(labels)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']
