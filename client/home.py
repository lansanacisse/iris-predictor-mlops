import streamlit as st

def home_page():
    st.title("Iris Species Predictor")
    st.markdown("""
    Welcome to this web app, designed to predict the species of an iris flower based on its sepal and petal dimensions.

    To get started:
    1. **Training**: Train the model using the 'Training Models' tab.
    2. **Predict**: Input dimensions in the 'Predict' tab to get predictions.
    3. **Metrics**: Evaluate the model's performance in the 'Metrics' tab.
    """)

    # Embed the new Giphy URL
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://media.giphy.com/media/iClT0Y7dwF4NfbVCNX/giphy.gif" alt="Iris Animation" width="600">
        </div>
        """,
        unsafe_allow_html=True,
    )
