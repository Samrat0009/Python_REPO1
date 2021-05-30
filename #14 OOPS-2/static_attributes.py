#we do not need to use self here means it is(not dependent on instance attributes)!!!!

class Student:

	passingPercentage = 40

	def studentDetails(self):
		self.name = "Parikh"
		print("Name = ", self.name)
		self.percentage = 80
		print("Percentage = ", self.percentage)
		pass

	def isPassed(self):
		if self.percentage > Student.passingPercentage:
			print("Student is passed")
		else:
			print("Student is not passed")

	@staticmethod                                                  # | Decorator : tells this function to stay away from the object (stop the by default passing of self)
	def welcomeToSchool():                                         # | ignores self basically!
		print("Hey! Welcome To School")

s1 = Student()
s1.studentDetails()
Student.studentDetails(s1)
s1.isPassed()
s1.welcomeToSchool()

#class_name.function(object_name)