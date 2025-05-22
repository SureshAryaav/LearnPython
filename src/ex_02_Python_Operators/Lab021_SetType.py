#set – Unordered, unique items

colors = {"red", "green", "blue"}

print(colors)
print(type(colors))

print("red" in colors)
print("yellow" in colors)
print("yellow" not in colors)

print(len(colors))
print(colors)

#frozenset – Immutable version of a set
frozen_colors = frozenset(["red", "green", "blue"])
print(frozen_colors)
print(type(frozen_colors))
print(len(frozen_colors))

