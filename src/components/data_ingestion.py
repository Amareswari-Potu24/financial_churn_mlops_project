import pandas as pd
from sklearn.model_selection import train_test_split
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataIngestion:

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")

        # Load data
        df = pd.read_csv("notebook/data/Churn_Modelling.csv")

        # Create artifacts folder if not exists
        os.makedirs("artifacts", exist_ok=True)

        # Split data
        train, test = train_test_split(df, test_size=0.2, random_state=42)

        train_path = "artifacts/train.csv"
        test_path = "artifacts/test.csv"

        # Save files
        train.to_csv(train_path, index=False)
        test.to_csv(test_path, index=False)

        logging.info(f"Data ingestion completed. Train path: {train_path}, Test path: {test_path}")

        return train_path, test_path