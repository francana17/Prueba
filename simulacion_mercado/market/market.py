class Market:
    def __init__(self, initial_price=200.0, stock=100_000):
        # Precio inicial del mercado ($200 por tarjeta gráfica)
        self.price = initial_price

        # Stock total disponible (aunque actualmente no se usa para limitar compras)
        self.stock = stock

        # Historial de precios, empezando con el precio inicial
        self.history = [initial_price]

    def update_price(self, action):
        # Actualiza el precio según la acción de un agente
        if action == 'buy':
            self.price *= 1.005  # Si se compra, el precio sube un 0.5%
        elif action == 'sell':
            self.price *= 0.995  # Si se vende, el precio baja un 0.5%

        # Añade el nuevo precio al historial
        self.history.append(self.price)

    def get_price_change_pct(self):
        # Calcula el cambio porcentual de precio respecto a la iteración anterior
        if len(self.history) < 2:
            return 0.0  # Si no hay suficiente historial, no hay cambio
        return (self.price - self.history[-2]) / self.history[-2] * 100

    def get_moving_average(self, window=10):
        # Calcula el promedio móvil del precio en las últimas `window` iteraciones
        if len(self.history) < window:
            # Si no hay suficientes datos, calcula el promedio de todo lo que haya
            return sum(self.history) / len(self.history)
        # Calcula el promedio solo de las últimas `window` entradas
        return sum(self.history[-window:]) / window

