import streamlit as st
import requests
import numpy as np
import os
import sys
import importlib
from datetime import datetime  # Import pour l'année

# Ajouter dynamiquement le chemin vers le dossier `server`
server_path = os.path.join(os.path.dirname(__file__), "server")
if server_path not in sys.path:
    sys.path.append(server_path)

# Importer le module train
try:
    import train
except ModuleNotFoundError:
    raise ModuleNotFoundError(f"Impossible de trouver le module 'train'. Vérifiez que le chemin {server_path} est correct.")

importlib.reload(train)
from train import training_page
from metrics import show_metrics
from predict import predict_page
from metrics import show_metrics
from home import home_page

# Configuration de la page
st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸",
    layout="centered",
)

# Configuration des onglets
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🤖 Training Models", "🔮 Predict", "📊 Metrics"])

# Home Page
with tab1:
    home_page()

# Training Models Page
with tab2:
    training_page()

# Predict Page
with tab3:
    predict_page()

# Metrics Page
with tab4:
    show_metrics()
