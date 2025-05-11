from market.market import Market  # Importa la clase Market para manejar el precio y su historial

class Simulation:
    def __init__(self, agents, iterations=1000):
        self.agents = agents          # Lista de objetos tipo Agent
        self.market = Market()        # Instancia del mercado de tarjetas gráficas
        self.iterations = iterations  # Número total de iteraciones a simular

    def run(self):
        smart_agent = self.agents[-1]  # Se asume que el SmartAgent es el último en la lista
        decision_log = []              # Lista para registrar el historial de decisiones

        for i in range(1, self.iterations + 1):
            from random import shuffle
            shuffle(self.agents)  # Reordena aleatoriamente a los agentes en cada iteración

            smart_action = 'hold'  # Inicializa la acción del SmartAgent para esta iteración

            for agent in self.agents:
                action = agent.decide(self.market, i)  # Cada agente toma una decisión
                self.market.update_price(action)       # Se actualiza el precio según su acción
                if agent is smart_agent:
                    smart_action = action  # Guarda la acción del SmartAgent

            # Calcula el balance total del SmartAgent (efectivo + valor de sus tarjetas)
            current_balance = smart_agent.balance + smart_agent.cards * self.market.price

            # Registra los datos relevantes de esta iteración
            decision_log.append({
                "Iteración": i,
                "Acción": smart_action,
                "Precio GPU": round(self.market.price, 2),
                "Balance efectivo": round(smart_agent.balance, 2),
                "Tarjetas": smart_agent.cards,
                "Balance total": round(current_balance, 2)
            })

        # Devuelve los resultados principales de la simulación
        return (
            smart_agent.balance,
            self.market.history[:1000],
            smart_agent.actions[:1000],
            smart_agent.cards,
            decision_log
        )

