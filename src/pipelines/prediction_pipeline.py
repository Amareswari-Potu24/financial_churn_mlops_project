import pandas as pd
import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.utils import load_object
from src.exception import PredictionException


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PredictPipeline:

    def __init__(self):
        try:
            logging.info("Loading model and preprocessor for prediction")
            self.model = load_object("artifacts/model.pkl")
            self.preprocessor = load_object("artifacts/preprocessor.pkl")
            logging.info("Model and preprocessor loaded successfully")
        except Exception as e:
            # sys passed to match CustomException signature
            raise PredictionException(f"Failed to load model/preprocessor: {e}", sys)

    def predict(self, features):
        try:
            # Convert dict to DataFrame if needed
            if not isinstance(features, pd.DataFrame):
                features = pd.DataFrame([features])

            logging.info("Transforming input features")
            scaled = self.preprocessor.transform(features)

            logging.info("Making predictions")
            pred = self.model.predict(scaled)
            return pred

        except Exception as e:
            raise PredictionException(f"Prediction failed: {e}", sys)