from datetime import datetime, timezone
import bcrypt
from bson import ObjectId
from models import mongo

class User:
    @staticmethod
    def create(email, password):
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt).decode('utf-8')

        user = {
            'email': email,
            'password_hash': password_hash,
            'created_at': datetime.now(timezone.utc)
        }

        result = mongo.db.users.insert_one(user)
        user['_id'] = result.inserted_id

        return user
    
    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})
    
    @staticmethod
    def find_by_id(user_id): 
        try:
            object_id = ObjectId(user_id)
            return mongo.db.users.find_one({'_id': object_id})
        except:
            return None
    
    @staticmethod
    def check_password(user, password):
        password_bytes = password.encode('utf-8')
        hash_bytes = user['password_hash'].encode('utf-8')
        return bcrypt.checkpw(password_bytes, hash_bytes)
    
    @staticmethod
    def to_json(user):
        if user:
            return {
                'id': str(user['_id']),
                'email': user['email'],
                'created_at': user['created_at'].isoformat() if isinstance(user['created_at'], datetime) else user['created_at']
            }
        return None