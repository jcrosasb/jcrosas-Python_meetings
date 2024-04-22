from abc import ABC, abstractmethod
from functools import reduce


class House:

    def __init__(self, num_rooms: int, num_bathroom: int) -> None:
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathroom


class Vehicle(ABC):

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def travel(self):
        pass

    @abstractmethod
    def fuel(self):
        pass

class Car(Vehicle):

    gas = 10
    odometer = 0

    def fuel(self):
        if self.gas > 0:
            print('Car uses fuel')
            self.gas -= 1
            return 1
        else:
            print('Out of gas')
            return 0
        
    def travel(self):
        if self.fuel() > 0:
            print('Car is traveling')
            self.odometer += 1
            return 1
        else:
            print('Car cannot travel')
            return 0

class HybridCar(Car):  # Single inheritance
    
    battery = 5
    efficiency = 0.5

    def fuel(self):
        if self.battery >= 1:
            self.battery -= 1
            if self.battery == 0 and self.efficiency > 0:
                self.efficiency -= 0.01
            return 1
        else:
            energy = super().fuel()
            if energy > 0:
                self.battery += energy * self.efficiency
            return energy


class HybridRV(HybridCar, House):  # Multiple inheritance
    
    #efficiency = 0.2

    def __init__(self, name: str, num_rooms: int) -> None:
        super().__init__(name)
        House.__init__(self, num_rooms, num_bathroom=1)

    # DONT DO THIS
    # def __init__(self, num_rooms, num_bathrooms, name) -> None:
    #     super(House, self ).__init__(num_rooms, num_bathrooms)
    #     HybridCar.__init__(self, name)


class Horse:

    energy = 5
    odometer = 0
    mood = 'happy'

    def travel(self):
        if self.mood != 'happy':
            raise ValueError
        if self.energy > 2:
            print('Horse is moving')
            self.odometer += 1
            self.energy -= 2
            return 2
        else:
            print('Horse is not moving')
            return 0
        

    def __setitem__(self, key, value):
        if key == 'name':
            self.name = value
        

class Wagon:

    carrying_capacity = 10
    odometer = 0
    
    def __init__(self, locomotion: list[Vehicle]) -> None:
        self.locomotion = locomotion

    def travel(self):
        try:
            total_travel = reduce(lambda total_energy,vehicle: total_energy + vehicle.travel(),self.locomotion, 0)
            self.odometer += total_travel
            if total_travel > 0:
                print('Wagon is traveling')
            else:
                print('Wagon is not traveling')
            return total_travel
        except:
            print('Unhappy horses')
            return 0

def drive_vehicle(vehicle: Vehicle): 

    while vehicle.travel():
        print(vehicle.odometer)

horse = Horse()

# CAN BE DONE, BUT DONT DO THIS
#horse.name = 'Spirit'

horse['name'] = 'Spirit'

#horse.mood = 'tired'

horse_2 = Horse()
horse_3 = Horse()

#print(horse_2.name)

car_1 = HybridCar(name='Tesla')
car_2 = HybridCar(name='Rivian')

wagon = Wagon(locomotion=[car_1, car_2])
#drive_vehicle(wagon)

#drive_vehicle(horse)



# car = HybridCar(name='Ford')

# hybrid_RV_1 = HybridRV(name='Tesla', num_rooms=2)

# hybrid_RV_2 = HybridRV(name='Rivian', num_rooms=1)

# drive_vehicle(hybrid_RV_1)

# print(hybrid_RV_2.efficiency)

# HybridRV.efficiency = 0.6

# print(hybrid_RV_1.efficiency)
# print(hybrid_RV_2.efficiency)

# print(HybridRV.mro())  # Method Resolution Order



# print(HybridCar.efficiency)
# print(HybridRV.efficiency)

#hybrid_RV = HybridRV(num_rooms=2, num_bathrooms=1, name='Tesla')

# house = House(num_bathroom=1, num_rooms=2)

# print(house.num_bathrooms)
# print(house.num_rooms)

#print(hybrid_RV.num_bathrooms)

# drive_vehicle(car)
# drive_vehicle(hybrid_RV)

# 

# while car.travel() == 1:
#     print(car.odometer)