
class Agent:
    def __init__(self, id, balance=1000):
        self.id = id  # Identificador único del agente
        self.balance = balance  # Dinero disponible
        self.cards = 0  # Número de tarjetas gráficas que posee
        self.actions = []  # Historial de acciones realizadas

    def can_buy(self, price):
        return self.balance >= price  # Puede comprar si tiene suficiente dinero

    def can_sell(self):
        return self.cards > 0  # Puede vender si tiene al menos una tarjeta

    def buy(self, price):
        if self.can_buy(price):
            self.balance -= price
            self.cards += 1
            self.actions.append('buy')
            return 'buy'
        self.actions.append('hold')  # No puede comprar, se queda quieto
        return 'hold'

    def sell(self, price):
        if self.can_sell():
            self.balance += price
            self.cards -= 1
            self.actions.append('sell')
            return 'sell'
        self.actions.append('hold')  # No puede vender, se queda quieto
        return 'hold'

    def decide(self, market, iteration):
        raise NotImplementedError  # Método abstracto, se define en subclases

