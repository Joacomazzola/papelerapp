import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, binom

# Título de la aplicación
st.title("Distribuciones de Probabilidad con Notas")

# Selección de la distribución
distribucion = st.sidebar.selectbox(
    "Selecciona una distribución",
    ("Normal", "Exponencial", "Binomial")
)

# Parámetros para cada distribución
if distribucion == "Normal":
    mean = st.sidebar.slider("Media", -10.0, 10.0, 0.0)
    std_dev = st.sidebar.slider("Desviación estándar", 0.1, 10.0, 1.0)
    x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
    y = norm.pdf(x, mean, std_dev)
    st.write(f"Distribución Normal (media={mean}, desviación estándar={std_dev})")
elif distribucion == "Exponencial":
    scale = st.sidebar.slider("Escala (1/λ)", 0.1, 10.0, 1.0)
    x = np.linspace(0, 3*scale, 100)
    y = expon.pdf(x, scale=scale)
    st.write(f"Distribución Exponencial (escala={scale})")
elif distribucion == "Binomial":
    n = st.sidebar.slider("Número de ensayos", 1, 100, 10)
    p = st.sidebar.slider("Probabilidad de éxito", 0.0, 1.0, 0.5)
    x = np.arange(0, n+1)
    y = binom.pmf(x, n, p)
    st.write(f"Distribución Binomial (n={n}, p={p})")

# Gráfico de la distribución
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(f"Distribución {distribucion}")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
st.pyplot(fig)

# Área de notas
st.header("Notas")
notas = st.text_area("Escribe tus notas aquí:")

# Guardar notas (opcional)
if st.button("Guardar notas"):
    with open("notas.txt", "w") as f:
        f.write(notas)
    st.success("Notas guardadas con éxito")

# Mostrar notas guardadas (opcional)
try:
    with open("notas.txt", "r") as f:
        saved_notes = f.read()
    st.text_area("Notas guardadas:", value=saved_notes, height=200)
except FileNotFoundError:
    st.info("No hay notas guardadas aún.")
