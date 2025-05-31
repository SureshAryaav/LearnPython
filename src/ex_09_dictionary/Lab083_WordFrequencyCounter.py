sentence = input("Enter a sentence: ")
words = sentence.split()

frequency = {}

for word in words:
	word = word.lower()
	frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequencies:")
for word, count in frequency.items():
	print(f"{word}: {count}")
