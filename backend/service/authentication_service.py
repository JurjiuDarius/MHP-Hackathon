import hashlib
from models.user import User
from utils.jwt import create_token
import jwt
from utils.jwt import SECRET_KEY


def login(data):
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")
    if role not in ["employee", "admin"]:
        return {"message": "Invalid role!"}, 400

    user = User.query.filter_by(email=email, role=role).first()
    if not user:
        return {"message": "User not found!"}, 404

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if not hashed_password == user.password:
        return {"message": "Incorrect password!"}, 401

    token = create_token(user.id, role)

    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"message": "Token has expired!"}, 401
    except jwt.InvalidTokenError:
        return {"message": "Invalid token!"}, 401

    if decoded_token.get("userId") != user.id or decoded_token.get("role") != role:
        return {"message": "Token verification failed!"}, 401

    return {"token": token, "user": user.serialize()}, 200
