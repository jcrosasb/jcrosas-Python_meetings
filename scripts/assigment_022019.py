import math
class ArrayNumber:
    ''' Class ArrayNumber serves to create array-like objects made up of numbers.'''
    def __init__(self, data):
        '''Initialize a new instance of Array Object
            Attributes:
                data: numbers to be included in ArrayNumber object'''
        self.data = data
        self.index = 0


    def __iter__(self):
        return self

    def _lazy_caterer_number(self, number):
        return (number**2 + number + 2) // 2
    
    def _triangle_number(self, number):
        return (number**2 + number) // 2
    
    def _fibonacci_number(self, number):
        return round((1/math.sqrt(5))*((1+math.sqrt(5))/2)**number - (1/math.sqrt(5))*((1-math.sqrt(5))/2)**number)

    def __next__(self):
        '''Method to return the next element in the ArrayNumber object'''
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return self._fibonacci_number(item)
        else:
            raise StopIteration

if __name__ == '__main__':

    array = ArrayNumber([1, 2, 7, 4, 1, 5, 8])

    iterator = iter(array)

    # print(next(array))
    # print(next(array))
    # print(next(array))
    # print(next(array))
    # print(next(array))
    # print(next(array))
    # print(next(array))


    for item in array:
        print(item)

    # while item := next(array, 0):
    #     print(item)
        
    try:
        while True:
            item = next(array)
            print(item)
    except StopIteration:
        print("Reached the end of the iterator")
