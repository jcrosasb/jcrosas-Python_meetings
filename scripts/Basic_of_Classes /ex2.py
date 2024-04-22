# Exercise 2. Vector. 
# In this exercise, you model mathematical vectors using classes. 
# Write a Python class called Vector that represents a vector in n-dimensional space. 
# Include methods to add two vectors, subtract two vectors, calculate the dot product of two vectors, and calculate the magnitude of a vector.

class Vector:

    def __init__(self, *args: float) -> None:
        '''Initializer for Vector Class, representing a vector in n-dimensional space
           Parameters:
                args: coordinate numbers of the vector (can be any number). Coordinates are
                      then stored in attribute "data"'''
        self.data = [i for i in args]


    def __add__(self, vector: 'Vector'):
        '''Dunder method for addition of vectors
           Parameters:
                * vector: a separate Vector object to be added to self Vector
           Returns:
                * The sum of both vector objects'''
        if len(self.data) != len(vector.data):
            raise ValueError('Both vectors have to be of same length')
        return Vector(*[x+y for x,y in zip(self.data, vector.data)])
    

    def __sub__(self, vector: 'Vector'):
        '''Dunder method for substraction of vectors
           Parameters:
                * vector: a separate Vector object to be substracted to self Vector
           Returns:
                * The rest of both vector objects'''
        if len(self.data) != len(vector.data):
            raise ValueError('Both vectors have to be of same length')
        return Vector(*[x-y for x,y in zip(self.data, vector.data)])
    

    def dot_product(self, vector: 'Vector'):
        '''Method for dot product of vectors
           Parameters:
                * vector: a separate Vector object with wich the doct product will be done with self Vector
           Returns:
                * The dot product of both vector objects'''
        if len(self.data) != len(vector.data):
            raise ValueError('Both vectors have to be of same length')
        return sum(x*y for x,y in zip(self.data, vector.data))
    

    def magnitude(self):
        '''Method for magnitude of a vector.
           Returns:
                * The magnitude of a vector=(a1, a2, ..., an), defined as
                  sqrt(a1^2 + a2^2 + ... + an^2)'''
        return (sum(coordinate**2 for coordinate in self.data))**0.5
    

    def __str__(self):
        '''Dunder method to print a vector'''
        return f'{self.data}'


if __name__ == '__main__':

    vector_1 = Vector(1, 2, 3)
    vector_2 = Vector(4, 5, 6)

    print(f'The vectors are: {vector_1} and {vector_2}\n')

    print(f'The sum is {vector_1 + vector_2}')
    print(f'The rest is {vector_1 - vector_2}')
    print(f'The dot product is {vector_1.dot_product(vector_2)}')
    print(f'The magnitude of {vector_1} is {vector_1.magnitude()}')
    print(f'The magnitude of {vector_2} is {vector_2.magnitude()}')