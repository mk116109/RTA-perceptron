import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

model_path = "https://github.com/mk116109/RTA-perceptron/blob/main/perceptron.pkl"
with open(model_path, "rb") as picklefile:
    model = pickle.load(picklefile)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        sepal_length = float(request.args.get('sl'))
        petal_length = float(request.args.get('pl'))
    else:  # POST
        data = request.get_json(force=True)
        sepal_length = float(data.get('sl'))
        petal_length = float(data.get('pl'))

    features = [sepal_length, petal_length]
    
    # Predict the class using the model
    predicted_class = int(model.predict(features))
    output = {"features": features, "predicted_class": predicted_class}
    
    # Return a json object containing the features and prediction
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)