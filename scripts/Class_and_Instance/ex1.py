# Librarian Console. 
# In this exercise, you implement the concept of class attributes and instance attributes to design 
# a program to automate and manage the lending and return processes, inventory tracking, 
# and fine calculation in a library environment efficiently. 
# This exercise is split into three main components. 
# Complete each component at a time and verify your code. Follow the instructions to complete each component.

# 1. Base class.
#     Define a Book class with attributes title, author, copies, and available_copies.
#     The basic functionality includes the methods to borrow a book and to return a book. 
#     Note: The borrow a book decreases the available copies while the return a book increases it.
#     Use a class-level attribute total_books to track the number of books
#     Use the template:

import hashlib

class Book:
    '''Class to create a book record for a library, which includes
            * title of book
            * author of book
            * number of copies of the book'''
    
    # Class attributes
    total_books = 0
    
    def __init__(self, title: str, author:str, copies:int=1):
        '''Instantiate a Book object
           Parameters:
                * title: (string) the title of the book
                * author: (string) the author of the book
                * copies: the number of copies available. Default is set to 1
           In addition, we also have:
                * book_id: unique identifier for each book
                * available_copies: initially set to "copies"
                * The class attribute is increased by 1 each time we create a new Book'''
        self.update_total_books()
        self.title = title
        self.author = author
        self.copies = copies
        self.available_copies = copies
        self.book_id = self.generate_id()


    @classmethod
    def update_total_books(cls)->None:
        '''Method to update the number of books'''
        cls.total_books += 1
        return None


    def borrow_book(self)->None:
        '''Method to borrow a book. The total number of copies remains unchanged but the number of available
           copies decreases by one. If there are no available copies, it raises an error'''
        if self.available_copies == 0:
            raise ValueError('No copies to borrow')
        self.available_copies -= 1
        return None


    def return_book(self)->None:
        '''Method to return a book. The total number of copies remains unchanged but the number of available
           copies increases by one. If all copies are available, it raises an error'''
        if self.available_copies == self.copies:
            raise ValueError('The number of available copies is complete')
        self.available_copies += 1
        return None


    def fine_calculator(self, number_days: int)->float:
        '''Method to calculate the fine based on the number of days the book was not returned
           Parameters:
                * number_days: (Integer) the number of days after the due day
           Return:
                * The total fine. For each day, $0.5 is charged'''
        return number_days * 0.5


    def add_copies(self, new_copies: int)->None:
        '''Method to add new copies to the library
           Parameters:
                * new_copies: (Integer) the number of new books to be added'''
        if new_copies < 0:
            raise ValueError('Number of copies to be added must be positive')
        self.copies += new_copies
        self.available_copies += new_copies
        return None
    

    def remove_copies(self, num_copies: int)->None:
        '''Method to remove copies from the library
           Parameters:
                * num_copies: (Integer) the number of books to be removed'''
        if num_copies > self.available_copies:
            raise ValueError('The numbers of books to be removed exceeds the number of available copies')
        if num_copies < 0:
            raise ValueError('Number of copies to be removed must be positive')
        self.available_copies -= num_copies
        self.copies -= num_copies
        return None
    

    def generate_id(self)->str:
        '''Method to generate the ID of the book based on the title'''
        return hashlib.sha1(self.title.encode()).hexdigest()


    def __str__(self):
        '''Method to print the status of each book'''
        return f'ID: {self.book_id}\n' + \
               f'Title: {self.title}\n' + \
               f'Author: {self.author}\n' + \
               f'Total copies: {self.copies}\n' + \
               f'Available copies: {self.available_copies}'
            
    
if __name__ == '__main__':

    book_1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book_2 = Book("To Kill a Mockingbird", "Harper Lee", copies=5)

    print(Book.total_books)

    print(book_1.book_id)
    print(book_2.book_id)

    # # Test if it will raise ValueError on 'borrow_book()'
    # for _ in range(2):
    #     book_1.borrow_book()

    # book_1.add_copies(3)

    # print(book_1.copies)

    # book3 = Book(title='Harry Potter',
    #              author='JK Rowling',
    #              copies=3)
    
    # print(book3)
    # book3.borrow_book()
    # print(book3)
    # book3.borrow_book()
    # print(book3)
    # book3.borrow_book()   
    # print(book3)

    # # This will fail
    # # book3.borrow_book()   
    # # print(book3)

    # book3.return_book()
    # print(book3)

    # # print(Book.total_books)


    # book4 = Book(title='Lord of the Ring',
    #              author='Tolkine',
    #              copies=5)
    
    # print(Book.total_books)


    # # print(book2)




