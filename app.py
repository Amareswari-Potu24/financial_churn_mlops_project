import sys
import os
from flask import Flask, request, render_template

# Add project root to Python path so Flask can find src
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Import your PredictPipeline class
from src.pipelines.prediction_pipeline import PredictPipeline

app = Flask(__name__)
predict_pipeline = PredictPipeline()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data from the HTML form
        features = {key: float(value) for key, value in request.form.items()}
        
        # Get prediction from the pipeline
        prediction = predict_pipeline.predict(features)[0]
        
        # Render the HTML with prediction
        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Host 0.0.0.0 for Docker; debug=True for development
    app.run(debug=True, host='0.0.0.0')