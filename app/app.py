
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Loading the saved models
fraud_model = joblib.load('models/fraud_model.pkl')

app = Flask(__name__)

@app.route('/predict_fraud', methods=['POST'])
def predict_fraud():
    data = request.get_json(force=True)
    prediction = fraud_model.predict([list(data.values())])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
