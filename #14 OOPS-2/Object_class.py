# 3 types of obj-class methods functions : __new__  : used to create new objects
#                                        : __init__ : used to initialise the object
#                                        : __str__  : below ! basically customises what the function returns ! (useful info)


#this does not usually give any useful information to us about the class!!

class Circle(object):

	def __init__(self,radius):
		self.__radius = radius

c = Circle(3)
print(c)


#whereas this helps ud write a more useful message for the user to interpret!!


class Circle(object):

	def __init__(self,radius):
		self.__radius = radius

	def __str__(self):
		return "This is a Circle class which takes radius as an argument."

c = Circle(3)
print(c)