my_dict = {"name": "sandhya", "branch": "ece", "cource": "python"}

# Shallow copy
copied = my_dict.copy()
print(f"Returns a shallow copy: {copied}")

# Get a value using get()
print("Value for key 'name':", my_dict.get("name"))

# List of keys and values
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))

# Pop a key
value = my_dict.pop("name")
print("Popped value for 'name':", value)

# Pop last item
pair = my_dict.popitem()
print("Popped pair:", pair)

# Update dictionary
my_dict.update({"b": 3, "id": 4})
print("After update:", my_dict)

# Set default (won't overwrite existing 'b')
my_dict.setdefault("b", 9)
print("After setdefault:", my_dict)

my_dict = {"name": "sandhya", "branch": "ece", "cource": "python"}

# Shallow copy
copied = my_dict.copy()
print(f"Returns a shallow copy: {copied}")

# Get a value using get()
print("Value for key 'name':", my_dict.get("name"))

# List of keys and values
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))

# Pop a key
value = my_dict.pop("name")
print("Popped value for 'name':", value)

# Pop last item
pair = my_dict.popitem()
print("Popped pair:", pair)

# Update dictionary
my_dict.update({"b": 3, "id": 4})
print("After update:", my_dict)

# Set default (won't overwrite existing 'b')
my_dict.setdefault("b", 9)
print("After setdefault:", my_dict)