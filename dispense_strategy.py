from abc import ABC, abstractmethod

class DispenseStrategy(ABC):
    @abstractmethod
    def dispense_cash(self,amount, notes):
        pass

class GreedyDispenseStrategy(DispenseStrategy):
    def dispense_cash(self,amount, cash_notes):  
        cash = []
        i = 0
        while i < len(cash_notes):
            count = amount // cash_notes[i]
            cash.append(f"{count} of {cash_notes[i]} note")
            amount = amount % cash_notes[i]
            i+=1

        if amount != 0:
            print("Sorry amount can't be dispense")
            return False
        for note in cash:
            print(note)
            return True