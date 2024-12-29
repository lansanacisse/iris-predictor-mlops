from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
import pickle
import numpy as np

# Initialize FastAPI
app = FastAPI()

# Load models
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

# Connect to MongoDB
try:
    client = MongoClient("mongodb://mongo:27017/")
    db = client["mlops_db"]
    collection = db["predictions"]
except Exception as e:
    print(f"🚫 Unable to connect to MongoDB: {e}")

# Schema for input data
class PredictionRequest(BaseModel):
    features: list[float]
    model: str

# Prediction endpoint
@app.post("/predict")
async def predict(data: PredictionRequest):
    # Check if the model exists
    model_key = data.model
    print(f"🔍 Received model: {model_key}")
    if model_key not in models:
        raise HTTPException(status_code=400, detail=f"Model '{data.model}' not found.")

    # Prepare the data for prediction
    try:
        features = np.array(data.features).reshape(1, -1)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input features: {e}")

    # Perform the prediction
    model = models[model_key]
    prediction = int(model.predict(features)[0])

    # Save the prediction to MongoDB
    try:
        record = {"features": data.features, "prediction": prediction, "model": data.model}
        collection.insert_one(record)
    except Exception as e:
        print(f"⚠️ Warning: Unable to save prediction to MongoDB: {e}")

    return {"prediction": prediction, "model_used": data.model}

# Endpoint to retrieve all saved predictions
@app.get("/predictions")
def get_predictions():
    try:
        predictions = list(collection.find({}, {"_id": 0}))  # Do not include MongoDB ID
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unable to fetch predictions: {e}")

# Endpoint to delete all saved predictions
@app.delete("/predictions")
def delete_predictions():
    try:
        result = collection.delete_many({})
        return {"deleted_count": result.deleted_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unable to delete predictions: {e}")

# API root
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Iris Prediction API"}
