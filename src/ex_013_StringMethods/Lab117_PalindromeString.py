def is_palindrome(text):
	text = text.lower().replace(" ", "")
	return text == text[::-1]

print(is_palindrome("madam"))      # True
print(is_palindrome("Hello"))      # False
