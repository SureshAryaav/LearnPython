# Step 1: Take input from the user
sentence = input("Enter a sentence: ")

# Step 2: Convert the sentence to title case
title_case_sentence = sentence.title()

# Step 3: Count the number of words
words = sentence.split()
word_count = len(words)

# Output the results
print("\nTitle Case Sentence:")
print(title_case_sentence)

print("\nNumber of Words:")
print(word_count)
