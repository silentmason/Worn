# backend/main.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Placeholder for Discord user data (replace with actual Discord API integration)
user_data = {
    'username': 'CoolUser123',
    'profile_picture': 'https://via.placeholder.com/50',  # Placeholder image
}

@app.route('/user')
def get_user():
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(debug=False)