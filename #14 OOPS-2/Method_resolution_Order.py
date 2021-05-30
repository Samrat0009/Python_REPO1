
class Mother:

    def __init__(self):
        self.name = "Manju"

    def print(self):

        print("Print Of Mother called")

class Father:

    def __init__(self):
        self.name = "Ajay"

    def print(self):

        print("Print Of Father called")

class Child(Mother,Father):

    def __init__(self):
        super().__init__()

    def print(self):
        print("Name of child is", self.name)

c = Child()
c.print()
print(Child.mro())              ##This shows in which order an attribute/class/object is accessed in multiple inheritance!!!

#EXAMPLE


class A:

    def __init__(self):
        print("init of a")
class B:
    def __init__(self):
        print("init of b")

class C(B,A):
    def __init__(self):
        super().__init__()

c = C.mro()