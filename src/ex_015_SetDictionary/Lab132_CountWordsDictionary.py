sentence = "this is a test this is only a test"
words = sentence.split()

word_count = {}
for word in words:
	word_count[word] = word_count.get(word, 0) + 1

print(word_count)
