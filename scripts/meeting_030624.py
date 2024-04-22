# OOP

# ClASS: blueprint to create objects sharing the same attributes and sharing the same behaviour

# OBJECT: instance of a class with specific values and specific behaviour


# Define a class Vehicle that store the maker, model and year of a vehicle. 
# In addition, define an odometer with 0 miles. Define a method to print the information to the console.

# Add a couple of methods to read the current odometer_reading attribute and to increase it by a given number of miles.

class Vehicle:

    # Class attributes block
    runs_on = 'gas type'
    author = 'Juan Carlos'
    version = '2.0'

    # __new__method (rarely used):
    #   1. Creates the objet
    #   2. Returns the object

    # def __new__(cls, *args, **kwargs):
    #     print('triggering __new__ method')
    #     return super().__new__(cls)

    def __init__(self, maker: str, model: str, year: int, vehicle_type: str=None):
        '''Initializer of Vehicle class'''
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer = 0
        self.vehicle_type = self.runs_on if vehicle_type is None else vehicle_type
        # if vehicle_type is None:
        #     self.vehicle_type = self.runs_on
        # else:
        #     self.vehicle_type = vehicle_type


    def read_odometer(self):
        '''Method to print the odometer'''
        print(f'Miles: {self.odometer}')
        return None


    def add_miles(self, miles: int):
        '''Method to add miles to the car and increase the odometer'''
        self.odometer += miles
        self.new = False
        return None


    def print_information(self):
        '''Method to print the information of the car'''
        print(f'Maker: {self.maker}\n'
              f'Model: {self.model}\n'
              f'Year: {self.year}')
        return None
        

# Create a Point class that inherits from tuple
# Control over object creation (only create a new object if all coordinates are positive e.g.)
# Add the method to calculate the Euclidean distance between two Points

class Point(tuple):

    def __new__(cls, *args, **kwargs):
        x, y = args
        if x < 0 or y < 0:
            raise ValueError('x and y must be positive')
        return super().__new__(cls, (x,y))


    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y


class Configuration:
        # Class attributes for configuration parameters
    database_host = "localhost"
    database_port = 5432
    database_username = "admin"
    database_password = "password123"

    def __init__(self):
        pass


if __name__ == '__main__':

    #point_1 = Point(1,2)

    # print(point_1.x)
    # print(point_1.y)

    # print(isinstance(point_1, tuple))

    # print(Point(3,4)[0])

    # point_2 = Point.__new__(Point, 5, 6)
    # point_2 = Point.__init__(x=-5,y=6)

    # print(point_2.x)
    # print(point_2.y)

    # for method in point_1.__dir__():
    #     print(method)

    # # Python's way
    # red_corolla = Vehicle(maker='Toyota', model='Corolla', year=2024)
    # red_corolla.print_information()

    # # Bad way
    # new_car = object.__new__(Vehicle)
    # new_car.__init__(maker='Toyota', model='Corolla', year=2020)
    # new_car.print_information()


    # red_corolla.read_odometer()

    # red_corolla.add_miles(100)

    # red_corolla.read_odometer()

    # print(id(red_corolla))  # identity
    # print(type(red_corolla))  # Type
    # print(red_corolla.model)  # Values are, more or less, the attributes

    camry = Vehicle(maker="Toyota", model="Camry", year=2020)
    accord = Vehicle(maker="Honda", model="Accord", year=2019)
    
    model_3 = Vehicle(maker="Tesla", model="Model 3", year=2022, vehicle_type='electric')

    # model_3.read_odometer()
    # model_3.add_miles(10)
    # model_3.read_odometer()

    accord.runs_on = 'hydrogen'  # Bad practice
    print(camry.vehicle_type)
    print(model_3.vehicle_type)
    Vehicle.runs_on = 'diesel'
    Vehicle.version = '2.1'
    print(camry.runs_on)
    print(model_3.runs_on)

    f_150 = Vehicle(maker="Ford", model="F-150", year=2021)
    print(f_150.runs_on)
    print(accord.runs_on)

    print(accord.author)

    


    # print('camry', camry.vehicle_type)
    # print('model_3', model_3.vehicle_type)
    # model_3.vehicle_type = 'electric'  # Bad practice
    # print('camry', camry.vehicle_type)
    # print('model_3', model_3.vehicle_type)
    # Vehicle.vehicle_type = 'electric'  # OK, because you affect all classes
    # print('camry', camry.vehicle_type)
    # print('model_3', model_3.vehicle_type)
    # print('f_150', f_150.vehicle_type)
    # Vehicle.vehicle_type = 'compact'
    # print('camry', camry.vehicle_type)
    # print('model_3', model_3.vehicle_type)
    # print('f_150', f_150.vehicle_type)

#    print(model_3.new)

    # print(camry.maker, camry.vehicle_type)
    # print(accord.maker, accord.vehicle_type)
    # print(f_150.maker, f_150.vehicle_type)
    # print(model_3.maker, model_3.vehicle_type)

#    print(Vehicle.maker)

    # print(f'Corolla: {id(red_corolla)}')
    # print(f'Camry: {id(camry)}')

    # print(red_corolla == camry)

    # accord.add_miles(25)
    # model_3.add_miles(100)

    # accord.read_odometer()
    # model_3.read_odometer()
    # f_150.read_odometer()

    list1 = ['a', 'b', 'c']

    list2 = ' '.join(list1)

    print(type(list2))