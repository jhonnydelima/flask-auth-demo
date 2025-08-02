from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')
  
  if not username or not password:
    return jsonify({"error": "Username and password are required"}), 400
  
  user = User.query.filter_by(username=username).first()
  if not user or user.password != password:
    return jsonify({"error": "Invalid username or password"}), 401
  
  login_user(user)
  print(current_user.is_authenticated)
  return jsonify({"message": "Login successful"})

if __name__ == '__main__':
  app.run(debug=True)