FROM python:3.8-slim

# Installer les dépendances
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier le code de l'application
COPY app.py /app/app.py

# Définir le répertoire de travail
WORKDIR /app

# Commande pour démarrer l'application Streamlit
CMD ["streamlit", "run", "app.py"]