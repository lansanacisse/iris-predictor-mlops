from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import pickle
import numpy as np

# Initialisation FastAPI
app = FastAPI()

# Charger le modèle
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Connexion à MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["mlops_db"]
collection = db["predictions"]

# Schéma des données d'entrée
class Features(BaseModel):
    features: list[float]

# Endpoint de prédiction
@app.post("/predict")
async def predict(data: Features):
    features = np.array(data.features).reshape(1, -1)
    prediction = int(model.predict(features)[0])
    
    # Sauvegarder la prédiction dans MongoDB
    record = {"features": data.features, "prediction": prediction}
    collection.insert_one(record)

    return {"prediction": prediction}

# Racine de l'API
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API FastAPI pour la prédiction Iris"}
