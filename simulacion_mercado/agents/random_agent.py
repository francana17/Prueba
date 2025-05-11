
import random
from .base import Agent

class RandomAgent(Agent):
    def decide(self, market, iteration):
        # Escoge aleatoriamente entre comprar, vender o mantener
        choice = random.choice(['buy', 'sell', 'hold'])
        if choice == 'buy':
            return self.buy(market.price)
        elif choice == 'sell':
            return self.sell(market.price)
        self.actions.append('hold')  # Si elige 'hold'
        return 'hold'

