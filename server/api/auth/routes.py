from flask import request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required
)
from api import mongo
from api.models import User
from api.utils.objectId import PydanticObjectId
from . import auth_bp

db = mongo.db
users = db["users"]

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    required_fields = ['full_name', 'username', 'email']

    if not data or not all(field in data for field in required_fields):
        return jsonify({ "error": "Missing required fields" }), 400
    
    if users.find_one({ "username": data["username"] }) or users.find_one({ "email": data["email"] }):
        return jsonify({ "error": "Username or Email already exists" }), 400

    try:
        password = data.pop("password", None)
        if not password:
            return jsonify({ "error": "Password is required" }), 400

        user = User(**data)
        user.set_password(password)

        user_id = users.insert_one(user.to_bson()).inserted_id
        user.id = PydanticObjectId(str(user_id))
        print(user)

        return {
            "message": "User registered successfully",
            "user": user.to_json(exclude_password=True)
        }, 200

    except Exception as e:
        print(f'Exception: {e}')
        return jsonify({ "error": "Internal Server Error" }), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not all(field in data for field in ["username", "password"]):
        return jsonify({ "error": "Missing required fields" }), 400
    
    user_data = users.find_one({ "username": data["username"] })

    if not user_data:
        return jsonify({ "error": "Invalid username or password" }), 400
    
    user = User(**user_data)

    if not user.check_password(data["password"]):
        return jsonify({ "error": "Invalid username or password" }), 400
    
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    }), 200

@auth_bp.route('/refresh', methods=['GET'])
def refresh():
    current_user_id = get_jwt_identity()
    access_token = create_access_token(identity=str(current_user_id))
    return jsonify({ "access_token": access_token }), 200