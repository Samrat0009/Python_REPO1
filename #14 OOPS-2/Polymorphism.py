# Ability to take multiple forms { METHOD OVERIDING }

# order of print in python : 1.=> lowest class 2.=> parent class => .....=> parent's parent's parent's.......class !

class Vehicle:

	def __init__(self,color,maxSpeed):
		self.color = color
		self._maxSpeed = maxSpeed

	@classmethod
	def getMaxSpeed(cls):
		return 15

	def setMaxSpeed(self,maxSpeed):
		self._maxSpeed = maxSpeed

	def print(self):                                                              # when both functions are called print
		print("Color :" ,self.color)
		print("MaxSpeed :",self._maxSpeed)

class Car(Vehicle):

	def __init__(self,color,maxSpeed,numGears,isConvertible):

		super().__init__(color,maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def print(self):                                                              # when both functions are called print


		# Correct : super().print()                  # to print the parent class first we use super().print()

		# Incorrect : self.print()                  # we cannot use this to print parent class first : it will send the function into an infinite loop !
                                                    # because self.print() again would go to the lowest class which is car......and so on....
		print("Color :" ,self.color)
		print("MaxSpeed :",self._maxSpeed)
		print("NumGears :",self.numGears)
		print("IsConvertible :", self.isConvertible)


# c = Car("red",15,3,False)
# c.print()
#print()
v = Vehicle("red",18)
v.print()
print()