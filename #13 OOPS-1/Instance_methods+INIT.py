
class Student:

	passingPercentage = 40

	def __init__(self,name,age,percentage):
		self.name = name
		self.age = age
		self.percentage = percentage

	def studentDetails(self):
		print("Name = ", self.name)
		print("Age =" , self.age)
		print("Percentage = ", self.percentage)
		pass

	def isPassed(self):
		if self.percentage > Student.passingPercentage:
			print("Student is passed")
		else:
			print("Student is not passed")

	@staticmethod
	def welcomeToSchool():
		print("Hey! Welcome To School")

s1 = Student("Parikh", 20, 88)
s2 = Student("Paruukh", 22, 32)
s3 = Student("Pari", 21, 98)


Student.studentDetails(s1)
Student.isPassed(s1)

Student.studentDetails(s2)
Student.isPassed(s2)

Student.studentDetails(s3)
Student.isPassed(s3)




# OR



# s1.isPassed()
# s2 = Student("Varun",26,90)
# s1.studentDetails()
# s2.studentDetails()
# s1.studentDetails()
# Student.studentDetails(s1)
# s1.isPassed()
# s1.welcomeToSchool()


#class_name.function(object_name)