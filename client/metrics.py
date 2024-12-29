import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import pickle
import os

# Fonction pour charger un modèle
def load_model(model_name):
    """Charge un modèle spécifique depuis le dossier des modèles."""
    model_dir = "/app/server/models"  # Chemin absolu dans Docker
    model_path = os.path.join(model_dir, model_name)

    if not os.path.exists(model_path):
        st.error(f"Le fichier modèle '{model_name}' n'existe pas.")
        return None

    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

# Fonction pour charger les données
def load_data(file_path):
    """
    Charge les données à partir d'un fichier CSV.

    Args:
        file_path (str): Chemin du fichier CSV.

    Returns:
        tuple: (X, y, feature_names) où
               - X est un DataFrame des caractéristiques,
               - y est une série ou un tableau des étiquettes,
               - feature_names est une liste des noms des colonnes caractéristiques.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")

    # Charger le fichier CSV
    data = pd.read_csv(file_path)

    # Extraire les caractéristiques et les étiquettes
    X = data.iloc[:, :-1]  # Toutes les colonnes sauf la dernière pour les caractéristiques
    y = data.iloc[:, -1]   # La dernière colonne pour les étiquettes
    feature_names = list(X.columns)  # Les noms des colonnes caractéristiques

    return X, y, feature_names

# Fonction pour tracer les courbes des probabilités
def plot_class_curves(model, X, y, feature_names):
    st.subheader("Courbes des Probabilités pour les Classes")

    if not hasattr(model, "predict_proba"):
        st.error("Le modèle sélectionné ne supporte pas `predict_proba`.")
        return

    y_proba = model.predict_proba(X)
    fig, ax = plt.subplots()
    for i in range(y_proba.shape[1]):  # Basé sur les classes disponibles
        ax.plot(y_proba[:, i], label=f"Classe {i}")

    plt.title("Courbes des Probabilités Prédites")
    plt.xlabel("Échantillons")
    plt.ylabel("Probabilité")
    plt.legend()
    st.pyplot(fig)

# Fonction pour afficher la précision
def display_accuracy(y, y_pred):
    st.subheader("Précision")
    accuracy = accuracy_score(y, y_pred)
    st.metric(label="Precision",value=f"{accuracy:.2f}")

# Fonction pour afficher le rapport de classification
def display_classification_report(y, y_pred):
    st.subheader("Rapport de Classification")
    report = classification_report(y, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    try:
        st.table(report_df.style.format("{:.2f}").background_gradient(cmap="coolwarm"))
    except Exception as e:
        st.error(f"Erreur lors de l'affichage du rapport : {e}")

# Fonction pour afficher la matrice de confusion
def display_confusion_matrix(y, y_pred):
    st.subheader("Matrice de Confusion")
    cm = confusion_matrix(y, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=sorted(set(y)), yticklabels=sorted(set(y)))
    plt.ylabel("Réel")
    plt.xlabel("Prédit")
    st.pyplot(fig)

# Fonction principale
def show_metrics():
    st.title("Métriques du Modèle")

    # Chemin du fichier CSV
    csv_path = "/app/data/Iris.csv"


    # Charger les données
    try:
        X, y, feature_names = load_data(csv_path)
    except FileNotFoundError as e:
        st.error(e)
        return

    # Permettre à l'utilisateur de choisir le modèle
    model_name = st.selectbox(
        "Sélectionnez le modèle à évaluer",
        ["Random_Forest_model.pkl", "SVM_model.pkl", "Decision_Tree_model.pkl", "XGBoost_model.pkl"]
    )

    # Charger le modèle sélectionné
    model = load_model(model_name)
    if model is None:
        st.error("Impossible de charger le modèle sélectionné.")
        return

    # Faire des prédictions
    y_pred = model.predict(X)

    # Afficher les métriques
    display_accuracy(y, y_pred)
    display_classification_report(y, y_pred)
    display_confusion_matrix(y, y_pred)
    plot_class_curves(model, X, y, feature_names)
