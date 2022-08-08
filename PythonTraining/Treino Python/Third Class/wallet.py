class Wallet:
    def __init__(self, saldo):
        self.saldo = saldo    

    def payment(self, valor):
        self.saldo -= valor
        print (f'\nPagando {valor} sua carteira fica com o total de {self.saldo}')

    def recieve(self, valor):
        self.saldo += valor
        print (f'\nRecebendo {valor} sua carteira fica com o total de {self.saldo}')
    
