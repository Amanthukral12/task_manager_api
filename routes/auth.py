from flask import Blueprint, request, jsonify
from models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields!'}), 400
    
  
    
    existing_user_by_email = User.find_by_email(data['email'])
    
    if  existing_user_by_email:
        return jsonify({'message': 'email already exists!'}), 409
    
 
    try:
        new_user = User.create(
            email=data['email'],
            password=data['password']
        )
        
        return jsonify({
            'message': 'User registered successfully!',
            'user': User.to_json(new_user)
        }), 201
    except Exception as e:
        return jsonify({'message': f'Error registering user: {str(e)}'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
  
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing email or password!'}), 400
    
    
    user = User.find_by_email(data['email'])
    
   
    if user and User.check_password(user, data['password']):
        
        token = generate_token(str(user['_id']))
        
        return jsonify({
            'message': 'Login successful!',
            'token': token,
            'user': User.to_json(user)
        }), 200
    
    return jsonify({'message': 'Invalid email or password!'}), 401


from utils.auth_utils import generate_token