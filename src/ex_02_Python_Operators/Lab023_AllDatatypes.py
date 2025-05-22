# Numeric Types
int_var = 10
float_var = 3.14
complex_var = 2 + 3j

# String Type
str_var = "Hello, Python!"

# Boolean Type
bool_var = True

# Sequence Types
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
range_var = range(3)

# Mapping Type
dict_var = {"name": "Alice", "age": 25}

# Set Types
set_var = {1, 2, 3}
frozenset_var = frozenset([4, 5, 6])

# None Type
none_var = None

# Print all with their type
print("Integer:", int_var, "| Type:", type(int_var))
print("Float:", float_var, "| Type:", type(float_var))
print("Complex:", complex_var, "| Type:", type(complex_var))

print("String:", str_var, "| Type:", type(str_var))
print("Boolean:", bool_var, "| Type:", type(bool_var))

print("List:", list_var, "| Type:", type(list_var))
print("Tuple:", tuple_var, "| Type:", type(tuple_var))
print("Range:", list(range_var), "| Type:", type(range_var))  # converted to list for display

print("Dictionary:", dict_var, "| Type:", type(dict_var))

print("Set:", set_var, "| Type:", type(set_var))
print("Frozenset:", frozenset_var, "| Type:", type(frozenset_var))

print("None:", none_var, "| Type:", type(none_var))
