# Open in read mode
file = open("sample.txt", "r")

# Read entire content
content = file.read()
print(content)
print(file.readlines())

# Close the file
file.close()
