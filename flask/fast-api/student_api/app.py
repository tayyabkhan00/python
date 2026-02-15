from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("/Users/tayyabkhan/python/flask/fast-api/student_api/model.pkl")


# ------------------------------
# Home Route
# ------------------------------
@app.route("/")
def home():
    return "Student Pass/Fail Prediction API is running!"


# ------------------------------
# Prediction Route
# ------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate input
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        required_fields = ["hours_studied", "attendance", "previous_score"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Extract features
        hours = float(data["hours_studied"])
        attendance = float(data["attendance"])
        previous = float(data["previous_score"])

        # Convert to numpy array
        features = np.array([[hours, attendance, previous]])

        # Make prediction
        prediction = model.predict(features)
        probability = model.predict_proba(features)

        result = "Pass" if prediction[0] == 1 else "Fail"

        # Return JSON response
        return jsonify({
            "prediction": result,
            "probability_pass": round(float(probability[0][1]), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ------------------------------
# Run Application
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
