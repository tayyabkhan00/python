from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI(title="Student Pass/Fail Prediction API")

# Load trained model
model = joblib.load("/Users/tayyabkhan/python/flask/fast-api/student_api(fast-api)/model.pkl")


# -------------------------
# Input Schema (Validation)
# -------------------------
class Student(BaseModel):
    hours_studied: float
    attendance: float
    previous_score: float


# -------------------------
# Home Route
# -------------------------
@app.get("/")
def home():
    return {"message": "Student Pass/Fail Prediction API is running!"}


# -------------------------
# Prediction Route
# -------------------------
@app.post("/predict")
def predict(student: Student):

    try:
        # Convert input to numpy array
        features = np.array([[ 
            student.hours_studied,
            student.attendance,
            student.previous_score
        ]])

        # Make prediction
        prediction = model.predict(features)
        probability = model.predict_proba(features)

        result = "Pass" if prediction[0] == 1 else "Fail"

        return {
            "prediction": result,
            "probability_pass": round(float(probability[0][1]), 2)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
