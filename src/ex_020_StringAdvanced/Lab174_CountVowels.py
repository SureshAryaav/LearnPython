def count_vowels(s):
	vowels = "aeiouAEIOU"
	return sum(1 for char in s if char in vowels)

print(count_vowels("Python Programming"))  # Output: 4
