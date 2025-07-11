from abc import ABC, abstractmethod

class ATMState(ABC):
    @abstractmethod
    def authenticate(self, controller,  pin):
        pass
    @abstractmethod
    def withdraw_cash(self, controller,  amount):
        pass
    @abstractmethod
    def show_balance(self, controller):
        pass
    @abstractmethod
    def show_transaction_history(self, controller):
        pass
    @abstractmethod
    def deposit_cash(self, controller, amount):
        pass
    @abstractmethod
    def transfer_money(self, controller, amount, account_id):
        pass


class IdleState(ATMState):
    def authenticate(self, controller,  account_no, pin):
        account = controller.atm.get_account(account_no)
        if account.validatePin(pin):
            controller.current_account = account
            controller.change_state(Authenticatedtate())
    def withdraw_cash(self,controller, amount):
        print("Please Authenticate Using using Pin first")
    def show_balance(self, controller):
        print("Please Authenticate Using using Pin first")
    def show_transaction_history(self, controller):
        print("Please Authenticate Using using Pin first")
    
    def transfer_money(self, amount, account_id, controller):
        print("Please Authenticate Using using Pin first")
    
    def deposit_cash(self, controller, amount):
        print("Please Authenticate Using using Pin first")

class Authenticatedtate(ATMState):
    def authenticate(self, controller,  account_no, pin):
        print("Already authenticated")
    def withdraw_cash(self,controller, amount):
        if amount > controller.current_account.get_withdrawl_limit():
            print("Sorry amount exceeded the limit")
            return
        is_dispenseable = controller.dispense_strategy.dispense_cash(amount, controller.atm.cash_notes)
        if is_dispenseable:
            controller.current_account.deductBalance(amount)
    def show_balance(self, controller):
        balance = controller.current_account.checkBalance()
        print(f"Current balance is {balance}")
    def show_transaction_history(self, controller):
        controller.current_account.showPastTransaction()
    def transfer_money(self, amount, account_id, controller):
        reciever_account = controller.atm.get_account(account_id)
        ## It should be in a transaction
        reciever_account.addbalance(amount)
        controller.current_account.deductBalance(amount)

    def deposit_cash(self, controller, amount):
        controller.current_account.addbalance(amount)
