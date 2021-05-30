class complex:
    def __init__(self,real,image):
        self.real = real
        self.image = image

    def print(self):
        print(self.real,'+ i',end="")
        print(self.image)

    def add(self,otherC):
        newReal = self.real + otherC.real
        newImage = self.image + otherC.image

        self.real = newReal
        self.image = newImage

    def mul(self,otherC):
        newReal = self.real*otherC.real - self.image*otherC.image
        newImage = self.image*otherC.real + otherC.image*self.real

        self.real = newReal
        self.image = newImage


a,b = (int(y) for y in input().split())
c,d = (int(x) for x in input().split())

c1 = complex(a,b)
c2 = complex(c,d)

n = int(input())
if n==1:
    c1.add(c2)
    c1.print()
elif n==2:
    c1.mul(c2)
    c1.print()
