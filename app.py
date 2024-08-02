from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/bfhl": {"origins": "http://localhost:3000"}})  # Enable CORS for specific route and origin
@app.route("/")
def home():
    return "Hello World", 200
@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    data = request.json.get('data')
    print("Received data:", data)  # Debug print

    if not data:
        print("No data provided")  # Debug print
        return jsonify({"is_success": False, "message": "No data provided"}), 400

    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_alphabet = max(alphabets, key=str.lower) if alphabets else ""

    response = {
        "is_success": True,
        "user_id": "your_name_ddmmyyyy",
        "email": "your_email@example.com",
        "roll_number": "your_roll_number",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }

    print("Response:", response)  # Debug print
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
