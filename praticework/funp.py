def square(n):
    return n**2
print(square(4))
def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(even_odd(4))
def fact_num(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(fact_num(5))
def is_palindrome(s):
    return s==s[::-1]
s=input()
if is_palindrome(s):
    print("is palindrome")
else:
    print("not palindrome")
def sum_digits(n):
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum
print(sum_digits(30))
def max_num(a,b):
    return max(a,b)
print(max_num(10,9))
def c_to_f(c):
    return (c*9/5)+32
print(c_to_f(50))
def v_count(s):
    count=0
    v="aeiouAEIOU"
    for ch in s:
        if ch in v:
            count+=1
    return count
print(v_count("chandhueio"))
def m_table(n):
    t=[]
    for i in range(1,n+1):
        t.append(i*n)
    return t
print(m_table(10))
def reverse_s(s):
    return s[::-1]
print(reverse_s("sandhya"))
def fib_seq(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
print(fib_seq(10))
def is_armstrong(n):
    t=0
    num=n
    s=len(str(n))
    while n>0:
        digit=n%10
        t+=digit**n
        n=n//10
    return t==num
print(is_armstrong(153))