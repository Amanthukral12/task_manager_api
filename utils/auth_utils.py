import jwt
from functools import wraps
from datetime import datetime, timezone, timedelta
from flask import current_app, request, jsonify
from models.user import User

def generate_token(user_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES']),
        'iat': datetime.now(timezone.utc),
        'sub': user_id
    }
    return jwt.encode(
        payload, current_app.config['JWT_SECRET_KEY'],algorithm='HS256'
    )

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token_parts = auth_header.split()

            if len(token_parts) == 2 and token_parts[0].lower() == 'bearer':
                token = token_parts[1]
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        try:
            payload = jwt.decode(
                token,
                current_app.config['JWT_SECRET_KEY'],
                algorithms=['HS256']
            )
            user_id = payload['sub']

            user = User.find_by_id(user_id)
            if not user:
                return jsonify({'message': 'User not found'}), 401
            
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        
        kwargs['user_id'] = user_id
        return f(*args, **kwargs)
    return decorated