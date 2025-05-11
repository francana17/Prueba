# Importación de librerías necesarias
import streamlit as st
import pandas as pd
import itertools
import matplotlib.pyplot as plt

# Importación de agentes y simulador
from agents.random_agent import RandomAgent
from agents.trend_agent import TrendAgent
from agents.anti_trend_agent import AntiTrendAgent
from agents.smart_agent import SmartAgent
from simulation.simulation import Simulation

# Función para generar los 100 agentes del sistema, incluyendo el SmartAgent con su "gene"
def generar_agentes(gene):
    agents = [RandomAgent(i) for i in range(51)]
    agents += [TrendAgent(51 + i) for i in range(24)]
    agents += [AntiTrendAgent(75 + i) for i in range(24)]
    smart_agent = SmartAgent(99, gene)
    agents.append(smart_agent)
    return agents, smart_agent

# Interfaz principal de Streamlit
st.title("Simulación de mercado de tarjetas gráficas")
modo = st.radio("Selecciona el modo:", ["Simulación rápida", "Optimización completa"])

# Botón para ejecutar la simulación
if st.button("Ejecutar simulación"):
    if modo == "Simulación rápida":
        # Ejecuta la simulación con un gene predefinido
        gene = [0.005, 0.01, 980, 900, 0.2]
        agents, smart_agent = generar_agentes(gene)
        sim = Simulation(agents)
        balance, prices, actions, final_cards, decision_log = sim.run()
    else:
        # Búsqueda exhaustiva (grid search) de parámetros para optimizar el SmartAgent
        best_balance = float('-inf')
        best_gene = None
        best_decision_log = []

        # Combinaciones de thresholds y condiciones para el gene
        param_combinations = list(itertools.product([0.0025, 0.005, 0.0075, 0.01], repeat=2))

        for buy_th, sell_th in param_combinations:
            for max_iter in [900, 950, 990]:
                for min_iter in [10, 50, 100]:
                    gene = [buy_th, sell_th, max_iter, min_iter, 0.2]
                    agents, smart_agent = generar_agentes(gene)
                    sim = Simulation(agents)
                    balance, prices, actions, final_cards, decision_log = sim.run()
                    # Guarda solo si el balance es mejor y se respetó la condición de terminar sin tarjetas
                    if balance > best_balance and final_cards == 0:
                        best_balance = balance
                        best_gene = gene
                        best_decision_log = decision_log

        # Resultado óptimo
        balance = best_balance
        decision_log = best_decision_log

    # Resultados tras ejecutar la simulación
    st.success(f"Balance final del SmartAgent: ${balance:.2f}")
    st.subheader("Decisiones del SmartAgent por iteración")

    # Mostrar las decisiones del agente como tabla
    df_decisiones = pd.DataFrame(decision_log)
    st.dataframe(df_decisiones)

    # Botón para descargar resultados en CSV
    csv = df_decisiones.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar decisiones en CSV",
        data=csv,
        file_name='smart_agent_decisiones.csv',
        mime='text/csv'
    )

    # Gráfico de precios y acciones del SmartAgent
    fig, ax = plt.subplots(figsize=(12, 6))
    df_decisiones["Iteración"] = df_decisiones["Iteración"].astype(int)

    ax.plot(df_decisiones["Iteración"], df_decisiones["Precio GPU"], label="Precio GPU", linewidth=2)

    compras = df_decisiones[df_decisiones["Acción"] == "buy"]
    ventas = df_decisiones[df_decisiones["Acción"] == "sell"]

    ax.scatter(compras["Iteración"], compras["Precio GPU"], color='green', label='Compra', marker='^', s=60)
    ax.scatter(ventas["Iteración"], ventas["Precio GPU"], color='red', label='Venta', marker='v', s=60)

    ax.set_xlabel("Iteración")
    ax.set_ylabel("Precio de la GPU")
    ax.set_title("Acciones del SmartAgent")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # Gráfico del balance total del SmartAgent
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.plot(df_decisiones["Iteración"], df_decisiones["Balance total"], label="Balance total", linewidth=2)
    ax2.set_xlabel("Iteración")
    ax2.set_ylabel("Balance total ($)")
    ax2.set_title("Evolución del balance total del SmartAgent")
    ax2.legend()
    ax2.grid(True)

    st.pyplot(fig2)
