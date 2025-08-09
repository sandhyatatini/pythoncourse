
def celsius_to_fahrenheit():
    print("🧠 Program: Convert Celsius to Fahrenheit\n")
    print("📄 Code:\n\"\"\"\ndef c_to_f(c):\n    return (c * 9/5) + 32\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("c_to_f(0) ➝ 32.0")
    print("c_to_f(100) ➝ 212.0")
    print("\n📝 Explanation:")
    print("This converts Celsius to Fahrenheit using the formula: F = (C × 9/5) + 32.\n")

def swap_two_numbers():
    print("🧠 Program: Swap Two Numbers\n")
    print("📄 Code:\n\"\"\"\ndef swap(a, b):\n    a, b = b, a\n    return a, b\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("swap(10, 20) ➝ (20, 10)")
    print("swap(-5, 3) ➝ (3, -5)")
    print("\n📝 Explanation:")
    print("This uses Python’s tuple unpacking to swap values without using a third variable.\n")


def area_of_circle():
    print("🧠 Program: Calculate Area of a Circle\n")
    print("📄 Code:\n\"\"\"\ndef area_circle(r):\n    return 3.14 * r * r\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("area_circle(7) ➝ 153.86")
    print("area_circle(3) ➝ 28.26")
    print("\n📝 Explanation:")
    print("This calculates the area of a circle using the formula πr², with π = 3.14.\n")


def check_century_year():
    print("🧠 Program: Check Century Year\n")
    print("📄 Code:\n\"\"\"\ndef is_century(year):\n    return year % 100 == 0\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("is_century(2000) ➝ True")
    print("is_century(2023) ➝ False")
    print("\n📝 Explanation:")
    print("A year is a century year if it's divisible by 100.\n")


def sum_even_numbers():
    print("🧠 Program: Sum of Even Numbers in a Range\n")
    print("📄 Code:\n\"\"\"\ndef sum_even(start, end):\n    return sum(i for i in range(start, end+1) if i % 2 == 0)\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("sum_even(1, 10) ➝ 30")
    print("sum_even(4, 8) ➝ 18")
    print("\n📝 Explanation:")
    print("This adds all even numbers between the given start and end using a loop.\n")


def is_power_of_two():
    print("🧠 Program: Check if a Number is a Power of Two\n")
    print("📄 Code:\n\"\"\"\ndef is_power_two(n):\n    return n > 0 and (n & (n - 1)) == 0\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("is_power_two(8) ➝ True")
    print("is_power_two(12) ➝ False")
    print("\n📝 Explanation:")
    print("A number is a power of 2 if it has only one bit set in binary.\n")


def sum_of_digits():
    print("🧠 Program: Sum of Digits in a Number\n")
    print("📄 Code:\n\"\"\"\ndef digit_sum(n):\n    return sum(int(d) for d in str(n))\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("digit_sum(123) ➝ 6")
    print("digit_sum(409) ➝ 13")
    print("\n📝 Explanation:")
    print("The number is converted to a string and each digit is summed after converting back to int.\n")


def count_upper_lower():
    print("🧠 Program: Count Uppercase and Lowercase Letters\n")
    print("📄 Code:\n\"\"\"\ndef count_cases(text):\n    upper = sum(1 for c in text if c.isupper())\n    lower = sum(1 for c in text if c.islower())\n    return upper, lower\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("count_cases('Hello') ➝ (1, 4)")
    print("count_cases('Hi THERE') ➝ (5, 2)")
    print("\n📝 Explanation:")
    print("The program counts uppercase and lowercase letters using `.isupper()` and `.islower()`.\n")


def capitalize_first_letters():
    print("🧠 Program: Capitalize First Letter of Each Word\n")
    print("📄 Code:\n\"\"\"\ndef capitalize_words(sentence):\n    return sentence.title()\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("capitalize_words('hello world') ➝ 'Hello World'")
    print("capitalize_words('python is fun') ➝ 'Python Is Fun'")
    print("\n📝 Explanation:")
    print("The `.title()` method capitalizes the first letter of each word in a sentence.\n")


def convert_days():
    print("🧠 Program: Convert Days to Years, Weeks, and Days\n")
    print("📄 Code:\n\"\"\"\ndef convert_days(days):\n    years = days // 365\n    weeks = (days % 365) // 7\n    rem = (days % 365) % 7\n    return years, weeks, rem\n\"\"\"")
    print("\n🧪 Test Cases:")
    print("convert_days(800) ➝ (2, 10, 5)")
    print("convert_days(365) ➝ (1, 0, 0)")
    print("\n📝 Explanation:")
    print("365 days = 1 year, 7 days = 1 week. We use floor division and modulo to break it down.\n")
