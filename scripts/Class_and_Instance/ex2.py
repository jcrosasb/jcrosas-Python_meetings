# A bakery management system can provide an excellent context for demonstrating 
# the use of class methods, instance methods, and static methods. 
# In this exercise, you consider a bakery where various types of pastries are produced and sold, 
# and use the concepts of methods to manage inventory and calculate pricing. Follow the steps below:

class Pastry:
    '''Class to create a record for a pastry, which inlcude:
            * name of the pastry
            * cost of each pastry
            * quantity of pastries made'''

    '''Class attributes'''
    total_pastries_produced:int = 0
    total_revenue:float = 0
    standard_markup:float = 1.5

    def __init__(self, name:str, cost_price:float, quantity:int) -> None:
        '''Initializes Pastry object
           Parameters:
                * name: (String) the name of the pastry
                * cost_price: (float) the price of the pastry
                * quantity: (int) the number of pastries created'''
        self.name = name
        self.cost_price = cost_price
        self.quantity = quantity
        self.update_total_pastries_produced(self.quantity)


    @classmethod
    def update_total_pastries_produced(cls, quantity)->None:
        '''Method to update the class attribute "total_pastries_produced" by "quantity"
           Parameters:
                * quantity: (Integer) the number of pastries that we want to add'''
        cls.total_pastries_produced += quantity
        return None


    @classmethod
    def total_production(cls)->int:
        '''Method to keep track of total number of pastries created
           returns:
                * total_pastries_produced: (integer) class level attribute that keeps track of number of pastries'''
        return cls.total_pastries_produced
    

    @classmethod
    def markup(cls)->float:
        '''Method to keep track of markup
           returns:
                * standard_markup: (float) class level attribute'''
        return cls.standard_markup
    

    @classmethod
    def update_total_revenue(cls, amount)->None:  
        '''Method to update the total revenue
           Parameters:
                * amount: (Float) the amount to be added to revenue'''
        if amount < 0:
            raise ValueError('amount must be positive')
        cls.total_revenue += amount
        return None
    

    @staticmethod
    def display_pricing_info(pastries: list['Pastry'])->None:
        '''method to display pricing information
           Parameters:
                * pastries: list with Pastry objects that we want to display'''
        for pastry in pastries:
            print(f'{pastry.name}: ${pastry.calculate_price()}')
        return None
    

    def update_quantity(self, num_new_item: int)->None:
        '''Method to update the number of pastries created'''
        self.update_total_pastries_produced(num_new_item - self.quantity) 
        self.quantity = num_new_item
        return None
   

    def calculate_price(self)->float:
        '''Method to calculate the total price of each pastry'''
        return self.cost_price * self.markup()


    def sell(self, num_items:int)->float:
        '''Method to calculate the price of a sell. It also updates the revenue and the number of 
           pastries available
           Parameters:
                * num_items: (integer) the number of integers sold'''
        if num_items < 0:
            raise ValueError('num_items must be positive')
        self.quantity -= num_items
        # self.update_total_pastries_produced(-num_items)
        profit_by_sell = num_items * self.calculate_price()
        self.update_total_revenue(profit_by_sell)
        return profit_by_sell


if __name__ == '__main__':

    pastry1=Pastry("Croissant", 2.5, 50)
    pastry2=Pastry("Danish", 2.0, 40)

    print(Pastry.total_production())
    #print(Pastry.update_total_revenue())

    pastry1.update_quantity(60)
    print(Pastry.total_production())

    pastries = [pastry1, pastry2]
    Pastry.display_pricing_info(pastries)

    print(pastry1.sell(10) )
    print(pastry2.sell(20))
    print(Pastry.total_revenue)



