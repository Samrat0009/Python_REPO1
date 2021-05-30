#this function will show error because when s1.print_details is called it goes directly to s1.print_details.
#here since the (self.age = 60) under store_detail is not called s1.age/self.age is not defined.
# so print(self.age)/print(s1.age) will show error
class Student:
    name = "parikh"
    def store_details(self):
        self.age = 60
    def print_details(self):
        print(self.age)
s = Student()
s.store_details()
s1 = Student()
s1.print_details()

#WHEREAS

#here the function store_details first assigns s1.age=60
#then fn print_details is called , i.e. print(s1.age) will not show error

class Student:
    name = "parikh"
    def store_details(self):
        self.age = 60
    def print_details(self):
        print(self.age)
s = Student()
s.store_details()
s1 = Student()
s1.store_details()
s1.print_details()