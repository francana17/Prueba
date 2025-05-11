# Simulación de Mercado de Tarjetas Gráficas

Este proyecto modela un mercado artificial donde distintos agentes económicos compran y venden tarjetas gráficas en función de reglas predefinidas. El objetivo es simular comportamientos económicos y optimizar el rendimiento de un agente inteligente (SmartAgent) que busca maximizar su balance final.

## 🏗️ Arquitectura del Proyecto

```
simulacion_mercado/
│
├── agents/             # Lógica de los distintos tipos de agentes
│   ├── base.py
│   ├── random_agent.py
│   ├── trend_agent.py
│   ├── anti_trend_agent.py
│   └── smart_agent.py
│
├── market/
│   └── market.py       # Modelo del mercado
│
├── simulation/
│   └── simulation.py   # Lógica principal de simulación
│
├── app.py              # Interfaz de usuario con Streamlit
├── requirements.txt    # Dependencias del proyecto
├── Dockerfile          # Contenedor Docker para desplegar la app
└── utils/              # (Opcional) Funciones auxiliares
```

## ⚙️ Funcionamiento

- **100 agentes** interactúan durante **1000 iteraciones**:
  - 51 agentes aleatorios.
  - 24 tendenciales.
  - 24 anti-tendenciales.
  - 1 SmartAgent con estrategia configurable.
- Cada agente decide si comprar, vender o mantener su posición.
- El precio del mercado sube un 0.5% por cada compra, y baja un 0.5% por cada venta.

## 🎯 Objetivo del SmartAgent

El `SmartAgent` busca:
- Comprar cuando el precio está significativamente por debajo del promedio.
- Vender cuando el precio supera el promedio por cierto margen.
- Terminar la simulación con **cero tarjetas** y el **mayor balance posible**.

## 🚀 Instrucciones para correr

### Requisitos

- Python 3.11+
- pip

### Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Docker

```bash
docker build -t simulacion-app .
docker run -p 8501:8501 simulacion-app
```

Luego accede a http://localhost:8501 en tu navegador.

## 📦 Output

- Visualización de decisiones y precios.
- Gráfico de acciones (compra/venta).
- Gráfico de evolución del balance total.
- Botón para descargar el historial del SmartAgent en CSV.

## 🧹 Limpieza

- Puedes eliminar las carpetas `__pycache__/` si lo deseas, ya que son generadas automáticamente.
- Los archivos `__init__.py` son necesarios para la correcta importación de módulos en Python.

---

© 2025 - Simulación para prueba técnica.
