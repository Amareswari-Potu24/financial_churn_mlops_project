import os
import pickle
import logging
from sklearn.metrics import accuracy_score
from src.exception import CustomException

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def save_object(file_path, obj):
    """Save Python object to file with pickle."""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Object saved successfully at {file_path}")

    except Exception as e:
        logging.error(f"Failed to save object at {file_path}: {e}")
        raise CustomException(f"Failed to save object at {file_path}: {e}")

def load_object(file_path):
    """Load Python object from file with pickle."""
    try:
        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)
        logging.info(f"Object loaded successfully from {file_path}")
        return obj

    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        raise CustomException(f"File not found: {file_path}: {e}")

    except Exception as e:
        logging.error(f"Failed to load object from {file_path}: {e}")
        raise CustomException(f"Failed to load object from {file_path}: {e}")