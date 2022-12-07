import abc
import math
# I basically followed exactly what you did in class for the polygon and square classes and just did that for the other classes as well
class Polygon:
# adding the abstract method might be useless how I did it here but I want to practice with it
    @abc.abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class Square(Polygon): 
#this is how you did it in class
    def __init__(self, side_length):

        self._side = side_length 
    
    def area (self):
        return self._side*self._side

    def perimeter(self):
        return 4*self._side

class Rectangle(Polygon):
    def __init__(self, width, height):
    
        self._width = width
        self._height = height

    def area (self):
        return self._width * self._height

    def perimeter(self):
        return 2*(self._width + self._height)

class RightTriangle(Polygon):

    def __init__(self, leg1, leg2):
        
        self._leg1 = leg1
        self._leg2 = leg2

    def area (self):

        return (self._leg1 * self._leg2)/ 2

    def perimeter(self):
        #the square root of the legs added to the power of 2
        x = math.sqrt((self._leg1 ** 2) + (self._leg1 ** 2))
        return self._leg1 + self._leg2 + x 

if __name__ == '__main__':
    tri = RightTriangle(leg1 = 2, leg2 = 2)
    print(tri.perimeter())
    print(tri.area())
