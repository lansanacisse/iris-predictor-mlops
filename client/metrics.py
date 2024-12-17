import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns

def show_metrics():
    st.title("📊 Model Metrics")
    
    # Example data for demonstration
    y_true = [0, 1, 2, 1, 0, 2, 1, 0, 2, 2]
    y_pred = [0, 1, 2, 1, 0, 2, 2, 0, 1, 2]

    # Accuracy
    accuracy = accuracy_score(y_true, y_pred)
    st.write(f"**Accuracy:** {accuracy:.2f}")

    # Classification Report
    st.subheader("Classification Report")
    report = classification_report(y_true, y_pred, target_names=["Iris-setosa", "Iris-versicolor", "Iris-virginica"], output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    st.dataframe(report_df)

    # Confusion Matrix
    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Iris-setosa", "Iris-versicolor", "Iris-virginica"], yticklabels=["Iris-setosa", "Iris-versicolor", "Iris-virginica"])
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    st.pyplot(fig)

    # Prediction Distribution
    st.subheader("Prediction Distribution")
    pred_df = pd.DataFrame({"True Labels": y_true, "Predicted Labels": y_pred})
    fig, ax = plt.subplots()
    sns.countplot(data=pred_df, x="Predicted Labels", order=[0, 1, 2])
    plt.title("Distribution of Predicted Classes")
    st.pyplot(fig)
