# =========================================================
# 🏬 PLATAFORMA EMPRESARIAL
# Identificación de Clientes de Alto Valor
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

sns.set(style="whitegrid")

st.set_page_config(page_title="Panel Empresarial - Clientes de Alto Valor", layout="wide")

# =========================================================
# 🔷 ENCABEZADO – ESTILO EMPRESA
# =========================================================

st.markdown("""
# 🏬 **PANEL CORPORATIVO – SEGMENTACIÓN DE CLIENTES**
Este sistema identifica a los **clientes de alto valor** en base a su comportamiento de compra.
Ideal para áreas de **Marketing, Ventas y Fidelización**.
""")

# =========================================================
# 📥 CARGA AUTOMÁTICA DEL DATASET (NO PEDIMOS NADA AL USUARIO)
# =========================================================

url = "https://raw.githubusercontent.com/JDanielhtc/Proyecto_Mineria/refs/heads/main/datakggle1.csv"
df = pd.read_csv(url, encoding="latin-1")

# Limpieza
df = df.dropna(subset=["Quantity", "UnitPrice", "CustomerID"])
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# =========================================================
# 🧮 CREACIÓN DE VARIABLES
# =========================================================

df["total_compra"] = df["Quantity"] * df["UnitPrice"]

clientes = df.groupby("CustomerID").agg(
    total_cantidad=("Quantity","sum"),
    gasto_total=("total_compra","sum"),
    precio_promedio=("UnitPrice","mean"),
    ticket_promedio=("total_compra","mean")
).reset_index()

# =========================================================
# 🎯 DEFINIR CLIENTES DE ALTO VALOR
# =========================================================

umbral = clientes["gasto_total"].median()
clientes["alto_valor"] = (clientes["gasto_total"] >= umbral).astype(int)

# =========================================================
# 🎛️ PANEL RESUMEN (KPIs)
# =========================================================

col1, col2, col3 = st.columns(3)

col1.metric("👥 Total de Clientes", clientes.shape[0])
col2.metric("💎 Clientes de Alto Valor", int(clientes["alto_valor"].sum()))
col3.metric("📈 % Alto Valor",
            f"{100 * clientes['alto_valor'].mean():.1f}%")

# =========================================================
# 🔘 BOTÓN PRINCIPAL – IDENTIFICAR CLIENTES
# =========================================================

st.markdown("## 📊 Identificación de Clientes de Alto Valor")

if st.button("🔍 GENERAR CLASIFICACIÓN DE CLIENTES"):
    
    st.success("Clasificación completada.")

    # --- Gráfico de distribución del gasto ---
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(clientes["gasto_total"], kde=True, ax=ax)
    ax.axvline(umbral, color="red", linestyle="--", label="Umbral alto valor")
    ax.legend()
    st.pyplot(fig)

    # --- Tabla de clientes de alto valor ---
    top_clientes = clientes.sort_values("gasto_total", ascending=False).head(20)
    
    st.markdown("### 💎 TOP 20 Clientes de Alto Valor")
    st.dataframe(top_clientes)

    # --- Recomendaciones ---
    st.markdown("""
    ## 💡 Recomendaciones de Acción Comercial

    ✔ Enviar ofertas **premium** a los clientes de alto valor  
    ✔ Programar **campañas de fidelización**  
    ✔ Ofrecer **membresías exclusivas**  
    ✔ Retener a clientes con alto ticket y alta frecuencia

    """)

# =========================================================
# 🎁 SECCIÓN 100% EMPRESARIAL – GENERADOR DE OFERTAS
# =========================================================

st.markdown("## 🎁 Generar Oferta Automática")

opcion = st.selectbox("Selecciona el tipo de oferta:", [
    "Descuento 20% en productos premium",
    "Envío gratis por 30 días",
    "Puntos dobles en compras",
    "Acceso a preventas exclusivas"
])

if st.button("🎯 Aplicar oferta a clientes de alto valor"):
    st.success(f"Oferta aplicada: **{opcion}**")
    st.write("La estrategia se ha aplicado a todos los clientes de alto valor (simulación).")
