class fraction:
    def __init__(self,num = 0,den = 1):         # init can be given default values like this !!
        self.num = num
        self.den = den

    def print(self):
        if self.num == 0:
            print(0)
        elif self.num == 1:
            print(self.num)
        else:
            print(self.num,'/',self.den)

f = fraction(2,3)
f1 = fraction(2)
f2 = fraction()

print(f.__dict__)
print(f1.__dict__)
print(f2.__dict__)

f.print()
f1.print()
f2.print()
