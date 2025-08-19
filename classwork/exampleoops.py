class Instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,'-')}")
    def uploadPost(self,image):
        self.post.append(image)
class InstagramV1(Instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f'bio uploaded')
    def uploadpost(self,post,music):
        super().uploadPost(post)
        self.music=music
        print(f"{self.music} is added")
sandhya=Instagram("sandhya123")
sandhya.uploadPost("Good morning")
bhavani=InstagramV1("bhavani","degsiner")
bhavani.uploadPost("Good evening")