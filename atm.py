from account import Account

class ATM:
    def __init__(self):
        self.cash_notes = [2000, 500, 200, 100]
        self.account_map = {}

    def add_acount(self, account: Account):
        self.account_map[account.account_no] = account

    def get_account(self, account_no):
        return self.account_map[account_no]
    




