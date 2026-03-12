import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("Full ML pipeline started")

    # -------------------- Step 1: Data Ingestion --------------------
    logging.info("Step 1: Data ingestion started")
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()
    logging.info(f"Step 1: Data ingestion completed. Train: {train_path}, Test: {test_path}")

    # -------------------- Step 2: Data Transformation --------------------
    logging.info("Step 2: Data transformation started")
    transformation = DataTransformation()
    X_train, X_test, y_train, y_test = transformation.initiate_data_transformation(train_path, test_path)
    logging.info("Step 2: Data transformation completed")

    # -------------------- Step 3: Model Training --------------------
    logging.info("Step 3: Model training started")
    trainer = ModelTrainer()
    trainer.initiate_model_trainer(X_train, X_test, y_train, y_test)
    logging.info("Step 3: Model training completed")

    logging.info("Full ML pipeline finished successfully")