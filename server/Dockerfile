FROM python:3.9-slim

WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers
COPY . .

# Exposer le port pour FastAPI
EXPOSE 8000

# Commande pour démarrer le serveur
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
