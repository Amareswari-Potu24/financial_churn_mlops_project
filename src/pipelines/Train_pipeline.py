import logging
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import IngestionException, TransformationException, ModelTrainingException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("Full ML pipeline started")

    try:
        # Step 1: Ingestion
        logging.info("Step 1: Data ingestion started")
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()
        logging.info("Step 1: Data ingestion completed")

        # Step 2: Transformation
        logging.info("Step 2: Data transformation started")
        transformation = DataTransformation()
        X_train, X_test, y_train, y_test = transformation.initiate_data_transformation(train_path, test_path)
        logging.info("Step 2: Data transformation completed")

        # Step 3: Model Training
        logging.info("Step 3: Model training started")
        trainer = ModelTrainer()
        trainer.initiate_model_trainer(X_train, X_test, y_train, y_test)
        logging.info("Step 3: Model training completed")

    except (IngestionException, TransformationException, ModelTrainingException) as e:
        logging.error(f"Pipeline failed with custom exception: {e}")
        raise e

    except Exception as e:
        logging.error(f"Pipeline failed with unexpected error: {e}")
        raise e

    logging.info("Full ML pipeline finished successfully")