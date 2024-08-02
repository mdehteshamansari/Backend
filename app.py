from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

    if request.method == 'POST':
        data = request.get_json()
        full_name = data.get('full_name', 'john_doe')
        dob = data.get('dob', '17091999')
        user_id = f"{full_name}_{dob}"

        email = "john@xyz.com"
        roll_number = "ABCD123"
        numbers = [x for x in data['data'] if x.isdigit()]
        alphabets = [x for x in data['data'] if x.isalpha()]
        highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }

        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
