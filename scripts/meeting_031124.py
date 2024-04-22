# A blueprint of a blueprint is a subclass

from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, name: str) -> None:
        self.name = name


    def travel(self):
        pass


    @abstractmethod
    def fuel(self):
        pass


class Radio:
    pass


class Car(Vehicle):

    radio = Radio()
    odometer = 0
    gas = 100
    
    def fuel(self):
        if self.gas > 0:
            print('Car uses fuel')



class HybridCar(Car):
    pass


class Airplane(Vehicle):
    pass


class Boat(Vehicle):
    pass


car = Car(name='Ford')
car.fuel()

vehicle = Vehicle(name='test1')


# Four pillars of OOP:
#   1. Abstraction
#   2. Encapsulation (python is not great)
#   3. Inheritance
#   4. Polymorphism

# CONCRETE CLASS: one that you can instantiate  