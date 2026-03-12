# Financial Customer Churn Prediction – End-to-End MLOps Machine Learning Project

## Project Overview

Customer churn prediction is a critical problem in the financial services industry. Banks and financial institutions aim to identify customers who are likely to leave so that they can proactively implement retention strategies.

This project builds an **end-to-end Machine Learning pipeline** to predict whether a financial customer will churn based on demographic, behavioral, and account-related features. The project demonstrates a **production-grade ML workflow**, covering data exploration, feature engineering, model training, experiment tracking, containerization, and deployment.

The solution follows **industry best practices in Machine Learning Engineering and MLOps**, including modular project structure, logging, exception handling, experiment tracking with MLflow, and containerization using Docker.

The project is designed to reflect **real-world machine learning development workflows** typically used by ML engineers with several years of professional experience.

---

## Business Problem

Customer acquisition costs are significantly higher than customer retention costs. Predicting churn enables organizations to:

• Identify high-risk customers
• Launch targeted retention campaigns
• Reduce revenue loss
• Improve customer satisfaction

By using machine learning models trained on historical data, organizations can proactively detect churn risk.

---

## Dataset

The dataset used in this project is a **financial customer churn dataset** containing customer demographics, account information, and financial activity.

Typical features include:

• Credit Score
• Geography
• Gender
• Age
• Tenure
• Balance
• Number of Products
• Has Credit Card
• Is Active Member
• Estimated Salary

Target Variable:

`target`

• 1 → Customer churned
• 0 → Customer retained

---

## Project Architecture

The project follows a **modular and scalable ML project structure** commonly used in production environments.

```
financial-churn-mlops-project
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── notebook/
│   └── EDA_and_Preprocessing.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   ├── predict_pipeline.py
│   │
│   ├── utils/
│   │   ├── utils.py
│   │
│   ├── logger.py
│   ├── exception.py
│
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
├── .gitignore
├── README.md
```

---

## Key Features Implemented

### Exploratory Data Analysis (EDA)

The project includes an advanced EDA notebook that analyzes:

• Data distributions
• Target imbalance
• Correlation analysis
• Feature relationships with churn
• Outlier detection
• Business insights from data

The notebook also demonstrates feature engineering and preprocessing decisions used later in the pipeline.

---

### Data Preprocessing

The preprocessing pipeline includes:

• Missing value handling
• Categorical feature encoding
• Numerical feature scaling
• Feature selection
• Train-test splitting

Categorical features are converted into numerical form using **One-Hot Encoding**.

Numerical features are normalized using **StandardScaler**.

All preprocessing steps are combined using a **ColumnTransformer pipeline** and saved as a serialized object.

---

### Machine Learning Models

The following algorithms are evaluated:

• Logistic Regression
• Random Forest
• Gradient Boosting / XGBoost

Models are evaluated using metrics such as:

• Accuracy
• Precision
• Recall
• F1 Score
• ROC-AUC Score

The best performing model is selected and saved as a serialized model artifact.

---

### Model Serialization

The trained model and preprocessing pipeline are stored using **pickle**.

Saved artifacts:

```
artifacts/model.pkl
artifacts/preprocessor.pkl
```

These files are later used by the prediction pipeline for inference.

---

### Logging and Exception Handling

To simulate production-level code quality, the project includes:

Custom logging system
Custom exception handling

This helps track errors and maintain traceability across pipeline components.

---

### MLflow Experiment Tracking

MLflow is integrated for experiment tracking.

Tracked information includes:

• Model parameters
• Training metrics
• Experiment runs
• Model artifacts

This enables reproducible experimentation and model comparison.

---

### Docker Containerization

The application is containerized using Docker to ensure consistent deployment across environments.

The Docker container includes:

• Python runtime
• Required dependencies
• Trained ML model
• Flask application

This enables the application to run consistently across development, staging, and production environments.

---

### Prediction Pipeline

The prediction pipeline performs the following steps:

1. Load trained model
2. Load preprocessing pipeline
3. Transform new customer data
4. Generate churn predictions

The pipeline can be integrated with APIs or real-time applications.

---

## Technologies Used

Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn

MLflow
Docker

Flask

---

## How to Run the Project

### Step 1 — Clone the Repository

```
git clone https://github.com/yourusername/financial-churn-mlops-project.git
cd financial-churn-mlops-project
```

---

### Step 2 — Create Conda Environment

```
conda create -p venv python=3.10 -y
conda activate venv/
```

---

### Step 3 — Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 4 — Run Training Pipeline

```
python src/pipeline/train_pipeline.py
```

This step performs:

• Data ingestion
• Data preprocessing
• Model training
• Model evaluation
• Saving trained model artifacts

---

### Step 5 — Run MLflow UI

```
mlflow ui
```

Open browser:

```
http://localhost:5000
```

This allows viewing experiment runs and model metrics.

---

### Step 6 — Run Prediction API

```
python app.py
```

This starts a Flask server for predictions.

---

### Step 7 — Run Docker Container

Build Docker image:

```
docker build -t churn-ml-app .
```

Run container:

```
docker run -p 5000:5000 churn-ml-app
```

The application will now be available at:

```
http://localhost:5000
```

---

## Model Evaluation

The best model is selected based on:

• ROC-AUC Score
• F1 Score
• Precision-Recall balance

These metrics are critical for churn prediction because churn datasets are often **imbalanced**.

---

## Future Improvements

Possible improvements to this project include:

• Hyperparameter tuning using Optuna
• SHAP explainability for model interpretation
• Deployment to AWS / Azure
• CI/CD pipeline integration
• Real-time streaming predictions

---

## Author

Amareswari Potu

Machine Learning Engineer | Data Scientist

Specializing in:

Machine Learning
Deep Learning
NLP
MLOps
LLMs and RAG Systems

---

## License

This project is licensed under the MIT License.
