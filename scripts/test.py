class Vehicle:
    def __new__(cls, **kwargs):
        maker = kwargs.get('maker')
        
        if maker != 'Ford':
            raise ValueError("Vehicle maker must be Ford")
        
        print("Creating a new Vehicle instance")
        instance = super().__new__(cls)
        
        return instance
    def __init__(self, maker, model, year):
        print("Initializing the Vehicle instance")
        self.maker = maker
        self.model = model
        self.year = year


class Car(Vehicle):
    def __new__(cls, **kwargs):
        
        color = kwargs.get('color')
        if color == 'White':
            raise ValueError("White cars are not allowed")
        
        print("Creating a Car...")        
        instance = super().__new__(cls, **kwargs)
        
        return instance
    def __init__(self, maker, model, year, color):
        print("Initializing the Car instance")
        super().__init__(maker, model, year)
        self.color = color


red_car = Car(maker='Toyota', model='Corolla', year=2024, color='red')