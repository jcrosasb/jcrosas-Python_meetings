# Exercise 1. Complex Numbers. 
# In this exercise, you create a complex number calculator. 
# Create a class called ComplexNumber to represent complex numbers. 
# Include methods to add, subtract, multiply, and divide two complex numbers. 
# Note: Define a human-readable interface to print complex numbers to the console.

class ComplexNumber:

    i = (-1)**0.5

    def __init__(self, real: float, imag: float) -> None:
        '''Initializer for ComplexNumber objects
           Parameters:
                * real: (float) the real part of the complex number
                * imag: (float) the imaginary part of the complex number'''
        self.real = real
        self.imag = imag

    
    def __add__(self, complex: 'ComplexNumber') -> 'ComplexNumber':
        '''Dunder method to calculate the sum of two complex numbers
           Parameters:
                * complex: (ComplexNumber) Complex number to be added to self complex number
           Returns:
                * (ComplexNumber) The sum of both complex number'''
        return ComplexNumber(self.real + complex.real, self.imag + complex.imag)

    def __sub__(self, complex: 'ComplexNumber') -> 'ComplexNumber':
        '''Dunder method to calculate the substraction of two complex numbers
           Parameters:
                * complex: (ComplexNumber) Complex number to be substracted to self complex number
           Returns:
                * (ComplexNumber) The substraction of both complex number'''
        return ComplexNumber(self.real - complex.real, self.imag - complex.imag)
    

    def __mul__(self, complex: 'ComplexNumber') -> 'ComplexNumber':
        '''Dunder method to calculate the multiplication of two complex numbers
           Parameters:
                * complex: (ComplexNumber) Complex number to be multiplied to self complex number
           Returns:
                * (ComplexNumber) The multiplication of both complex number'''
        return ComplexNumber(self.real*complex.real - self.imag*complex.imag, \
                             self.real*complex.imag + self.imag*complex.real)


    def __truediv__(self, complex: 'ComplexNumber') -> 'ComplexNumber':
        '''Dunder method to calculate the true division of two complex numbers
           Parameters:
                * complex: (ComplexNumber) Complex number to be divided to self complex number
           Returns:
                * (ComplexNumber) The division of both complex number'''
        return ComplexNumber((self.real*complex.real + self.imag*complex.imag)/(complex.real**2 + complex.imag**2), \
                             (self.imag*complex.real - self.real*complex.imag)/(complex.real**2 + complex.imag**2))
    

    def __str__(self):
        '''Dunder method to print complex numbers in their standar form: a + jb'''
        if self.imag < 0:
            return f'{self.real} - {-1*self.imag}j'
        return f'{self.real} + {self.imag}j'


if __name__ == '__main__':

    complex_number_1 = ComplexNumber(3, 2)
    complex_number_2 = ComplexNumber(1, 4)

    print(f'The complex numbers are: {complex_number_1} and {complex_number_2}\n')

    print(complex_number_1 + complex_number_2)
    print(complex_number_1 - complex_number_2)
    print(complex_number_1 * complex_number_2)
    print(complex_number_1 / complex_number_2)
