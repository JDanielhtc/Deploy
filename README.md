Descripción del Proyecto

Este proyecto implementa un modelo de Machine Learning (RandomForest) para clasificar clientes en alto valor o bajo valor, basándose en su comportamiento de compra.
Además, incluye una aplicación web funcional en Streamlit, que permite:

Subir el dataset

Entrenar el modelo directamente

Visualizar gráficos (ROC, PR, matriz de confusión)

Identificar clientes de alto valor

Simular acciones comerciales (ofertas/fidelización)

📂 Estructura del Repositorio
/Proyecto_Mineria_U2
│
├── streamlit_app.py       # Código de la aplicación web
├── requirements.txt       # Dependencias para ejecutar el proyecto
├── modelo_colab.ipynb     # Notebook con el entrenamiento completo del modelo
├── datakggle1.csv         # Dataset usado (si decides incluirlo)
└── README.md              # Este archivo

📥 Dataset utilizado

El proyecto consume un dataset proveniente de Kaggle:

Versión procesada cargada desde GitHub RAW:

https://raw.githubusercontent.com/JDanielhtc/Proyecto_Mineria/refs/heads/main/datakggle1.csv

▶ Cómo ejecutar el proyecto en local

Sigue estos pasos para correr la aplicación Streamlit en tu PC o laptop:

1️⃣ Clonar el repositorio
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd TU_REPO

2️⃣ Crear un entorno virtual (opcional pero recomendado)
En Windows:
python -m venv venv
venv\Scripts\activate

En Mac/Linux:
python3 -m venv venv
source venv/bin/activate

3️⃣ Instalar dependencias
pip install -r requirements.txt


El archivo requirements.txt contiene:

streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn

4️⃣ Ejecutar la aplicación web
streamlit run streamlit_app.py


Esto abrirá automáticamente tu navegador en:

http://localhost:8501

☁ Cómo desplegar la aplicación en la nube (Streamlit Cloud)

Sube tu repositorio completo a GitHub

Entra a:
👉 https://share.streamlit.io

Conéctalo con tu cuenta de GitHub

Selecciona tu repositorio

Elige el archivo de entrada:

streamlit_app.py


Asegúrate que requirements.txt esté en la raíz del repo

Haz clic en Deploy

🎉 Listo! Tu plataforma web queda online y se puede usar desde cualquier dispositivo.

📌 Dependencias clave del proyecto
Librería	Uso
pandas	Manejo de datos
numpy	Operaciones numéricas
scikit-learn	Modelo RandomForest, métricas
matplotlib / seaborn	Visualización de gráficos
streamlit	App web interactiva
🎯 Objetivo del Modelo

Identificar clientes de alto valor basándose en:

Monto total gastado

Ticket promedio

Cantidad de productos adquiridos

Precio unitario

Relación entre cantidad y precio

🧠 Archivos importantes
✔ streamlit_app.py

Contiene la aplicación web funcional:

Carga del dataset

Preprocesamiento automático

Entrenamiento del modelo

Visualización de gráficos

Identificación de clientes de alto valor

✔ modelo_colab.ipynb

Notebook con:

Análisis

Limpieza

Feature engineering

Entrenamiento

Resultados

Conclusiones
