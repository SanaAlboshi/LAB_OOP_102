# bank_account.py

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        # Remove leading/trailing spaces from name
        account_holder = account_holder.strip()

       # Validate name length
        if len(account_holder) <= 2:
            raise ValueError("Account holder name must be longer than 2 characters ⚠️")

       #only letters (spaces allowed)
        if not account_holder.replace(" ", "").isalpha():
            raise ValueError("Account holder name must contain only letters ⚠️")
        
      #initial balance is not negative
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative ⚠️")

        self.__account_holder = account_holder.title()  
        self.__balance = initial_balance

        #deposit money
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive ⚠️")
        self.__balance += amount
        return self.__balance
    
    #withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive ⚠️")
        if amount > self.__balance:
            raise Exception("Insufficient funds ⚠️")
        self.__balance -= amount
        return self.__balance
    
    #get current balance
    def get_balance(self):
        return self.__balance
    
    #get account holder name
    def get_account_holder(self):
        return self.__account_holder
