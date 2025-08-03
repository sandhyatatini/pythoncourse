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
