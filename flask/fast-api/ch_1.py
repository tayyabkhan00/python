from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "ML Model API is Live"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    return jsonify({"prediction": 1})

if __name__ == "__main__":
    app.run(debug=True)
