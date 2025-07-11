from atm import ATM
from account import Account
from dispense_strategy import DispenseStrategy,GreedyDispenseStrategy
from atm_states import IdleState

class ATMController:
    def __init__(self, atm: ATM):
        self.atm = atm
        self.current_account: Account= None
        self.dispense_strategy: DispenseStrategy = GreedyDispenseStrategy()
        self.current_state = IdleState()


    
    def authenticate_pin(self, account_no, pin):
        self.current_state.authenticate(self, account_no, pin)
        
    def change_state(self, state):
        self.current_state = state 
    
    def withdrawCash(self, amount):
       self.current_state.withdraw_cash(self, amount)

    def depositCash(self, amount):
        self.current_state.deposit_cash(self, amount)


    def checkCurrentBalance(self):
        self.current_state.show_balance(self)


    def showTransactionHistory(self):
        self.current_state.show_transaction_history(self)

    def transferMoney(self, account_no, amount):
        self.current_state.transfer_money(amount, account_no, self)
