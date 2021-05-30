class fraction:
    def __init__(self,num = 0,den = 1):         # init can be given default values like this !!
        if den ==0:
            den = 1
        self.num = num
        self.den = den

    def print(self):
        if self.num == 0:
            print(0)
        elif self.num == 1:
            print(self.num)
        else:
            print(self.num,'/',self.den)

    def simplify(self):       # basically greatest common factor
        if self.num == 0:
            self.den = 1
            return
        current = min(self.num,self.den)
        while current >1:
            if self.num%current==0 and self.den%current==0:
                break
            current -=1
        self.num = self.num//current
        self.den = self.den//current


f = fraction(2,3)
f1 = fraction(10,5)
f2 = fraction()

f.print()              # now this is possible
f1.print()
f2.print()

f.simplify()
f1.simplify()
f2.simplify()

f.print()              # values after simplify
f1.print()
f2.print()