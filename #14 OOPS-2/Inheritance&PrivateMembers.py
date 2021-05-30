

class Vehicle:

	def __init__(self,color,maxSpeed):
		self.color = color
		self.__maxSpeed = maxSpeed                 ## privatise a member by putting "__" before name!

	def getMaxSpeed(self):
		return self.__maxSpeed

	def setMaxSpeed(self,maxSpeed):
		self.__maxSpeed = maxSpeed

class Car(Vehicle):

	def __init__(self,color,maxSpeed,numGears,isConvertible):

		super().__init__(color,maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def printCar(self):
		print("Color :" ,self.color)
		print("MaxSpeed :",self.getMaxSpeed())          # "self.__maxspeed" cannot be accessed outside it's own class, so we use "setmaxspeed" "getmaxspeed"
		print("NumGears :",self.numGears)               # it is the only way to access private members outside thier class !
		print("IsConvertible :", self.isConvertible)


c = Car("red",15,3,False)
c.printCar()