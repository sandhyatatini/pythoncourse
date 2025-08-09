import my_programs
def show_menu():
    print("************FUNCTION MENU************")
    print("1.Convert temperature from Celsius to Fahrenheit")
    print("2.Swap two numbers without using a third variable")
    print("3.Calculate the area of a circle")
    print("4.Check if a year is a century year")
    print("5.Find sum of all even numbers in a given range")
    print("6.Check if a number is a power of two")
    print("7.Find sum of digits in a number")
    print("8.Count uppercase and lowercase letters in a string")
    print("9.Capitalize the first letter of each word in a sentence")
    print("10.Convert days to years, weeks, and days")
    print("0.Exit")
    print("*************************************")
while True:
    show_menu()
    choice=input("Enter your choice: ")
    if choice=="1":
        my_programs.celsius_to_fahrenheit()
    elif choice=="2":
        my_programs.swap_two_numbers()
    elif choice=="3":
        my_programs.area_of_circle()
    elif choice=="4":
        my_programs.check_century_year()
    elif choice=="5":
        my_programs.sum_even_numbers()
    elif choice=="6":
        my_programs.is_power_of_two()
    elif choice=="7":
        my_programs.sum_of_digits()
    elif choice=="8":
        my_programs.count_upper_lower()
    elif choice=="9":
        my_programs.capitalize_first_letters()
    elif choice=="10":
        my_programs.convert_days()
    elif choice=="0":
        print("Exiting programs.")
        break
    else:
        print("Invalid choice. please try again.\n")
