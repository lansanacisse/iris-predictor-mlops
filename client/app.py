import streamlit as st
import requests
import numpy as np
from metrics import show_metrics  # Import the show_metrics function from metrics.py

# Page configuration
st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸",
    layout="centered",
)

# Onglets pour la navigation
tab1, tab2 = st.tabs(["🏠 Home", "📊 Metrics"])

# Contenu de l'onglet Home
with tab1:
    st.title("🌸 Iris Flower Prediction 🌸")

    st.markdown(
        """
        Welcome to the **Iris Flower Prediction** app! ✨  
        Fill in the flower's dimensions below to get a prediction and see its image! 🌼
        """
    )

    # Input form for user
    with st.form(key="input_form"):
        st.subheader("Enter the Flower Dimensions")
        sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, format="%.2f")
        sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, format="%.2f")
        petal_length = st.number_input("Petal Length (cm)", min_value=0.0, format="%.2f")
        petal_width = st.number_input("Petal Width (cm)", min_value=0.0, format="%.2f")
        submit_button = st.form_submit_button(label="🔬 Predict")

    # Class names and corresponding images
    CLASS_NAMES = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}
    CLASS_IMAGES = {
        0: "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",
        1: "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
        2: "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg",
    }

    # Prediction logic
    if submit_button:
        features = [sepal_length, sepal_width, petal_length, petal_width]
        try:
            response = requests.post("http://server:8000/predict", json={"features": features})
            if response.status_code == 200:
                prediction = response.json()["prediction"]
                flower_name = CLASS_NAMES.get(prediction, "Unknown")
                image_url = CLASS_IMAGES.get(prediction, None)
                st.success(f"🌷 The predicted flower is: **{flower_name}** 🌿")

                if image_url:
                    st.image(image_url, caption=f"Here is an {flower_name}!", use_container_width=True)
            else:
                st.error("⚠️ Error during prediction. Please try again.")
        except Exception as e:
            st.error(f"🚫 Unable to connect to the server: {e}")

# Contenu de l'onglet Metrics
with tab2:
    show_metrics()
