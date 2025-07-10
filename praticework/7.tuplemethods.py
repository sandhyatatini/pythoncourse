user_input = input("Enter tuple elements (e.g., 3,7,9,7,8): ")
t = tuple(map(int, user_input.split(",")))

print("Tuple entered:", t)

# Count the number of times 7 appears
print("Count of 7:", t.count(7))

# Find index of first occurrence of 3
print("Index of 3:", t.index(3))

# Slicing
print("Slice t[1:3]:", t[1:3])

# Length of tuple
print("Length of tuple:", len(t))

# Concatenation with another tuple
print("Concatenated tuple:", t + (8, 9))

# Membership check
print("Is 3 in tuple?:", 3 in t)
print("Is 4 not in tuple?:", 4 not in t)