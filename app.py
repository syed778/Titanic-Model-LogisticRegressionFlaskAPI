from flask import Flask, request, jsonify
import pickle
import numpy as np

# Step 1: Initialize Flask app
app = Flask(__name__)

# Step 2: Load the saved Titanic model
model = pickle.load(open("titanic_model.pkl", "rb"))


# Step 3: Define Home route
@app.route("/")
def home():
    return "Titanic Survival Prediction API is working!"


# Step 4: Define Predict route
@app.route("/predict", methods=["POST"])
def predict():
    # Step 4.1: Get data from request
    data = request.get_json(force=True)

    # Step 4.2: Extract feature values
    features = [
        data["Pclass"],
        data["Age"],
        data["SibSp"],
        data["Parch"],
        data["Fare"],
        data["Sex_male"],
        data["Embarked_Q"],
        data["Embarked_S"],
    ]

    # Step 4.3: Reshape and predict
    prediction = model.predict([np.array(features)])

    # Step 4.4: Send back result
    return jsonify({"Survived": int(prediction[0])})


# Step 5: Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
