# Abstract Classes : python by default does not have abstract classes >
# so we use a **module abc**: abstract base classes

# abstract methods: Declared, but have no implementation!!

from abc import ABC,abstractmethod

class Automobile(ABC):
    def __abs__(self):
        print("auto created")

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self):
        pass

class Car(Automobile):
    def __init__(self,name):
        print("car created")
        self.name = name

    def start(self):                     # with abstract classes you have to initiate these every time!
        pass                             # start,stop,drive have to be implemented to every child class
                                         # here chile class : Car, Bus, etc.
    def stop(self):
        pass

    def drive(self):
        pass

c = Car("honada")

#NOTE : objects of abstract class cannot be created!
#     : implement all the abstract methods in child class!