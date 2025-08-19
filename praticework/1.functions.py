'''def add(a,b):
    return a+b
a=int(input())
b=int(input())
print(f"The sum of a and b:{add(a,b)}")
#--------------------------------------
def square(c):
    return c**2
c=int(input())
print(square(c))
#--------------------------------------
def Area_of_circle(radius):
    pi=3.14
    return pi*radius*radius
radius=int(input())
print(Area_of_circle(radius))
#--------------------------------------
def greet(name):
    print(f"hello {name}")
name=input()
greet(name)
#--------------------------------------
def Celsius_to_fahrenheit(celsius):
    return celsius*9/5+32
celsius=int(input())
print(Celsius_to_fahrenheit(celsius))
#--------------------------------------
def Multiply(a,b,c):
    return a*b*c
a,b,c=tuple(map(int,input().split()))
print(Multiply(a,b,c))
#-------------------------------------
def Simple_interest(p,r,t):
    return p*r*t/100
p,r,t=tuple(map(float,input().split()))
print(Simple_interest(p,r,t))
#--------------------------------------
def length_of_string(s):
    return len(s)
s=input()
print(length_of_string(s))
#--------------------------------------
def Append_to_list(lst,elements):
     lst.append(elements)
     return lst
lst=list(map(int,input().split()))
elements=int(input())
print(Append_to_list(lst,elements))
#---------------------------------------'''
input_str=input()
numbers=list(map(int,input_str.split()))
doubled_list=[]
for num in numbers:
    doubled=num*2
    doubled_list.append(doubled)
print(doubled_list)
#-------------------------------------
def Double_list(number):
    double_list=[]
    for num in number:
        doubled_list.append(num*2)
    return doubled_list
input_str=input()
number=list(map(int,input_str.split()))
print(Double_list(number))
#---------------------------------------
def remove(l,val):
    while val in l:
        l.remove(val)
    return l

