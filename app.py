from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Database setup (SQLite)
DATABASE = 'social_media.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

def init_db():
    with app.app_context():
        db = get_db_connection()
        with open('schema.sql', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Create the database tables if they don't exist
try:
    with app.app_context():
        get_db_connection()
except sqlite3.OperationalError:
    init_db()

# --- Routes ---

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if username exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return jsonify({'message': 'Username already exists'}), 400

    # Create new user
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if not user or user['password'] != password:
        return jsonify({'message': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful'}), 200

@app.route('/logout', methods=['POST'])
def logout():
    # In a real application, you might want to invalidate the user's session here
    return jsonify({'message': 'Logout successful'}), 200

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    text = data.get('text')
    username = data.get('username')  # Assume username is sent with the post for now

    if not text or not username:
        return jsonify({'message': 'Text and username are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (username, text) VALUES (?, ?)', (username, text))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    conn.close()

    # Convert rows to dictionaries before jsonify
    posts_list = [dict(post) for post in posts]

    return jsonify(posts_list), 200

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
