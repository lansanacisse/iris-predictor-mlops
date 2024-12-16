# MLOps - Iris Flower Prediction Project 🌸

## **Description**
This project is a Dockerized web application that predicts the class of Iris flowers (**Iris-setosa**, **Iris-versicolor**, **Iris-virginica**) using a pre-trained **Machine Learning** model. It leverages **FastAPI** for the backend API, **MongoDB** to store predictions, and **Streamlit** for the user interface.

---

## **Technologies Used**
- **FastAPI**: For the REST API.
- **MongoDB**: Database to store predictions.
- **Streamlit**: User interface.
- **Docker & Docker Compose**: Service orchestration.
- **Scikit-learn**: For training the Machine Learning model.

---

## **Project Architecture**

```
mlops-td/
├── client/             
│   ├── app.py             # Streamlit user interface
│   ├── requirements.txt   # Dependencies for Streamlit
│   └── Dockerfile         # Docker image for the client
│
├── server/
│   ├── app.py             # FastAPI backend
│   ├── train.py           # Model training script
│   ├── model.pkl          # Pre-trained model
│   ├── requirements.txt   # Dependencies for FastAPI
│   └── Dockerfile         # Docker image for the server
│               
│── docker-compose.yml # Container orchestration file
│
└── README.md              # Documentation
```

---

## **Prerequisites**

Ensure the following are installed:
- **Docker**: [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Installation Guide](https://docs.docker.com/compose/install/)
- **Python 3.9** (optional, for local testing)

---

## **Installation and Deployment**

### **1. Clone the Project**
```bash
git clone "https://github.com/lansanacisse/mlops-SISE"
cd mlops-SISE
```

### **2. Build and Launch the Containers**
Use **Docker Compose** to start the services:
```bash
docker-compose up --build
```

### **3. Access the Services**
- **Streamlit User Interface**: [http://localhost:8501](http://localhost:8501)
- **FastAPI (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **MongoDB**: Exposed on port `27017`.

---

## **How the Project Works**

### **1. Model Training**
The classification model is trained on the **Iris** dataset using Scikit-learn. It is saved as `model.pkl` in the `server/` folder.

### **2. FastAPI Backend**
- The API exposes a **POST /predict** route that accepts flower features to predict its class.
- Predictions are stored in MongoDB.

**Example POST Request**:
```json
{"features": [5.1, 3.5, 1.4, 0.2]}
```

**Response**:
```json
{"prediction": "Iris-setosa"}
```

### **3. Streamlit Interface**
Users can:
- Input flower features (sepal/petal length and width).
- Get predictions with the **flower name** and an associated **image**.

---

## **Usage Example**

1. Open the Streamlit interface ([http://localhost:8501](http://localhost:8501)).
2. Fill in the fields with the feature values:
   - **Sepal Length**: 5.1
   - **Sepal Width**: 3.5
   - **Petal Length**: 1.4
   - **Petal Width**: 0.2
3. Click **"Predict"**.
4. The flower name and a corresponding image will appear.

---

## **Useful Commands**

### **1. Check Running Containers**
```bash
docker ps
```

### **2. Stop and Clean Up Containers**
```bash
docker-compose down --volumes
```

### **3. View Data in MongoDB**
From the terminal:
```bash
docker exec -it mongodb mongo
use mlops_db
db.predictions.find()
```

---

## **Local Deployment of Training Script**

You can run `train.py` locally to generate a model:
```bash
cd server
python train.py
```

---

## **Contact**
For any questions, feel free to contact me through my profile: [Lansana CISSE](https://github.com/lansanacisse).

---

🎉 **Ready to use? Simply run:**
```bash
docker-compose up --build
```

