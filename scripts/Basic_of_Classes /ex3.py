# Bank Accounts. For this exercise, assume that you are tasked with developing a Python program to manage bank accounts. 
# The requirements are to create a class named BankAccount that represents a bank account, allowing users to deposit money, withdraw money, and display account details. 
# Follow the guidelines to complete the exercise:

# 1. Define a bank account class
#     Name: BankAccount
#     Attributes:
#         account_number: A unique identifier for the bank account.
#         account_holder_name: The name of the account holder.
#         balance: The current balance of the account.

# 2. Set the initial state with the __init__ method. Use parameters:
#     account_number
#     account_holder_name
#     balance equals to zero

# 3. Define the behavior of the class
#     Name: deposit(amount)
#     Logic: Accepts an amount as a parameter and adds it to the account balance.
#     Name: withdraw(amount)
#     Logic: Accepts an amount as a parameter and subtracts it from the account balance if sufficient funds are available.  
#            Note: Ensure that appropriate error handling is implemented for withdrawal operations to prevent overdrawing from the account.
#     Name: display_details()
#     Logic: Displays the account details including account number, account holder name, and current balance.

class BankAccount:

    def __init__(self, account_number: str , account_holder_name: str, balance: int=0) -> None:
        '''Initializer of BankAccount class
           Parameters:
                * account_number: (string) the bank account number.
                * account_holder_name: (integer) the bank account number.
                * balance: (integer) the amount deposited into the account'''
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance


    def deposit(self, amount: int):
        '''Method to deposit money into account
           Parameters:
                * amount: (integer) the amount of money to be deposited
           Returns:
                * self.balance: (integer) the updated balance with the money deposited'''
        self.balance += amount
        return None


    def withdraw(self, amount: int):
        '''Method to withdraw money from account
           Parameters:
                * amount: (integer) the amount of money to be withdrawn. If amount exceeds balance, it
                          will raise an error.
           Returns:
                * self.balance: (integer) the updated balance with the money withdrawn'''
        if amount > self.balance:
            raise ValueError('Withdraw amount exceeds balance')
        self.balance -= amount
        return None


    def display_details(self):
        '''Method to display account number, holder name and current balance'''
        print(f'\nAccount Number: {self.account_number}\n',
              f'Account Holder Name: {self.account_holder_name}\n',
              f'Current Balance: {self.balance}')


if __name__ == '__main__':

    bank_account = BankAccount(account_number="123456789", 
                               account_holder_name= "John Doe", 
                               balance=1000)
    
    bank_account.display_details()

    bank_account.deposit(500)

    bank_account.display_details()

    bank_account.withdraw(500)

    bank_account.display_details()

#    bank_account.withdraw(5000)