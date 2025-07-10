for i in range(1,11):
    print(i)
else:
    print("end of number")
#--------------------
for i in range(1,20,2):
    if i==17:
        break
    print(i)
#---------------------
for i in range(2,20,2):
    if i==18:
        break
    print(i)
for i in range(1,100,5):
    if i==11:
        continue
    print(i)
#-----------------
bullets=10
while bullets>0:
    print("shoot()")
    bullets-=1
#------------------
bullets=10
while bullets>0:
    if bullets==5:
        print("dead")
        break
    print("shoot()")
    bullets-=1
#-----------------
bullets=10
while bullets>0:
    print("shoot()")
    bullets-=1
#------------------
bullets=10
while bullets>0:
    if bullets==5:
        print("dead")
        break
    print("shoot()")
    bullets-=1
#-----------------
l=['smartphone','laptop','airpods','shoes']
for i in l:
    if i=='laptop':
        break
    print(i.center(20,'_'))
else:
    print("end of the items")
#-----------------------
l=['smartphone','laptop','airpods','shoes']
for i in l:
    if i=='laptop':
        continue
    print(i.center(20,'_'))
else:
    print("end of the items")
#---------------------
l=['smartphone','laptop','airpods','shoes']
for i in l:
    print(i.center(20,'_'))
else:
    print("end of the items")
#------------------------
email,pwd="sandhyatatini58@gmail.com","Sandhya@44"
max_attempt=5
cur_attempt=1
while cur_attempt<=max_attempt:
    e=input("enter the email: ")
    p=input("enter the pwd: ")
    if e==email and p==pwd:
        print("login sucessfull")
        break
    else:
        print("invalid mail")
    cur_attempt+=1
else:
    print("max attempts are done.try after 5 mins")
