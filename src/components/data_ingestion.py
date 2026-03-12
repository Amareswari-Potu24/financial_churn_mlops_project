import pandas as pd
import os
import logging
from src.exception import IngestionException

class DataIngestion:

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv("notebook/data/Churn_Modelling.csv")
            os.makedirs("artifacts", exist_ok=True)

            from sklearn.model_selection import train_test_split
            train, test = train_test_split(df, test_size=0.2, random_state=42)

            train_path = "artifacts/train.csv"
            test_path = "artifacts/test.csv"
            train.to_csv(train_path, index=False)
            test.to_csv(test_path, index=False)

            logging.info("Data ingestion completed successfully")
            return train_path, test_path

        except Exception as e:
            raise IngestionException(f"Data ingestion failed: {e}", sys)