import hashlib
from models.user import User
from utils.jwt import create_token


def login(data):
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")
    if role not in ["employee", "admin"]:
        return {"message": "Invalid role!"}, 400

    user = User.query.filter_by(email=email, role=role).first()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if not hashed_password == user.password:
        return {"message": "Incorrect password!"}, 401
    token = create_token(user.id, role)
    return {"token": token, "user": user.serialize()}, 200
