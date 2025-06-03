my_set = {1, 2, 3, 2, 4}
print(my_set)  # {1, 2, 3, 4}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))         # {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # {3}
print(set1.difference(set2))    # {1, 2}
