from abc import ABC, abstractmethod
import time
import uuid

class Transaction:
    def __init__(self, transaction_amount, transaction_type: str):
        self.transaction_id = uuid.uuid1()
        self.amount = transaction_amount
        self.transaction_type = transaction_type
        
    
    def __str__(self):
        return f"{time.time()} - {self.transaction_id}: Amount of {self.amount} {self.transaction_type} from your account"
    

class Account(ABC):
    def __init__(self,name, account_no, pin, amount):
        self.name = name
        self.account_no = account_no
        self.pin = pin
        self.amount = amount
        self.transactions = []


    def checkBalance(self):
        return self.amount
    
    def validatePin(self, pin):
        return self.pin == pin
    
    def addbalance(self, amount):
        self.amount += amount
        self.addTransaction(Transaction(amount, "credit"))
        

    def deductBalance(self, amount):
        self.amount -= amount
        self.addTransaction(Transaction(amount, "debit"))
    
    def addTransaction(self, transaction_message):
        self.transactions.append(transaction_message)


    def showPastTransaction(self):
        for transaction in self.transactions:
            print(transaction)

    @abstractmethod
    def get_withdrawl_limit(self):
        pass

class SavingsAccount(Account):
    def get_withdrawl_limit(self):
        return 40000
    
class CurrentAccount(Account):
    def get_withdrawl_limit(self):
        return 90000
    

class AccountFactory:
    @staticmethod
    def get_account_instance(account_type, name, account_no, pin, amount):
        if account_type == "savings":
            return SavingsAccount(name, account_no, pin, amount)
        
        if account_type == "current":
            return CurrentAccount(name, account_no, pin, amount)
        
