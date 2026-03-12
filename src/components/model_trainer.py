import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from src.utils import evaluate_models, save_object
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ModelTrainer:

    def initiate_model_trainer(self, X_train, X_test, y_train, y_test):
        logging.info("Model training started")

        models = {
            "LogisticRegression": LogisticRegression(),
            "RandomForest": RandomForestClassifier(),
            "XGBoost": XGBClassifier()
        }

        # Evaluate models
        report = evaluate_models(X_train, y_train, X_test, y_test, models)
        best_model_name = max(report, key=report.get)
        best_model = models[best_model_name]

        logging.info(f"Best model selected: {best_model_name} with accuracy: {report[best_model_name]}")

        # MLflow logging
        logging.info("MLflow run started")
        mlflow.set_experiment("churn_prediction")
        with mlflow.start_run():
            mlflow.log_param("best_model", best_model_name)
            mlflow.log_metric("accuracy", report[best_model_name])

            # Updated log_model call using 'name' instead of deprecated 'artifact_path'
            mlflow.sklearn.log_model(sk_model=best_model, name="model")

        logging.info("MLflow run completed")

        # Save model locally
        save_object("artifacts/model.pkl", best_model)
        logging.info("Model saved at artifacts/model.pkl")
        logging.info("Model training completed")