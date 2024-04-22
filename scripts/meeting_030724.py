# class Vehicle:

#     # Class attributes block
#     runs_on = 'gas type'
#     author = 'Juan Carlos'
#     version = '2.0'

#     def __new__(cls, *args, **kwargs):
#         maker = kwargs.get('maker')
#         if maker != 'Ford':
#             raise ValueError('I need a Ford car')
#         return super().__new__(cls)

#     def __init__(self, maker: str, model: str, year: int, vehicle_type: str=None):
#         '''Initializer of Vehicle class'''
#         self.maker = maker
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.vehicle_type = self.runs_on if vehicle_type is None else vehicle_type


#     def read_odometer(self):
#         '''Method to print the odometer'''
#         print(f'Miles: {self.odometer}')
#         return None


#     def add_miles(self, miles: int):
#         '''Method to add miles to the car and increase the odometer'''
#         self.odometer += miles
#         self.new = False
#         return None


#     def print_information(self):
#         '''Method to print the information of the car'''
#         print(f'Maker: {self.maker}\n'
#               f'Model: {self.model}\n'
#               f'Year: {self.year}')
#         return None
    

# class Car(Vehicle):

#     def __new__(cls, *args, **kwargs):
#         color = kwargs.get('color')
#         if color == 'white':
#             raise ValueError('I need red car')
#         return super().__new__(cls, *args, **kwargs)

#     def __init__(self, maker: str, model: str, year: int, color: str, vehicle_type: str=None):
#         super().__init__(maker, model, year, vehicle_type)
#         self.color = color
        
    
#     def print_information(self):
#         super().print_information()
#         print(f'Color: {self.color}')

# #red_car = Car(maker='Ford', model='Corolla', year=2024, color='red')
# red_car = Car(maker='Ford', model='Corolla', year=2024, color='red')

# red_car.print_information()

class BasicClass:

    species = 'human'

#    def __ne
    
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age


    def instance_method(self):
        self.age += 1
        return f'Hello {self.name}'
    

    @staticmethod
    def static_method():
        return 'goodbye'
    

    @classmethod
    def class_method(cls):
        return cls.species

    

bc = BasicClass(name='Juan', age=39)
print(bc.age)
print(bc.instance_method())
print(bc.name)
print(bc.age)

print(BasicClass.class_method())