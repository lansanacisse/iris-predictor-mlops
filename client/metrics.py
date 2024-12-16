import streamlit as st
import requests

# Configuration de la page
st.set_page_config(page_title="Métriques du Modèle", layout="wide")

# Titre de la page
st.title("🔍 Métriques du Modèle")

# Récupérer les métriques depuis l'API
try:
    response = requests.get("http://server:5000/metrics")
    if response.status_code == 200:
        metrics = response.json()
        
        # Afficher les métriques
        st.write("### 📊 Métriques")
        for key, value in metrics.items():
            st.metric(label=key.capitalize(), value=value)
    else:
        st.error("Impossible de récupérer les métriques depuis le serveur.")
except Exception as e:
    st.error(f"Erreur: {e}")
