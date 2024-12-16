import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸",  # Flower emoji
    layout="centered",
    initial_sidebar_state="expanded",
)

# Application title
st.title("🌸 Iris Flower Prediction 🌸")

# Mapping between class indices and flower names
CLASS_NAMES = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

# Links to images for each flower type
CLASS_IMAGES = {
    0: "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",  # Iris-setosa image
    1: "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",  # Iris-versicolor image
    2: "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"  # Iris-virginica image
}

# Adding a description
st.markdown(
    """Welcome to the Iris Flower Prediction app! ✨ 
    Enter the flower dimensions in the sidebar → and get an instant prediction along with a beautiful image. 💐
    """
)

# User inputs
st.sidebar.header("🎨 User Inputs")
sepal_length = st.sidebar.number_input(
    "Sepal Length (cm)", min_value=0.0, format="%.2f")
sepal_width = st.sidebar.number_input(
    "Sepal Width (cm)", min_value=0.0, format="%.2f")
petal_length = st.sidebar.number_input(
    "Petal Length (cm)", min_value=0.0, format="%.2f")
petal_width = st.sidebar.number_input(
    "Petal Width (cm)", min_value=0.0, format="%.2f")

# Prediction button
if st.sidebar.button("🔬 Predict"):
    features = [sepal_length, sepal_width, petal_length, petal_width]

    try:
        # Sending POST request to FastAPI server
        response = requests.post("http://server:8000/predict", json={"features": features})

        if response.status_code == 200:
            prediction = response.json()["prediction"]
            flower_name = CLASS_NAMES.get(prediction, "Unknown")
            image_url = CLASS_IMAGES.get(prediction, None)

            # Displaying the result
            st.success(f"The predicted flower is: **{flower_name}** 🌸")

            # Displaying the corresponding image
            if image_url:
                st.image(image_url, caption=f"Here is an {flower_name}! 🌿", use_container_width=True)

        else:
            st.error("⚠️ Error during prediction. Please try again.")
    except Exception as e:
        st.error(f"🚫 Unable to connect to the server: {e}")

# Adding a footer
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
    unsafe_allow_html=True
)