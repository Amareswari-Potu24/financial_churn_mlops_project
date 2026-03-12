import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def error_message_detail(error, error_detail: sys):
    """Generate detailed error message with file name and line number"""
    exc_type, exc_obj, exc_tb = error_detail.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "<unknown>"
        line_number = 0
    return f"Error occurred in script [{file_name}] at line [{line_number}]: {str(error)}"

class CustomException(Exception):
    """Base exception class with detailed logging"""
    def __init__(self, error_message, error_detail: sys):
        detailed_message = error_message_detail(error_message, error_detail)
        super().__init__(detailed_message)
        self.error_message = detailed_message
        logging.error(self.error_message)

class PredictionException(CustomException):
    """Specific exception for prediction pipeline"""
    pass