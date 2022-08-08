from calculator import Calculator
from telephone import Telephone
from wallet import Wallet

class Smartphone:
    def __init__(self, model, fab_date, color):
        self.model = model
        self.fab_date = fab_date
        self.color = color
            
        print( f'As especifiações do smartphone são as seguintes:\nModelo: {self.model}\nData de Fabricação: {self.fab_date}\nCor: {self.color}')

        self.wallet1 = Wallet(1000)
        
        self.tele1 = Telephone()

        self.calc1 = Calculator()
    
