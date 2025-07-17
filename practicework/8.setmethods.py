# Input sets from user
s1_input = input("Enter elements for set s1  (e.g., 1,2,3): ")
s2_input = input("Enter elements for set s2  (e.g., 3,4,5): ")

s1 = set(map(int, s1_input.split(',')))
s2 = set(map(int, s2_input.split(',')))

print("Original s1:", s1)

# Add an element
s1.add(10)
print("After add(10):", s1)

# Update with multiple elements
s1.update([20, 30])
print("After update:", s1)

# Discard an element
s1.discard(2)
print("After discard(2):", s1)

# Set operations
print("Union:", s1.union(s2))
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Symmetric Difference:", s1 ^ s2)

# Subset check
print("Is {1, 3} a subset of s1?:", {1, 3}.issubset(s1))

# Disjoint check
print("Is s1 disjoint from s2?:", s1.isdisjoint(s2))
