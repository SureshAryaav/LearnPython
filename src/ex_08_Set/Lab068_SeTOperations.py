a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))        # {1, 2, 3, 4, 5, 6}
print(a.intersection(b)) # {3, 4}
print(a.difference(b))   # {1, 2}
print(a.add(7))
print(a)#Adds element x to the set
print(a.remove(3)) #Removes x; error if not found
print(a.discard(3)) #Removes x; no error if not found
print(a.pop()) #Removes and returns an arbitrary element from the set
print(a)
print(b)
print(a.issubset(b)) #Returns True if every element in set is in other
print(a.issuperset(b)) #Returns True if every element in other is in set
print(a.clear()) #Removes all elements from set

