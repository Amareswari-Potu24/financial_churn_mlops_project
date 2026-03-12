import sys
import logging

# Configure logging for the project
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def error_message_detail(error, error_detail: sys):
    """Generate detailed error message with file name and line number"""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in script [{file_name}] at line [{line_number}]: {str(error)}"

class CustomException(Exception):
    """Base exception class with detailed error logging"""
    def __init__(self, error_message, error_detail: sys):
        detailed_message = error_message_detail(error_message, error_detail)
        super().__init__(detailed_message)
        self.error_message = detailed_message
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message

# Specific exceptions for your pipeline
class IngestionException(CustomException):
    pass

class TransformationException(CustomException):
    pass

class ModelTrainingException(CustomException):
    pass

class PredictionException(CustomException):
    pass