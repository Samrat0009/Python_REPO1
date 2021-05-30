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

    def add(self, otherF):
        newNum = otherF.den*self.num + otherF.num*self.den
        newDen = otherF.den*self.den

        self.num = newNum
        self.den = newDen

        self.simplify()

    def mul(self, otherF):
        newNum = otherF.num*self.num
        newDen = otherF.den*self.den

        self.num = newNum
        self.den = newDen

        self.simplify()


f = fraction(2,3)
f1 = fraction(5,10)
f2 = fraction(1)

f1.add(f2)
f2.add(f)

f1.print()
f2.print()

f = fraction(2,3)
f1 = fraction(8,10)
f2 = fraction(1)

f1.mul(f2)
f2.mul(f)

f1.print()
f2.print()