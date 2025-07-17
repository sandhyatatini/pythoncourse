#2 3 5 7 11 13 17 19 23 29
fact=0
n=int(input("Enter the num: "))
for i in range(2,(n//2)+1):
    if n%i==0:
        fact+=1
if fact==0:
    print(f"{n} is prime number\nFactors count={fact}")
else:
    print(f"{n} is not prime number\nFactors count={fact}")
     