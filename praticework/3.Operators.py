#1.Arithematic Operation
a=10
b=20
print("Addtion(+):",a+b)#Addtion(+):30
print("subtraction(-):",a-b)#Sub(-):-10
print("multiplication(*):",a*b)#mul(*):200
print("Division(/):",a/b)#div(/):0.5
print("Floor division(//):",a//b)#floor div(//):0
print("modulus(remainder)(%):",a%b)#mod (%):10
print("exponentiation(**):",a**b)#exp(**):100000000000000000000

#2. Comparison Operators
c=10
d=40
print("Equal to(==):",c==d)#Eqa(==):False
print("Not Equal to(!=):",c!=d)#Neqa(!=):True
print("Greater than(>):",c>d)#gre(>):False
print("Less than (<):",c<d)#les(<):True
print("Greater than or Equal to(>=):",c>=d)#greeqa(>=):False
print("less thanor Equal to(<=):",c<=d)#leseqa(<=):True

#3.Assignment Operators
'''var=var(op)(value)
   var(op)=value
   e+=10
   e=e+10'''
e=20
e+=30
print("Add & Assign(+=):",e)#Add & Assign(+=):50
e-=20
print("Subtract & Assign(-=):",e)#Subtract & Assign(+=):30
e*=3
print("multiply & Assign(*=):",e) #multiply & Assign(*=):90
e/=2
print("Divison & Assign(/=):",e)#Division & Assign(/=):45.0
e//=3
print("Floor Divison & Assign(//=):",e)#floor Division & Assign(//=):15.0
e%=2
print("Modulus & Assign(%=):",e)#Modulus & Assign(%=):1.0
e**=2
print("exponentiate & Assign(**=):",e)#exp&assign(**=):1.0

#4.Logical Operator
'''AND Gate Truth Table
 A      B   A and B
True  True   True
True  False  False
False True   False
False False  False'''
#if you give both statment true it gives the true in AND gate operation
#if you give one statment true and another statement false it gives the False in AND gate operation

x=10
y=20
print(x>5 and y<30)#two codition are correct it gives output:True
print(x>15 and y<30)#one codition is correct and another codition is incorrect it give the output:False

'''OR Gate Truth Table
 A      B   A and B
True  True   True
True  False  True
False True   True
False False  False'''
#if you give both statment true it gives the true in OR gate operation
#if you give one statment true and another statement false it gives the Ture in OR gate operation
#OR operatin to give any one statement correct its give true output

x=10
y=20
print(x>5 or y<30)#two codition are correct it gives output:True
print(x>15 or y<30)#one codition is correct and another codition is incorrect it give the output:Ture

'''NOT Gate Truth Table
A      not A
True   False
False  True'''
#its gives correct statement and its give worng statement :true=false
x=10
print(x>5)#False

#5.Membership Operators

names=["sandhya","chandu","bhavani","harisha","hemu"]
print("in result :","sandhya" in names)#in result:True
print("in result :","bhavani" in names)#in result:True
print("not in result :","sandeep" not in names)#in result:True
 
#6.Identity Operator
l=[3,3,4]
b=[3,3,4]
print("l is b:",l==b)#l is b:False
a=b
print("a is b:",a==b)#a is b:True
print("l is b:",l is b)#l is b:False
print("l is not b:",l is not b)#l is not b:True
print("a is not b:",a is not b)#a is not b:False
print("id(l):",id(l))#id(l):4376217600
print("id(b):",id(b))#id(b):4381180288
print("id(a):",id(a))#id(a):4381180288

#7.Bitwise Operators
x=5 #binary:0101
y=3 #binary:0011
print(x&y) #output:1
'''0101 
    0011
    ----
    0001
'''
print(x|y)#output:7
'''0101
   0011
   ----
   0111
   '''
#XOR OPERATION
print(x^y)#output:6
'''0101
    0011
    ----
    0110
    '''
#not operation
print(~x)#output:
'''0101
   ----
   1010
   '''
print(x<<1)#output:10
'''0101
   ----
   1010
  '''
print(x>>1)#output:
'''0101
   ----
'''
       
    
