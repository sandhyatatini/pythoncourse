from abc import ABC, abstractmethod
class Upload(ABC):
    @abstractmethod
    def compress(Self):
        pass
    def edit(self):
        print("editing the video")
class Image(Upload):
    def compress(self):
        print("Image is compressed to 3mb")
class Reel(Upload):
    def compress(self):
        print("Reel is compressed to 3mb")
r= Reel()
i=  Image()
s= edit()
r.compress()
i.compress()
s.edit()