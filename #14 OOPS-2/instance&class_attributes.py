# |instance and class attributes !!!!!!!


class Student:

    passingPercentage = 40
                                                                      # | function(self) is generally passed in instance methods
    def studentDetails(self):                                         # |  def studentDetails(self):
        self.name = "Parikh"                                          # |      self.name = "Parikh"
        print("Name = ", self.name)                                   # |      print.........
        self.percentage = 80                                          # |      percentage = 80
        print("Percentage = ", self.percentage)                       # |      print("percent.....
        pass                                                          # |      pass

    def isPassed(self):                                               #  if we call this ^ function with isPassed  as (percentage > Student.percentage) it will show error,
        if self.percentage > Student.passingPercentage:               # because now percentage =80 is local to its class but self.percentage = 80 is an instance attribute so
                                                                      # it can be called as self.percentage, as long as this function (self) exists!!!
            print("Student is passed")
        else:
            print("Student is not passed")

s1 = Student()
s1.studentDetails()
Student.studentDetails(s1)
s1.isPassed()