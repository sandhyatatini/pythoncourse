#inheritence
class status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")
class statusV1(status):
    def addCaption(self,text=None):
        self.Caption=text
        print(f'self.caption is added to your status')
class statusV2(status):
    def like(self):
        print(f'You can like status')
sravani=status()
sravani.uploadImage("selfie.png")

hema=statusV1()
hema.uploadImage("Goodmrng.png")
hema.addCaption("Moring Friends")    

vaishnavi=statusV2()
vaishnavi.uploadImage("coffee.png")

  