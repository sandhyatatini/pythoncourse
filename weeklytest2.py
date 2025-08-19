#1.automated salary text calculator

salary=float(input())
if salary <= 250000:
    print("No Tax")
elif salary > 250000 and salary <= 500000:
    print(salary*0.05)
elif salary > 500000 and salary <= 1000000:
    print(salary*0.2)
elif salary > 1000000:
    print(salary*0.03)


#2.movie ticket pricing system

n=int(input())
total = 0
for _ in range(n):
    age = int(input())
    if age >= 5 or age <= 18:
        total += 100
    elif age >= 19 and age <= 60:
        total += 150
    elif age>60:
        total += 120
print(total)

#3.electricity bill generator

units = int(input())
bill =0
if units<-100:
    bill+=units*1.5
elif units>100 and units<=200:
    bill+=150+(units-100)*2.5
elif units>200 and units<=500:
    bill+=400+(units-200)*4
else:
    bill+=1600+(units-500)*6
print(bill)

#4.car parking fee calculator

hours=int(input())
fee=0
if hours<=2:
    print(30)
elif hours>2 and hours<24:
    fee=30+(hours-2)*10
elif hours>=24:
    print(200)


#5.product inventory checker

name=input()
quantity=int(input())
if quantity == 0:
    print("Out of Stack")
elif quantity > 0 and quantity < 11:
    print("Low Stock")
elif quantity > 10 and quantity < 51:
    print("In Stock")
elif quantity>50:
    print("Overstocked")

#6.pattern

n=int(input())
for row in range(n):
    for col in range(n):
        if (row+col) % 2 == 0: #print((row+col)%2))
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()

#7.gym subscription billing

while True:
    print("1.monthly-5002.quaterly-13003.yeraly-5000")
    choice = int(input())
    people = int(input())
    if choice==1:
          print(people*500)
    elif choice==2:
        print(people*1300)
    elif choice==3:
        print(people*5000)
    elif choice==0:
        break
    else:
        print("Invalid choice")

#8.Billing bot

total = float(input())
if total<1000:
    print(total)
elif total>999 and total<5000:
    print(total-total*0.05)
elif total>4999 and total<10000:
    print(total-total*0.1)
elif total>=10000:
    print(total-total*0.15)

#9.ATM pin verificaiton with blocking logic

pin=1234
for i in range(3):
    epin=int(input())
    if epin==pin:
        print("Access Granted")
        break
else:
    print("ATM is blocked")


#10.bus booking system

total_seats=int(input())
booked_seats = list(map(int, input().split()))
print(f'Total seats:{total_seats}')
print(f'Booked: {len(booked_seats)}')
print(f'Available: {total_seats-len(booked_seats)}')


    