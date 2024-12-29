# Import libraries
import streamlit as st
import requests

def predict_page():
    # Title and Description
    st.title("Iris Flower Prediction")

    # Input form for user
    with st.form(key="input_form"):
        st.subheader("Enter the Flower Dimensions")
        sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, format="%.2f")
        sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, format="%.2f")
        petal_length = st.number_input("Petal Length (cm)", min_value=0.0, format="%.2f")
        petal_width = st.number_input("Petal Width (cm)", min_value=0.0, format="%.2f")

        # Dropdown to select model
        model_choice = st.selectbox(
            "Choose a Model for Prediction",
            ["Random Forest", "SVM", "Decision Tree", "XGBoost"]
        )
        
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

        # Validation: Vérifiez si toutes les valeurs sont à 0.0
        if all(value == 0.0 for value in features):
            st.error("⚠️ Please enter valid values for all flower dimensions!")
            return  # Arrête l'exécution si les valeurs sont invalides

        # Map the model choice to a model name for the backend API
        model_mapping = {
            "Random Forest": "random_forest",
            "SVM": "svm",
            "Decision Tree": "decision_tree",
            "XGBoost": "xgboost"
        }
        
        selected_model = model_mapping.get(model_choice)

        try:
            # Send the request to the server with the selected model
            response = requests.post(
                f"http://server:8000/predict", 
                json={"features": features, "model": selected_model}
            )
            
            if response.status_code == 200:
                result = response.json()
                prediction = result["prediction"]
                flower_name = CLASS_NAMES.get(prediction, "Unknown")
                image_url = CLASS_IMAGES.get(prediction, None)
                
                st.success(f"🌷 The predicted flower is: **{flower_name}** 🌿")
                if image_url:
                    st.image(image_url, caption=f"Here is an {flower_name}!", use_container_width=True)
            else:
                st.error(f"⚠️ Error during prediction: {response.json().get('detail', 'Unknown error')}")
        except Exception as e:
            st.error(f"🚫 Unable to connect to the server: {e}")
