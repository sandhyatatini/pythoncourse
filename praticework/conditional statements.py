data={
    'sandhyatatini58@gmail.com':'Sandhya@44',
    '21jr1a04e4@gmail.com':'Sandhya@44',
    'sandhyatatini@gmail.com':'9493945718',
}
email,pwd=input("enter the email and password: ") .split()
if data.get(email)==pwd:
    print("login successfully")
else:
    print("invalid login")
'''enter the email and password: sandhyatatini@gmail.com 9493945718
login successfully'''
'''enter the email and password: jhiyuhou 7870
invalid login'''
items=['coffee','icecream','cake','idly']
stocks=[20,40,30,20,0]
data=input("enter the item: ")
if data in items:
    ind=items.index(data)
    if stocks[ind]>0:
        print("availbel",stocks[ind])
    else:
        print("out of stcok.please try again",stocks[ind])
else:
    print("not avaliable")
