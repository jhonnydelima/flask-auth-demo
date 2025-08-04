# Flask Auth Demo

This project is a simple authentication API built with Flask, demonstrating user registration, login, logout, and user management with role-based access control (admin/user). It uses MySQL as the database and SQLAlchemy as the ORM. Passwords are securely hashed using bcrypt, and user session management is handled by Flask-Login.

## Features

- User registration with hashed passwords
- User login and logout
- JWT-like session management with Flask-Login
- Role-based access control (admin and user)
- Admin-only endpoints for updating and deleting users
- MySQL database integration

## Technologies Used

- Python 3
- Flask
- Flask-Login
- SQLAlchemy
- MySQL
- bcrypt

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up a MySQL database and update the connection string in `app.py` if needed
4. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints

- `POST /users` - Register a new user
- `POST /login` - Login
- `POST /logout` - Logout
- `GET /users/<user_id>` - Get user info (login required)
- `PATCH /users/<user_id>` - Update user password (admin or self)
- `DELETE /users/<user_id>` - Delete user (admin only)
