import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import pickle
from sklearn.datasets import load_iris

def show_metrics():
    st.title("📊 Métriques du Modèle Iris")
    
    # Permettre à l'utilisateur de spécifier le chemin du fichier
    pkl_path = st.text_input("Chemin du fichier modèle (model.pkl)", "model.pkl")
    
    # Charger le jeu de données Iris
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target
    
    try:
        # Charger le fichier .pkl
        with open(pkl_path, "rb") as file:
            model = pickle.load(file)
            st.success(f"✅ Fichier 'model.pkl' chargé avec succès depuis : {pkl_path}")
        
        # Vérifier si le modèle peut prédire
        if not hasattr(model, "predict"):
            st.error("❌ Le modèle chargé ne semble pas compatible avec la méthode 'predict'.")
            return
        
        # Faire des prédictions
        y_pred = model.predict(X)
        
        # Afficher les vraies étiquettes vs étiquettes prédites
        st.subheader("Vraies étiquettes vs Étiquettes prédites")
        data_frame = pd.DataFrame({"Vraies Étiquettes": y, "Étiquettes Prédites": y_pred})
        st.dataframe(data_frame)

        # Calculer et afficher la précision
        st.subheader("Précision")
        accuracy = accuracy_score(y, y_pred)
        st.metric(label="Précision", value=f"{accuracy:.2f}")

        # Afficher le rapport de classification
        st.subheader("Rapport de Classification")
        report = classification_report(y, y_pred, target_names=iris.target_names, output_dict=True)
        report_df = pd.DataFrame(report).transpose()
        st.table(report_df.style.format("{:.2f}").background_gradient(cmap="coolwarm", subset=pd.IndexSlice[:-1, :-1]))

        # Matrice de confusion
        st.subheader("Matrice de Confusion")
        cm = confusion_matrix(y, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
        plt.ylabel("Réel")
        plt.xlabel("Prédit")
        st.pyplot(fig)

        # Distribution des prédictions
        st.subheader("Distribution des Prédictions")
        fig, ax = plt.subplots()
        sns.countplot(x=y_pred, order=[0, 1, 2])
        plt.title("Distribution des Classes Prédites")
        plt.xlabel("Étiquettes Prédites")
        plt.ylabel("Nombre")
        plt.xticks(ticks=[0, 1, 2], labels=iris.target_names, rotation=45)
        st.pyplot(fig)
        