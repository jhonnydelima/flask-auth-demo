from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
# view login

@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')
  
  if not username or not password:
    return jsonify({"error": "Username and password are required"}), 400
  
  pass

if __name__ == '__main__':
  app.run(debug=True)