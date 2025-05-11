
from .base import Agent

class SmartAgent(Agent):
    def __init__(self, id, gene):
        super().__init__(id)
        self.gene = gene  # Lista de parámetros de comportamiento [buy_th, sell_th, max_buy_iter, min_sell_iter, factor]

    def decide(self, market, iteration):
        price = market.price
        avg_price = market.get_moving_average()

        # Fuerza la venta en las últimas 5 iteraciones si tiene tarjetas
        if iteration >= 996 and self.cards > 0:
            return self.sell(price)

        # Compra si el precio actual es suficientemente más bajo que el promedio
        if price < avg_price * (1 - self.gene[0]) and self.can_buy(price):
            return self.buy(price)

        # Vende si el precio actual es suficientemente más alto que el promedio
        if price > avg_price * (1 + self.gene[1]) and iteration > self.gene[3] and self.can_sell():
            return self.sell(price)

        # Si no se cumplen condiciones, mantiene la posición
        self.actions.append('hold')
        return 'hold'

