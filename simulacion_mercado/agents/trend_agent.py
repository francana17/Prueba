
import random
from .base import Agent

class TrendAgent(Agent):
    def decide(self, market, iteration):
        change = market.get_price_change_pct()
        # Si el precio ha subido ≥ 1% desde la última iteración:
        if change >= 1.0:
            # Tiene 75% de probabilidad de comprar
            return self.buy(market.price) if random.random() < 0.75 else 'hold'
        # Si no ha subido, tiene 20% de probabilidad de vender
        return self.sell(market.price) if random.random() < 0.20 else 'hold'

