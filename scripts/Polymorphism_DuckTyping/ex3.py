import math
from abc import ABC, abstractmethod

class Shape(ABC):
    '''Abstract class for object Shape'''
    
    @abstractmethod
    def area(self) -> None:
        '''Abstract method to calculate the area of a given shape'''
        pass


class Circle(Shape): 
    '''Class to create a Circle object'''

    def __init__(self, radius:float) -> None:
        self.radius = radius
    

    def area(self) -> float:
        '''Method to calculate the area of a Circle
           Returns:
                * the area, given by pi * self.radius^2'''
        return math.pi * self.radius**2
    

class Rectangle(Shape):
    '''Class to create a Rectangle object'''

    def __init__(self, width:float, height:float) -> None:
        self.width = width
        self.height = height
    

    def area(self) -> float:
        '''Method to calculate the area of a Rectangle
           Returns:
                * the area, given by self.width * self.height'''
        return self.width * self.height


class Triangle(Shape):
    '''Class to create a Triangle object'''
    
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height


    def area(self) -> float:
        '''Method to calculate the area of a Triangle
           Returns:
                * the area, given by self.base * self.height / 2'''
        return self.base * self.height / 2
    

def main():
    '''Function to return the sum of all areas
       Returns:
            * The sum of the area of a Cricle, Rectangle, and Triangle'''

    circle = Circle(radius=5)

    rectangle = Rectangle(width=20, height=10)

    triangle = Triangle(base=8, height=6)

    return round(circle.area() + rectangle.area() + triangle.area(), 2)



if __name__ == '__main__':

    # Use main function to sum all areas
    result = main()
    print(result)

    # circle = Circle(radius=5)
    # print(circle.area())

    # rectangle = Rectangle(width=20, height=10)
    # print(rectangle.area())

    # triangle = Triangle(base=8, height=6)
    # print(triangle.area())

    #print(circle.area() + rectangle.area() + triangle.area())
