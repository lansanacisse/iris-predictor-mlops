import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import pickle
import os

# Function to load a model
def load_model(model_name):
    """Loads a specific model from the models folder."""
    model_dir = "/app/server/models"  # Absolute path in Docker
    model_path = os.path.join(model_dir, model_name)

    if not os.path.exists(model_path):
        st.error(f"The model file '{model_name}' does not exist.")
        return None

    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

# Function to load data
def load_data(file_path):
    """
    Loads data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        tuple: (X, y, feature_names) where
               - X is a DataFrame of features,
               - y is a series or array of labels,
               - feature_names is a list of feature column names.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Load the CSV file
    data = pd.read_csv(file_path)

    # Extract features and labels
    X = data.iloc[:, :-1]  # All columns except the last for features
    y = data.iloc[:, -1]   # The last column for labels
    feature_names = list(X.columns)  # Names of the feature columns

    return X, y, feature_names

# Function to plot class probability curves
def plot_class_curves(model, X, y, feature_names):
    st.subheader("Class Probability Curves")

    if not hasattr(model, "predict_proba"):
        st.error("The selected model does not support `predict_proba`.")
        return

    y_proba = model.predict_proba(X)
    fig, ax = plt.subplots()
    for i in range(y_proba.shape[1]):  # Based on available classes
        ax.plot(y_proba[:, i], label=f"Class {i}")

    plt.title("Predicted Probability Curves")
    plt.xlabel("Samples")
    plt.ylabel("Probability")
    plt.legend()
    st.pyplot(fig)

# Function to display accuracy
def display_accuracy(y, y_pred):
    st.subheader("Accuracy")
    accuracy = accuracy_score(y, y_pred)
    st.metric(label="Accuracy", value=f"{accuracy:.2f}")

# Function to display the classification report
def display_classification_report(y, y_pred):
    st.subheader("Classification Report")
    report = classification_report(y, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    try:
        st.table(report_df.style.format("{:.2f}").background_gradient(cmap="coolwarm"))
    except Exception as e:
        st.error(f"Error displaying the report: {e}")

# Function to display the confusion matrix
def display_confusion_matrix(y, y_pred):
    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=sorted(set(y)), yticklabels=sorted(set(y)))
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    st.pyplot(fig)

# Main function
def show_metrics():
    st.title("Model Metrics")

    # Path to the CSV file
    csv_path = "/app/data/Iris.csv"

    # Load data
    try:
        X, y, feature_names = load_data(csv_path)
    except FileNotFoundError as e:
        st.error(e)
        return

    # Allow the user to select a model
    model_name = st.selectbox(
        "Select the model to evaluate",
        ["Random_Forest_model.pkl", "SVM_model.pkl", "Decision_Tree_model.pkl", "XGBoost_model.pkl"]
    )

    # Load the selected model
    model = load_model(model_name)
    if model is None:
        st.error("Unable to load the selected model.")
        return

    # Make predictions
    y_pred = model.predict(X)

    # Display metrics
    display_accuracy(y, y_pred)
    display_classification_report(y, y_pred)
    display_confusion_matrix(y, y_pred)
    plot_class_curves(model, X, y, feature_names)
