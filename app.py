from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

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

@app.route('/logout', methods=['POST'])
@login_required
def logout():
  logout_user()
  return jsonify({"message": "Logged out successfully"})

@app.route('/users', methods=['POST'])
def create_user():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')

  if not username or not password:
    return jsonify({"error": "Username and password are required"}), 400
  
  if User.query.filter_by(username=username).first():
    return jsonify({"error": "User already exists"}), 409
  
  user = User(username=username, password=password)
  db.session.add(user)
  db.session.commit()
  return jsonify({"message": "User created successfully"}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
@login_required
def get_user(user_id):
  user = User.query.get(user_id)
  if not user:
    return jsonify({"error": "User not found"}), 404
  return jsonify({"message": user.username})

if __name__ == '__main__':
  app.run(debug=True)