from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
import pickle
import numpy as np

# Initialisation FastAPI
app = FastAPI()

# Charger les modèles
models = {}
try:
    models = {
        "random_forest": pickle.load(open("models/Random_Forest_model.pkl", "rb")),
        "svm": pickle.load(open("models/SVM_model.pkl", "rb")),
        "decision_tree": pickle.load(open("models/Decision_Tree_model.pkl", "rb")),
        "xgboost": pickle.load(open("models/XGBoost_model.pkl", "rb")),
    }
    print("✅ Models loaded successfully:", models.keys())
except FileNotFoundError as e:
    print(f"⚠️ Model file not found: {e}")

# Connexion à MongoDB
try:
    client = MongoClient("mongodb://mongo:27017/")
    db = client["mlops_db"]
    collection = db["predictions"]
except Exception as e:
    print(f"🚫 Unable to connect to MongoDB: {e}")

# Schéma des données d'entrée
class PredictionRequest(BaseModel):
    features: list[float]
    model: str

# Endpoint de prédiction
@app.post("/predict")
async def predict(data: PredictionRequest):
    # Vérifier si le modèle existe
    model_key = data.model
    print(f"🔍 Received model: {model_key}")
    if model_key not in models:
        raise HTTPException(status_code=400, detail=f"Model '{data.model}' not found.")

    # Préparer les données pour la prédiction
    try:
        features = np.array(data.features).reshape(1, -1)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input features: {e}")

    # Effectuer la prédiction
    model = models[model_key]
    prediction = int(model.predict(features)[0])

    # Sauvegarder la prédiction dans MongoDB
    try:
        record = {"features": data.features, "prediction": prediction, "model": data.model}
        collection.insert_one(record)
    except Exception as e:
        print(f"⚠️ Warning: Unable to save prediction to MongoDB: {e}")

    return {"prediction": prediction, "model_used": data.model}

# Endpoint pour récupérer toutes les prédictions sauvegardées
@app.get("/predictions")
def get_predictions():
    try:
        predictions = list(collection.find({}, {"_id": 0}))  # Ne pas inclure l'ID MongoDB
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unable to fetch predictions: {e}")

# Endpoint pour supprimer toutes les prédictions sauvegardées
@app.delete("/predictions")
def delete_predictions():
    try:
        result = collection.delete_many({})
        return {"deleted_count": result.deleted_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unable to delete predictions: {e}")

# Racine de l'API
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API FastAPI pour la prédiction Iris"}
