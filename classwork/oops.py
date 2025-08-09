#encapsulation
class detail:
    def __init__(self,name,email,pwd):
        self.name=name
        self._email=email
        self.__pwd=pwd
    def getpassword(self):
        return self.__pwd
    def setpassword(self,new_password):
        self.__pwd=new_password
sandhya=detail("sandhya","sandhya@gmail","sandhya@123")
print(sandhya.name)
sandhya.name="bhavani"
print(sandhya.name)
print(sandhya._email)
print(sandhya.getpassword())
sandhya.setpassword("bhavani@123")
print(sandhya.getpassword())
#------------------------------
class Bank:
    def __init__(self):
        self.name="xyz"
        self._balance=0
    
    @property
    def norestrictbalance(self):
        return self._balance
    
    @norestrictbalance.setter
    def norestrictbalance(self,amount):
        self._balance+=amount
b=Bank()
print(b.norestrictbalance)
b.norestrictbalance=3000
print(b.norestrictbalance)
print(b.name)
#----------------------------
class Instagram:
    def __init__(self,name,bio,acc_status=False):
        self.name=name
        self._bio=bio
        self.__acc_status=acc_status
    def get_acc_status(self):
        return self.__acc_status
    def set_acc_status(self,status):
        self.__acc_status=status
    @property
    def bio(self):
        return self._bio
    @bio.setter
    def bio(self,new_bio):
        self._bio=new_bio
sandhya=Instagram("sandhya","slient",False)
print(sandhya.name)
print(sandhya.get_acc_status())
sandhya.set_acc_status=True
print(sandhya.get_acc_status)
print(sandhya.bio)
sandhya.bio="habit"
print(sandhya.bio)
    