# #method overridding
class NormalUser:
    def playvideo(self,name):
        print(f"\n {name} is playing video with:\n1.Normal Quality\n2.Ads run\n3.No background play\n4.Limited videos download\n5.Music with ads")
    def likes(self):
        pass
    def comments(self):
        pass
    def share(self):
        pass
    def description(self):
        pass
    def subscribe(self):
        pass
class PremiumUser(NormalUser):
    def playvideo(self,name):
        print(f"\n {name} is playing video with:\n1.High Quality\n2.Ads Free\n3.background play\n4.videos download\n5.Music")
sandhya=NormalUser()
Bhavani=PremiumUser()

sandhya.playvideo("sandhya")
Bhavani.playvideo("Bhavani")
#------------------------
class NormalUser:
    def playvideo(self,name):
        print(f"\n {name} is playing video with:\n1.Normal Quality\n2.Ads run\n3.No background play\n4.Limited videos download\n5.Music with ads")
class PremiumUser(NormalUser):
    def playvideo(self,name):
        print(f"\n {name} is playing video with:\n1.High Quality\n2.Ads Free\n3.background play\n4.videos download\n5.Music")
        
sandhya=NormalUser()
Bhavani=PremiumUser()

#------------------------
#operator overloaded
class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __lt__(self,other):
        return self.n<other.n
    def __gt__(self,other):
        return self.n>other.n
    def __str__(self):
        return self.n

number1=number(10)
number2=number(20)
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1>number2)
print(number1<number2)

