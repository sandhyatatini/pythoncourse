# Input from user
user_input = input("Enter fruits separated by commas (e.g., apple,banana,cherry): ")
fruits = user_input.split(",")  # Convert to list

print("Original list:", fruits)

# Append a fruit
new_fruit = input("Enter a fruit to append: ")
fruits.append(new_fruit)
print("After append:", fruits)

# Insert a fruit at a specific index
insert_fruit = input("Enter a fruit to insert: ")
index_to_insert = int(input("Enter index to insert at (e.g., 2): "))
fruits.insert(index_to_insert, insert_fruit)
print("After insert:", fruits)

# Sort the list
fruits.sort()
print("After sort:", fruits)

# Extend the list with numbers
fruits.extend([3, 4, 3])
print("After extend:", fruits)

# Pop an element at a specific index
pop_index = int(input("Enter index to pop (e.g., 3): "))
fruits.pop(pop_index)
print("After pop:", fruits)

# Remove first occurrence of 3
fruits.remove(3)
print("After remove(3):", fruits)

# Count how many times 'banana' occurs
count_banana = fruits.count("banana")
print("Banana count:", count_banana)

# Clear the list
fruits.clear()
print("After clear:", fruits)