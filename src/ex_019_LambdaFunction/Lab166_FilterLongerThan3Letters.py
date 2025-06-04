words = ["sun", "sky", "blue", "up", "hello"]
short_words = list(filter(lambda word: len(word) <= 3, words))
print(short_words)  # Output: ['sun', 'sky', 'up']
