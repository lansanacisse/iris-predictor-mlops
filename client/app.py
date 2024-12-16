import streamlit as st
import requests

# Configuration de la page
st.set_page_config(
    page_title="Prédiction des fleurs d'Iris",
    page_icon="🌸",  
    layout="centered",
    initial_sidebar_state="auto",
)
# Titre de l'application
st.title("Prédiction des fleurs d'Iris avec Animations 🌸")

# Correspondance entre les classes et les noms des fleurs
CLASS_NAMES = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

# Liens vers des images pour chaque type de fleur
CLASS_IMAGES = {
    0: "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",  # Image Iris-setosa
    1: "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",  # Image Iris-versicolor
    2: "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"  # Image Iris-virginica
}


# Entrées utilisateur
st.sidebar.header("Entrées utilisateur")
sepal_length = st.sidebar.number_input("Longueur du sépale (cm)", min_value=0.0, format="%.2f")
sepal_width = st.sidebar.number_input("Largeur du sépale (cm)", min_value=0.0, format="%.2f")
petal_length = st.sidebar.number_input("Longueur du pétale (cm)", min_value=0.0, format="%.2f")
petal_width = st.sidebar.number_input("Largeur du pétale (cm)", min_value=0.0, format="%.2f")

# Bouton de prédiction
if st.sidebar.button("Prédire"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    
    try:
        # Envoi de la requête POST au serveur FastAPI
        response = requests.post("http://server:8000/predict", json={"features": features})
        
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            flower_name = CLASS_NAMES.get(prediction, "Inconnu")
            image_url = CLASS_IMAGES.get(prediction, None)
            
            # Affichage du résultat
            st.success(f"La fleur prédite est : **{flower_name}** 🌸")
            
            # Affichage de l'image correspondante
            if image_url:
                st.image(image_url, caption=flower_name, use_container_width=True)
            
        else:
            st.error("Erreur lors de la prédiction. Veuillez réessayer.")
    except Exception as e:
        st.error(f"Impossible de se connecter au serveur : {e}")

# Ajout d'un pied de page
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    <div class="footer">
        <p style="text-align: center;">Développé par <strong>Lansana CISSE M2 SISE</strong></p>
    </div>
    """,
    unsafe_allow_html=True
)


