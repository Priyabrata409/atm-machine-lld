from atm import ATM
from account import Account, AccountFactory
from atm_controller import ATMController



def main():
    account1 = AccountFactory.get_account_instance("savings","Hari", 98231, "0909", 20000)
    account2 = AccountFactory.get_account_instance("savings","Rama", 98341, "0011", 40000)
    account3 = AccountFactory.get_account_instance("savings","Sama", 13741, "1020", 50000)
    atm = ATM()
    atm.add_acount(account1)
    atm.add_acount(account2)
    atm.add_acount(account3)

    atm_controller = ATMController(atm)
    atm_controller.authenticate_pin(98231, "0909")
    atm_controller.checkCurrentBalance()
    atm_controller.depositCash(20000)
    atm_controller.withdrawCash(10000)
    atm_controller.transferMoney(98341, 10000)
    atm_controller.showTransactionHistory()

main()