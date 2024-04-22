# from meeting_030824 import Pizza

# class Lasagna:

#     cost = Pizza.production_cost()


# my_lasagna = Lasagna()

# print(my_lasagna.cost)

class Vehicle:

    def __init__(self, name) -> None:
        self.name = name


    def __getitem__(self, key):
        return self.name[key]


    def __setitem__(self, key, value):
        name_list = list(self.name)
        name_list[key] = value
        self.name = ''.join(name_list)
        return None 

    # def travel(self):
    #     pass


# class Car(Vehicle):

#     def travel(self):
#         print('Traveling by car')


# class ElectricCar(Vehicle):

#     def travel(self):
#         print('Traveling by electric car')


# class Boat:

#     def travel(self):
#         print('Traveling by boat')


#     def get_miles(self):
#         return 10


# class Airplane(Boat):
# #    pass
#     def travel(self):
#         print('Traveling by airplane')


if __name__ == '__main__':

    vehicle = Vehicle('Ford')

    list1 = [1,2,3]


    print(vehicle.name)
    print(list1)

    print(vehicle[2])
    print(list1[2])

    vehicle[0] = 'C'
    list1[0] = 100

    print(vehicle.name)
    print(list1)



    # vehicle = Vehicle()
    # car = Car()
    # electric_car = ElectricCar()
    # boat = Boat()
    # airplane = Airplane()

    # vehicle.travel()
    # car.travel()
    # electric_car.travel()
    # boat.travel()
    # airplane.travel()

    # print(boat.get_miles())


    # print(airplane.get_miles())

    # list1 = [1,2,3]

    # tuple1 = (1,2,3)

    # set1 =  {1,2,3}

    # dict1 = {'a':1, 'b':2, 'c':3}

    # print(isinstance(list1, tuple))

    # print(isinstance(tuple1, list))

    # print(len(list1))
    # print(len(tuple1))


    # for _ in list1:
    #     print('hello')

    # for _ in tuple1:
    #     print('hello')

    # for _ in set1:
    #     print('hello')

    # for _ in dict1:
    #     print('hello')


    # print(list1[1])
    # print(tuple1[1])

    # # Iteration: Datatypes
    # # List:      Yes
    # # Tuple:     Yes
    # # String:    Yes
    # # Dict:      Yes
    # # Sets:      Yes

    # # Indexing: Datatypes
    # # List:     Yes
    # # Tuple:    Yes
    # # String:   Yes
    # # Dict:     No
    # # Sets:     No

    # # Slicing
    # # Lists:   yes
    # # Tuple:   yes
    # # Strings: yes
    # # Dict:    no
    # # Sets:    no

    # # reverse
    # # list:   yes
    # # tuple:  no
    # # strings: yes
    # # dict:   no
    # # sets:   no

    
