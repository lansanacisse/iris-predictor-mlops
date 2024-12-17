import streamlit as st
import requests
from metrics import show_metrics # Import the show_metrics function from metrics.py

# Page configuration
st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Metrics"])

# Class names and corresponding images
CLASS_NAMES = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}
CLASS_IMAGES = {
    0: "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",
    1: "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
    2: "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg",
}

# Home page
if page == "Home":
    # Page title
    st.title("🌸 Iris Flower Prediction 🌸")

    st.markdown(
        """
        Welcome to the **Iris Flower Prediction** app! ✨  
        Fill in the flower's dimensions below to get a prediction and see its image! 💩
        """
    )

    # Input form for user
    with st.form(key='input_form'):
        st.subheader("Enter the Flower Dimensions")
        sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, format="%.2f")
        sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, format="%.2f")
        petal_length = st.number_input("Petal Length (cm)", min_value=0.0, format="%.2f")
        petal_width = st.number_input("Petal Width (cm)", min_value=0.0, format="%.2f")
        submit_button = st.form_submit_button(label="🔬 Predict")

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

    # Footer
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
            font-size: 14px;
        }
        </style>
        <div class="footer">
            📚 Developed by <strong>Lansana CISSE M2 SISE</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Metrics page
elif page == "Metrics":
    show_metrics()
