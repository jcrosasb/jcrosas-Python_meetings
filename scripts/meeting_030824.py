import time

class Vehicle:
    '''This is a class that creates a vehicle with maker, model and year'''

    # Class attributes block
    version = '2.0'


    def __init__(self, maker: str, model: str, year: int):
        '''Initializer of Vehicle class'''
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer = 0


    def __str__(self):
        return f'Maker: {self.maker}, Model: {self.model}, Year: {self.year}'
    

    def __repr__(self) -> str:
        return f'Model: {self.model}'
    

    def __len__(self):
        return time.localtime()[0] - self.year
    
    # This also implements __iter__
    def __getitem__(self, key):
        if key == 0:
            return self.maker
        elif key == 1:
            return self.model
        elif key == 2:
            return self.year
        else:
            raise IndexError



    @classmethod
    def alternate_init(cls, vehicle_parameters:str):
        maker, model, year = vehicle_parameters.split(', ')
        return cls(maker=maker, model=model, year=year)
        #return cls(maker, model, year)
    

    @classmethod
    def alternate_init_2(cls, dictionary):
        maker = dictionary.get('maker')
        model = dictionary.get('model')
        year = dictionary.get('year')
        return cls(maker, model, year)
    

    @classmethod
    def f_150(cls):
        return cls('Ford', 'F-150', 2024)
    

class Car(Vehicle):
    pass


class ElectricCar(Car, Vehicle):
    pass

if __name__ == '__main__':

    car = Vehicle(maker='Toyota', model='Corolla', year=2024)

    salvador_car = Vehicle.alternate_init('Toyota, Camry, 2008')

    my_car = {'maker': 'Toyota', 
            'model': 'Camry',
            'year': 2008,
            'color': 'red'}

    sol_car = Vehicle.alternate_init_2(my_car)

    # print(salvador_car.model)
    # print(sol_car.model)

    # f_150 = Vehicle.f_150()

    # print(f_150)

    # print(len(sol_car))

    # print(sol_car[2])


    # for _ in sol_car:
    #     print(_)


    car_iterator = iter(sol_car)

    # print(next(car_iterator))
    # print(next(car_iterator))
    # print(next(car_iterator))
    #print(next(car_iterator))

    # uses of class methods
    #   1. Access class attributes
    #   2. Alternate __init__
    #   3. Define object with very specific attributes
    #   4. Change class attributes

    print(sol_car.__class__)
    print(type(sol_car))

    print(Vehicle.__bases__)
    print(Car.__bases__)
    print(ElectricCar.__bases__)