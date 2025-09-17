n=int(input("enter the number: "))
if n>=0:
    print("Positive number")
else:
    print("Negative number")
#----------------------------
n=int(input("enter the number: "))
if n%2==0:
    print("Even number")
else:
    print("odd number")
#------------------------------
n=int(input("enter the number: "))
if n%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
#-------------------------------
n=int(input("enter the number: "))
if n%3==0 and n%7==0:
    print("Divisible by both 3 and 7")
else:
    print("Not Divisible by both 3 and 7")
#--------------------------------------
n=int(input("enter the year: "))
if n%4==0 and n%100!=0:
    print("Leap year")
else:
    print("not leap year")
#---------------------------------------
n=int(input("Enter the marks: "))
if n>=35:
    print("Pass")
else:
    print("fail")
#----------------------------------------
n=int(input("enter the digits number: "))
if 100<=n<=999:
    print("3-digit number")
else:
    print("non 3-digit number")
#------------------------------------------
n=input("enter the letter: ")
v='aeiouAEIOU'
if n in v:
    print("Vowel")
else:
    print("NOT vowel")
#-------------------------------------------
n=int(input("enter the number: "))
b=int(input("Enter the number: "))
if n>b:
    print("n is greater")
else:
    print("b is greater")
#------------------------------------------
n=int(input("enter the number: "))
b=int(input("Enter the number: "))
if n<b:
    print("n is smaller")
else:
    print("b is smaller")
#-----------------------------------------
n=int(input("enter the number: "))
if n==0:
    print("Number is Zero")
else:
    print("non zero")
#-----------------------------------------
n=int(input("Enter the number: "))
if n%10==0:
    print("Multiple of n")
else:
    print("not multiple of 10")
#------------------------------------------
n=int(input("enter the number: "))
if n>=18:
    print("Eligible to vote")
else:
    print("not eligible to vote")
#-------------------------------------------
n=int(input("enter the range of 100: "))
if 1<=n<=100:
    print("In range")
else:
    print("out of range")
#--------------------------------------------
a,b=input("enter the square: ").split(',')
a=int(a)
b=int(b)
if a==b**2:
    print(f"{a} is square of {b}")
else:
    print(f"{a} is not square of {b}")
#---------------------------------------------
a,b=input('enter the string: ').split(',')
if a==b:
    print("Strings are equal")
else:
    print("Strings are not equal")
#---------------------------------------------
n=int(input("Enter the number: "))
if n%2==0:
    print("NOT prime")
else:
    print("Prime")
#----------------------------------------------
n=int(input("enter the number: "))
if n>0:
    if n%2==0:
        print("Positive and even number")
    else:
        print("positive and odd number")
else:
    print("Not a positive number")
#----------------------------------------------
n=input("enter the letter: ")
if n.isupper():
    print("Uppercase letter")
else:
    print("not uppercase letter")
#-----------------------------------------------
n=int(input("enter the number: "))
if n>30:
    print("IT'S hot")
else:
    print("not hot")
#---------------------------------------------
n=int(input("enter the number: "))
if n%2==0 and 1<=n<=9999:
    print("4-digit even number")
else:
    print("4-digit not even number")
#-------------------------------------
n=input("enter the letter: ").lower()
if n not in ['a','e','i','o','u']:
    print("Consonant")
else:
    print("Vowel")
#------------------------------------
n=int(input("enter the number: "))
if n%2==0 and n%3==0:
    print("Divisible by both 2 and 3")
elif n%2==0:
    print("Divisible by 2 only")
elif n%3==0:
    print("Divisible by 3 only")
else:
    print("not Divisible by 2 or 3")
#------------------------------------
n=int(input("enter the number: "))
if n<0 and n%2!=0:
    print("Negative and odd number")
else:
    print("not a negative odd number")
#--------------------------------------
n=input("enter the word: ")
if n and n[0].lower() in ['a','e','i','o','u']:
    print("Starts with a vowel")
else:
    print("Does not start with a vowel")
#---------------------------------------
a,b,c=map(int,input("enter the number: ").split(','))
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("invalid triangle")
#---------------------------------------
n=int(input("enter the year: "))
if n%400==0:
    print("Century leap year")
elif n%100==0:
    print("Century year but not a leap year")
else:
    print("not a century year")
#------------------------------------------
ch=input("enter the character digit: ")
if ch.isdigit():
    print("Digit")
else:
    print("Not Digit")
#------------------------------------------
n=input("enter the number: ")
a=int(n[::-1])
d=int(n)
if d==a:
    print("Palindrome number")
else:
    print("Not Palindrome number")
#------------------------------------------
n,b=input("enter the string: ").split(',')
a=len(n)
c=len(b)
if a>=c:
    print("first string is longer")
else:
    print("second string is longer")
#-------------------------------------------
n=int(input("inter the number: "))
if 50<=n<=100 and n%5==0:
    print("In range and divisible by 5")
else:
    print("Not in range")
#-------------------------------------------
n=input("enter the pasword: ")
if n>=8:
    print("Strong password")
else:
    print("Weak password")
#--------------------------------------------
password = input("Enter the password: ")

if len(password) < 8:
    print("Weak password (too short)")
elif not any(ch.isupper() for ch in password):
    print("Weak password (no uppercase letter)")
elif not any(ch.islower() for ch in password):
    print("Weak password (no lowercase letter)")
elif not any(ch.isdigit() for ch in password):
    print("Weak password (no number)")
elif not any(ch in "@#$%&*!?" for ch in password):
    print("Weak password (no special character)")
else:
    print("Strong password")
#-----------------------------------------------
import string

password = input("Enter the password: ")

# Conditions
has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in string.punctuation for ch in password)

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong password")
else:
    print("Weak password")
#----------------------------------------------------
n,b=input("enter the number: ").split(',')
d=int(n)+int(b)

if d%2==0:
    print("sum is even")
else:
    print("sum is odd")
#----------------------------------------------------
n=input("enter the special character: ")
if n in "@#$%&*!?":
    print("Special character")
else:
    print("No special character")
#------------------------------------------
temp = int(input("Enter the temperature in °C: "))

if temp < 15:
    print("Cold")
elif 15 <= temp <= 30:
    print("Moderate")
else:
    print("Hot")
#-------------------------------------------
import math
n=int(input("Enter the square: "))
if int(math.sqrt(n))**2==n:
    print("Prefect square")
else:
    print("not Prefect square")
#----------------------------------------
a,b=map(int,input("enter the ages: ").split(','))
if a>b:
    print("first person is older")
else:
    print("second person is older")
#----------------------------------------
n=int(input("enter the angle: "))
if n<90:
    print("Acute angle")
elif n==90:
    print("Right angle")
elif n>90 and n<180:
    print("Obtuse angle")
else:
    print("Invalid angle")