

class Vehicle:                                              #super/parent/base class!!!!

    def __init__(self,color,maxSpeed):
        self.color = color
        self.maxSpeed = maxSpeed

class Car(Vehicle):                                         #derived/child class!!!!!

    def __init__(self,color,maxSpeed,numGears,isConvertible):

        super().__init__(color,maxSpeed)         #this tells python to take color and max speed from vehicle(superclass)!!!
        self.numGears = numGears
        self.isConvertible = isConvertible

    def printCar(self):
        print("Color :" ,self.color)
        print("MaxSpeed :",self.maxSpeed)
        print("NumGears :",self.numGears)
        print("IsConvertible :", self.isConvertible)


c = Car("red",15,3,False)
c.printCar()







#EXAMPLE



class Vehicle:
    def __init__(self,color):
        self.color = color
class Car(Vehicle):
    def __init__(self,color,numGears):
        super().__init__(color)
        self.numGears = numGears
c= Car("black",5)
print(c.color)

