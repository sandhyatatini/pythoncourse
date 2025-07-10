# Input from user
s = input("Enter the first string (e.g., 'hello world '): ")
b = input("Enter the second string (e.g., 'python is awesome'): ")

# Split second string into a list for join example
c = b.split()  # ['python', 'is', 'awesome']

# String operations
print("Slice s[1:3]:", s[1:3])
print("Slice s[-3:-1]:", s[-3:-1])
print("Join c:", " ".join(c))
print("Concatenate s + b:", s + b)
print("Lowercase:", s.lower())
print("Uppercase:", s.upper())
print("Capitalize:", s.capitalize())
print("Title Case:", s.title())
print("Strip whitespace:", s.strip())
print("Right Strip:", s.rstrip())
print("Replace 'o' with 'e':", s.replace("o", "e"))
print("Find 'e':", s.find("e"))
print("Count 'o':", s.count("o"))
print("Starts with 'he':", s.startswith("he"))
print("Ends with 'ld':", s.endswith("ld"))
print("Split string:", s.split())
print("Join example:", " ".join(["hello", "world"]))
print("Is digit:", s.isdigit())
print("Is alpha:", s.isalpha())
print("Is alphanumeric:", s.isalnum())