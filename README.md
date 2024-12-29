Voici un README mis à jour avec votre structure de projet récente :

---

# MLOps - Iris Flower Prediction Project 🌸

## **Description**
This project is a Dockerized web application designed to predict the class of Iris flowers (**Iris-setosa**, **Iris-versicolor**, **Iris-virginica**) using a pre-trained **Machine Learning** model. It integrates a **FastAPI** backend, **MongoDB** for persistence, and a user-friendly **Streamlit** interface for training, predicting, and analyzing model performance.

---

## **Key Features**
- 🛠 **Train Models**: Train models interactively using various algorithms (**Random Forest**, **SVM**, **Decision Tree**, and **XGBoost**) via the web interface.
- 🔮 **Predict Classes**: Predict the flower class using the trained models and visualize the predictions with images.
- 📊 **Analyze Performance**: View detailed metrics, including accuracy, confusion matrices, and classification reports.
- 🗄 **Store Predictions**: All predictions are saved in **MongoDB** for review and analysis.

---

## **Technologies Used**
- **FastAPI**: Backend for API endpoints.
- **MongoDB**: Database for storing predictions.
- **Streamlit**: User interface for training and predictions.
- **Docker & Docker Compose**: For containerization and orchestration.
- **Scikit-learn** and **XGBoost**: For Machine Learning models.

---

## **Project Structure**

```
mlops-SISE/
├── client/             
│   ├── app.py             # Main Streamlit app
│   ├── home.py            # Home page logic
│   ├── metrics.py         # Metrics visualization logic
│   ├── predict.py         # Prediction page logic
│   ├── requirements.txt   # Dependencies for Streamlit
│   └── Dockerfile         # Docker image for the client
│
├── server/
│   ├── app.py             # FastAPI backend
│   ├── train.py           # Model training script
│   ├── models/            # Folder to store trained models
│   │   ├── Random_Forest_model.pkl
│   │   ├── SVM_model.pkl
│   │   ├── Decision_Tree_model.pkl
│   │   └── XGBoost_model.pkl
│   ├── requirements.txt   # Dependencies for FastAPI
│   └── Dockerfile         # Docker image for the server
│
├── data/                  # Data folder (e.g., Iris.csv)
│
├── docker-compose.yml      # Container orchestration file
│
└── README.md               # Documentation
```

---

## **Prerequisites**

Make sure you have the following installed:
- **Docker**: [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Installation Guide](https://docs.docker.com/compose/install/)
- **Python 3.9+** (optional, for local testing)

---

## **Installation and Deployment**

### **1. Clone the Repository**
```bash
git clone https://github.com/lansanacisse/mlops-SISE.git
cd mlops-SISE
```

### **2. Build and Launch the Containers**
Use **Docker Compose** to start the services:
```bash
docker-compose up --build
```

### **3. Access the Application**
- **Streamlit User Interface**: [http://localhost:8501](http://localhost:8501)
- **FastAPI (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **MongoDB**: Exposed on port `27017`.

---

## **How the Project Works**

### **1. Training Models**
- Navigate to the **Training Models** tab in the Streamlit app.
- Select the target column and feature columns.
- Choose an algorithm (e.g., Random Forest, SVM, Decision Tree, or XGBoost).
- Configure hyperparameters and train the model.
- Models are saved in the `server/models` directory for future use.

### **2. Predicting Classes**
- Go to the **Predict** tab in Streamlit.
- Input flower dimensions (sepal length, sepal width, petal length, and petal width).
- Choose a pre-trained model and get predictions with visual feedback.

### **3. Viewing Metrics**
- Navigate to the **Metrics** tab.
- Visualize performance metrics, including:
  - Accuracy.
  - Confusion matrix.
  - Classification report.

---

## **Example Usage**

### **1. Train a Model**
1. Open the Streamlit app: [http://localhost:8501](http://localhost:8501)
2. Go to the **Training Models** tab.
3. Upload the dataset or use the default Iris dataset.
4. Choose the algorithm and configure hyperparameters.
5. Train the model and save it automatically in the `server/models` directory.

### **2. Make a Prediction**
1. Go to the **Predict** tab.
2. Enter the dimensions:
   - **Sepal Length**: 5.1
   - **Sepal Width**: 3.5
   - **Petal Length**: 1.4
   - **Petal Width**: 0.2
3. Choose a model (e.g., Random Forest) and click **Predict**.
4. The predicted flower class and an associated image will appear.

### **3. Compare Predictions**
Use the backend `/compare_models` endpoint to compare predictions from all models for the same input.

#### Example `curl` Command:
```bash
curl -X POST http://localhost:8000/compare_models \
-H "Content-Type: application/json" \
-d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

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
```bash
docker exec -it mongodb mongo
use mlops_db
db.predictions.find()
```

---

## **Local Testing of the Training Script**

You can run the training script locally to generate models:
```bash
cd server
python train.py
```

---

## **Contact**
For questions or feedback, feel free to reach out:

- **Lansana CISSE**
- **M2 SISE**
- **GitHub**: [Lansana CISSE](https://github.com/lansanacisse)

---

## **Ready to Start?**
Run the following command to get started:
```bash
docker-compose up --build
```

🎉 Enjoy exploring the power of MLOps with this Iris Flower Prediction Project! 🌸

--- 

### **Notes**
This README reflects your updated project structure. If further adjustments are needed, feel free to ask! 😊
