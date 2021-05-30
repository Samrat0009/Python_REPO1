# python gives us the ability to overload almost all operators : which mean adjust them in ways they'd be useful to us.

# EASY WAY !!!!


class Point:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def __add__(self, other):         # this is the way to overload the "add" operator to 2D, 3D !!!
        x = self.__x + other.__x              #Synatx : __operator__
        y = self.__y + other.__y
        p3 = Point(x,y)
        return p3

    def __str__(self):

        return "This point is at (" + str(self.__x) + "," + str(self.__y) + ")"


p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 + p2
print(p3)


# HARD WAY !!!!



import math
class Point:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def __add__(self,other_point):
        return Point(self.__x + other_point.__x,self.__y + other_point.__y)                ######  Direct method

    def __str__(self):

        return "This point is at (" + str(self.__x) + "," + str(self.__y) + ")"

    def __lt__(self,other_point):
        return math.sqrt(self.__x**2 + self.__y**2) < math.sqrt(other_point.__x**2 + other_point.__y**2)


p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 + p2
print(p3)
print(p2<p1)
