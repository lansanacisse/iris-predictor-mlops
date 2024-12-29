import os
import pickle
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Créer le dossier pour sauvegarder les modèles
def create_models_dir():
    models_dir = os.path.join(os.path.dirname(__file__), "models")
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    return models_dir

# Charger un jeu de données
def load_dataset(file_path):
    # Convertir le chemin en chemin absolu
    abs_path = os.path.abspath(file_path)
    
    if not os.path.exists(abs_path):
        st.error(f"Le fichier {abs_path} n'existe pas.")
        return None
    
    data = pd.read_csv(abs_path)
    return data

# Entraîner le modèle
def train_model(algorithm, X_train, y_train, params):
    if algorithm == "Random Forest":
        model = RandomForestClassifier(**params)
    elif algorithm == "SVM":
        model = SVC(**params, probability=True)
    elif algorithm == "Decision Tree":
        model = DecisionTreeClassifier(**params)
    elif algorithm == "XGBoost":
        model = XGBClassifier(**params, use_label_encoder=False, eval_metric="logloss")
    else:
        st.error("Algorithme non supporté.")
        return None

    model.fit(X_train, y_train)
    return model

# Sauvegarder le modèle
def save_model(model, algorithm_name, models_dir):
    model_path = os.path.join(models_dir, f"{algorithm_name}_model.pkl")
    with open(model_path, "wb") as file:
        pickle.dump(model, file)
    return model_path

# Interface utilisateur pour configurer l'entraînement
def training_page():
    st.title("Entraînement de Modèles")

    # Utilisez un chemin absolu basé sur Docker
    dataset_path = "/app/data/Iris.csv"
    data = load_dataset(dataset_path)

    if data is not None:
        st.write("Aperçu des données :", data.head())

        # Sélectionner la colonne cible et les colonnes des caractéristiques
        target_column = st.selectbox("Colonne cible", data.columns)
        feature_columns = st.multiselect("Colonnes des caractéristiques", [col for col in data.columns if col != target_column])

        if target_column and feature_columns:
            X = data[feature_columns]
            y = data[target_column]

            # Encodage des classes cibles pour XGBoost
            label_encoder = LabelEncoder()
            y = label_encoder.fit_transform(y)

            # Diviser les données
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Sélectionner un algorithme
            algorithm = st.selectbox(
                "Choisissez un algorithme",
                ["Random Forest", "SVM", "Decision Tree", "XGBoost"]
            )

            # Configuration des hyperparamètres dans le formulaire principal
            params = {}
            if algorithm == "Random Forest":
                st.subheader("Hyperparamètres pour Random Forest")
                params["n_estimators"] = st.slider("Nombre d'estimateurs", 10, 500, 100)
                params["max_depth"] = st.slider("Profondeur max", 1, 20, 5)
            elif algorithm == "SVM":
                st.subheader("Hyperparamètres pour SVM")
                params["C"] = st.slider("C (Regularisation)", 0.01, 10.0, 1.0)
                params["kernel"] = st.selectbox("Kernel", ["linear", "rbf", "poly"])
            elif algorithm == "Decision Tree":
                st.subheader("Hyperparamètres pour Decision Tree")
                params["max_depth"] = st.slider("Profondeur max", 1, 20, 5)
            elif algorithm == "XGBoost":
                st.subheader("Hyperparamètres pour XGBoost")
                params["learning_rate"] = st.slider("Taux d'apprentissage", 0.01, 0.5, 0.1)
                params["n_estimators"] = st.slider("Nombre d'estimateurs", 10, 500, 100)

            # Bouton pour entraîner le modèle
            if st.button("Entraîner le modèle"):
                model = train_model(algorithm, X_train, y_train, params)

                if model:
                    # Sauvegarder le modèle
                    models_dir = create_models_dir()
                    model_path = save_model(model, algorithm.replace(" ", "_"), models_dir)

                    # Évaluer le modèle
                    y_pred = model.predict(X_test)
                    accuracy = accuracy_score(y_test, y_pred)

                    st.success(f"Modèle entraîné avec succès et sauvegardé dans le dossier Models.")
                else:
                    st.error("L'entraînement du modèle a échoué.")
