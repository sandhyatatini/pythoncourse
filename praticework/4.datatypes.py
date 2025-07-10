items = int(input("Enter number of items: "))
user_id = int(input("Enter user ID: "))
price = float(input("Enter the price: "))
discount = float(input("Enter the discount (%): "))

# Complex number input (split into real and imaginary parts)
complex_num = complex(input("enter the complex nuumber: "))

# List input
list_input = input("Enter list elements: ")  # e.g., 4,5,6
list_values = list(map(int, list_input.split(',')))

# Tuple input
tuple_input = input("Enter tuple elements: ")  # e.g., 2,4,2
tuple_values = tuple(map(int, tuple_input.split(',')))

# Set input
set_input = input("Enter set elements: ")  # e.g., 23,45,56
set_values = set(map(int, set_input.split(',')))

# Dictionary input
name = input("Enter your name: ")
batch = input("Enter your batch: ")
course = input("Enter your course: ")
d = {"name": name, "batch": batch, "course": course}

# Boolean values
a = False
b = True

# NoneType
c = None

# Printing everything
print(items)
print(user_id)
print(price)
print(discount)
print(complex_num)
print(list_values)
print(tuple_values)
print(set_values)
print(d)
print(a)
print(b)
print(c)
