# external imports
import datetime as dt
from flask import request, current_app, jsonify, abort
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    get_jwt_identity, 
    jwt_required
)

# internal imports
from api import mongo
from api.users import user_bp
from api.db.user_models import User
from api.db.pydantic_objectid import PydanticObjectId
from api.utils.validators import email_validator, username_validator, password_validator

@user_bp.route('/auth/register', methods=['POST'])
def register():
    users = mongo.db.users

    try:
        data = request.get_json()
        email = data.get('email', '').strip()
        username = data.get('username', '').strip()
        password = data.pop('password', None) # not storing actual password in the db

        if not data or not all([email, username, password]):
            abort(400, 'Missing required fields.')

        if not email_validator(email):
            abort(400, 'Invalid email address.')

        if not username_validator(username):
            abort(400, 'Username must be within 3 to 64 characters.')

        if not password_validator(password):
            abort(400, 'Password must contain an uppercase letter, a lowercase letter, a digit and a special character and its minimum length must be 8.')

        if users.find_one({'$or': [{'email': email}, {'username': username}]}):
            abort(400, 'Email or Username already exists.')

        user = User(**data)
        user.get_password_hash(password)
        user_id = str(users.insert_one(user.to_bson()).inserted_id)
        user.id = PydanticObjectId(user_id)

        return jsonify({
            'message': 'User registered successfully.',
            'data': {
                'user': user.to_json(),
                'access_token': create_access_token(
                    identity=user_id, 
                    expires_delta=dt.timedelta(seconds=current_app.config.JWT_ACCESS_TOKEN_EXPIRES)
                ),
                'refresh_token': create_refresh_token(
                    identity=user_id,
                    expires_delta=dt.timedelta(seconds=current_app.config.JWT_REFRESH_TOKEN_EXPIRES)
                )
            }
        }), 201

    except Exception as e:
        current_app.logger.error('Error while registering user: %s', e)
        raise e
    
@user_bp.route('/auth/login', methods=['POST'])
def login():
    users = mongo.db.users

    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()

        if not data or (not username and not email) or not password:
            abort(400, 'Missing required fields.')

        res = None
        if username:
            res = users.find_one({'username': username})
        elif email:
            res = users.find_one({'email': email})

        if not res: 
            abort(404, 'User not found.')

        user = User(**res)
        if not user.verify_password(password):
            abort(400, 'Invalid credentials.')

        return jsonify({
            'message': 'User logged in successfully.',
            'data': {
                'user': user.to_json(),
                'access_token': create_access_token(
                    identity=user.id, 
                    expires_delta=dt.timedelta(seconds=current_app.config.JWT_ACCESS_TOKEN_EXPIRES)
                ),
                'refresh_token': create_refresh_token(
                    identity=user.id,
                    expires_delta=dt.timedelta(seconds=current_app.config.JWT_REFRESH_TOKEN_EXPIRES)
                )
            }
        }), 200
    
    except Exception as e:
        current_app.logger.error('Error while logging user: %s', e)
        raise e
    
@user_bp.route('/auth/refresh', methods=['POST'])
def refresh():
    try:
        user_id = get_jwt_identity()
        new_access_token = create_access_token(
            identity=user_id, 
            expires_delta=dt.timedelta(seconds=current_app.config.JWT_ACCESS_TOKEN_EXPIRES)
        )
        
        return jsonify({
            'message': 'Access token refreshed successfully.',
            'data': { 'access_token': new_access_token }
        }), 200 
    
    except Exception as e:
        current_app.logger.error('Error while refreshing token: %s', e)
        raise e