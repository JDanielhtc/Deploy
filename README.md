
<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&text=Clasificación%20de%20Clientes%20de%20Alto%20Valor&fontSize=36&fontAlignY=35&animation=twinkling&fontColor=ffffff)

### 🔎 *Minería de Datos — Unidad 2*

Plataforma web funcional para identificar clientes de alto valor mediante Machine Learning.

</div>

---

# 📘 Descripción del Proyecto

Este proyecto desarrolla un modelo de **Machine Learning (RandomForestClassifier)** para clasificar clientes en:

- 🟢 **Alto valor**  
- 🔴 **Bajo valor**

Usando datos reales de e-commerce (Kaggle).  

Además, se creó una **aplicación web funcional con Streamlit** que permite:

✅ Subir el dataset  
✅ Entrenar el modelo directamente  
✅ Visualizar métricas (ROC, PR, matriz de confusión)  
✅ Detectar clientes de alto valor  
✅ Simular acciones comerciales (p. ej., aplicar ofertas)  

---

# 📂 Estructura del Repositorio



Proyecto_Mineria_U2/
│
├── streamlit_app.py # Aplicación web Streamlit
├── requirements.txt # Dependencias del proyecto
├── modelo_colab.ipynb # Notebook con el pipeline completo de minería
├── datakggle1.csv # Dataset usado (opcional)
└── README.md # Este archivo


---

# 📥 Dataset utilizado

Dataset original de Kaggle (Online Retail).

Versión procesada en RAW GitHub para carga directa:

🔗 https://raw.githubusercontent.com/JDanielhtc/Proyecto_Mineria/refs/heads/main/datakggle1.csv

---

# ▶ Cómo ejecutar el proyecto en local

### **1️⃣ Clonar el repositorio**

```bash
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO

2️⃣ (Opcional) Crear entorno virtual

Windows

python -m venv venv
venv\Scripts\activate


3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Ejecutar la aplicación web
streamlit run streamlit_app.py


La app se abrirá en:

👉 http://localhost:8501

☁ Cómo desplegar en la nube (Streamlit Cloud)

Sube tu repositorio a GitHub

Entra a: https://share.streamlit.io

Conecta tu GitHub

Selecciona tu repositorio

En “Main file path”, selecciona: streamlit_app.py

Verifica que requirements.txt esté en la raíz

Haz clic en Deploy

🎉 ¡Tu app queda disponible para cualquier persona!

📌 Dependencias del proyecto
Librería	Uso
pandas	Manejo de datos
numpy	Cálculo numérico
scikit-learn	Modelo RandomForest, train/test, métricas
matplotlib / seaborn	Gráficos
streamlit	Plataforma web
🎯 Objetivo del Modelo

Identificar clientes de alto valor usando:

Cantidad de productos comprados

Precio unitario

Total gastado

Ticket promedio

Razón precio/cantidad

El modelo genera una predicción binaria:
1 = cliente de alto valor.

🧠 Archivos importantes
✔ streamlit_app.py

Incluye:

Carga del dataset

Preprocesamiento

Entrenamiento automático

Gráficos (ROC, PR, Confusión)

Listado de clientes de alto valor

✔ modelo_colab.ipynb

Incluye:

Análisis exploratorio

Limpieza

Feature engineering

Modelado

Evaluación

Conclusiones

📈 Resultados del modelo (según el Notebook)

Los resultados pueden variar al usar otro dataset, pero típicamente:

Accuracy: ~0.80 - 0.92

ROC-AUC: ~0.85 - 0.95

PR-AUC: Alto debido al balance del dataset

El modelo logra:

Distinguir clientes que compran más artículos

Identificar quienes gastan más

Detectar tickets promedio más altos

📘 Conclusión

Este proyecto implementa una plataforma completa que combina:

Minería de datos

Machine Learning

Visualizaciones clave

Aplicación web funcional

Permitiendo que cualquier empresa de retail/e-commerce identifique clientes de alto valor y diseñe estrategias comerciales basadas en datos.

<div align="center">
⭐ Si este proyecto te sirvió, ¡dale una estrella en GitHub!
</div> ```
Conclusiones
