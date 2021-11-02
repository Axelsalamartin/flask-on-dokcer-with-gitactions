# import Flask class from the flask module
from flask import Flask, request, jsonify
import numpy as np
import pickle

# Create Flask object to run
app = Flask(__name__)

# Loading the model
model = pickle.load(open('src/training/model.pickle', 'rb'))

# Home path
@app.route('/')
def home():
    return "The Flask app is running"

# Prediction path
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    batch = np.array([data['sl'], data['sw'], data['pl'], data['pw']]).reshape((-1,4))
    result = model.predict(batch).reshape((1, -1)).astype(int)
    return(jsonify(results=result.tolist()))
	

if __name__ == "__main__":
    print("[+] Launching the Flask app...")
    app.run(host="0.0.0.0", port=5000)