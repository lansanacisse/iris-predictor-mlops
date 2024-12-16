# MLOps - Projet de Prédiction des Fleurs d'Iris 🌸

## **Description**
Ce projet est une application Web dockerisée permettant de prédire la classe des fleurs d'Iris (**Iris-setosa**, **Iris-versicolor**, **Iris-virginica**) grâce à un modèle de **Machine Learning** pré-entraîné. Il utilise **FastAPI** comme API backend, **MongoDB** pour stocker les prédictions, et **Streamlit** pour l'interface utilisateur.

---

## **Technologies Utilisées**
- **FastAPI** : Pour l'API REST.
- **MongoDB** : Base de données pour stocker les prédictions.
- **Streamlit** : Interface utilisateur.
- **Docker & Docker Compose** : Orchestration des services.
- **Scikit-learn** : Entraînment du modèle de Machine Learning.

---

## **Architecture du Projet**

```
mlops-td/
├── client/             
│   ├── app.py             # Interface utilisateur Streamlit
│   ├── requirements.txt   # Dépendances pour Streamlit
│   └── Dockerfile         # Image Docker pour le client
│
├── server/
│   ├── app.py             # API FastAPI
│   ├── train.py           # Entraînment du modèle
│   ├── model.pkl          # Modèle pré-entraîné
│   ├── requirements.txt   # Dépendances pour FastAPI
│   └── Dockerfile         # Image Docker pour le serveur
│               
│── docker-compose.yml # Orchestration des conteneurs
│
└── README.md              # Documentation
```

---

## **Prérequis**

Assurez-vous que les éléments suivants sont installés :
- **Docker** : [Instructions d'installation](https://docs.docker.com/get-docker/)
- **Docker Compose** : [Instructions d'installation](https://docs.docker.com/compose/install/)
- **Python 3.9** (optionnel, pour des tests locaux)

---

## **Installation et Déploiement**

### **1. Cloner le projet**
```bash
git clone <URL_DU_REPO>
cd mlops-td
```

### **2. Construire et Lancer les Conteneurs**
Utilisez **Docker Compose** pour démarrer les services :
```bash
docker-compose up --build
```

### **3. Accéder aux Services**
- **Interface utilisateur Streamlit** : [http://localhost:8501](http://localhost:8501)
- **API FastAPI (Swagger)** : [http://localhost:8000/docs](http://localhost:8000/docs)
- **MongoDB** : Exposé sur le port `27017`.

---

## **Fonctionnement du Projet**

### **1. Entraînement du Modèle**
Le modèle de classification est entraîné sur le jeu de données **Iris** avec Scikit-learn. Il est sauvegardé sous la forme d'un fichier `model.pkl` dans le dossier `server/`.

### **2. API FastAPI**
- L'API expose une route **POST /predict** qui accepte les caractéristiques de la fleur pour prédire sa classe.
- La prédiction est sauvegardée dans MongoDB.

**Exemple de Requête POST** :
```json
{"features": [5.1, 3.5, 1.4, 0.2]}
```

**Réponse** :
```json
{"prediction": "Iris-setosa"}
```

### **3. Interface Streamlit**
L'utilisateur peut :
- Saisir les caractéristiques de la fleur (longueur et largeur des sépales/pétales).
- Obtenir une prédiction avec le **nom de la fleur** et une **animation** associée.

---

## **Exemple d'Utilisation**

1. Ouvre l'interface Streamlit ([http://localhost:8501](http://localhost:8501)).
2. Remplis les champs avec les valeurs des caractéristiques :
   - **Longueur du sépale** : 5.1
   - **Largeur du sépale** : 3.5
   - **Longueur du pétale** : 1.4
   - **Largeur du pétale** : 0.2
3. Clique sur **"Prédire"**.
4. Le nom de la fleur et une animation correspondante apparaissent.

---

## **Commandes Utiles**

### **1. Vérifier les Conteneurs**
```bash
docker ps
```

### **2. Arrêter et Nettoyer les Conteneurs**
```bash
docker-compose down --volumes
```

### **3. Consulter les Données dans MongoDB**
Depuis le terminal :
```bash
docker exec -it mongodb mongo
use mlops_db
db.predictions.find()
```

---

## **Déploiement Local du Script d'Entraînement**

Tu peux exécuter `train.py` localement pour générer un modèle :
```bash
cd server
python train.py
```

---

## **Conclusion**

Ce projet met en œuvre un pipeline complet MLOps avec :
1. Un **modèle de Machine Learning** pour la classification.
2. Une **API FastAPI** pour servir le modèle.
3. Une **base de données MongoDB** pour stocker les prédictions.
4. Une **interface Streamlit** pour l'utilisateur.

---

## **Améliorations Possibles**
- Ajouter une authentification pour l'API.
- Ajouter des graphiques interactifs pour l'analyse des prédictions.

---

## **Contact**
Pour toute question, n'hésite pas à me contacter via [ton email ou réseau social].

---

🎉 **Prêt à utiliser ? Lance simplement :**
```bash
docker-compose up --build
