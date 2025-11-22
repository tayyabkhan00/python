from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Simple API route
@app.route("/hello")
def hello():
    return jsonify({"message": "Hello Tayyab!"})

# 2. API with parameters
@app.route("/square")
def square_number():
    num = int(request.args.get("num"))
    return jsonify({"result": num * num})

# 3. API with authentication
API_KEY = "12345"

@app.route("/secret-data")
def secret():
    key = request.args.get("key")
    
    if key != API_KEY:
        return jsonify({"error": "Invalid key"}), 401
    
    return jsonify({"data": "This is secret data!"})

if __name__ == "__main__":
    app.run(debug=True)
