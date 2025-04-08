from datetime import datetime, timezone
from bson import ObjectId
from models import mongo

class Task:
    VALID_STATUSES = ['pending', 'in-progress', 'completed']

    @staticmethod
    def create(title, user_id, description=None, status='pending'):
        if status not in Task.VALID_STATUSES:
            status = 'pending'
        
        task = {
            'title': title,
            'description': description,
            'status': status,
            'user_id': user_id,
            'created_at': datetime.now(timezone.utc),
            'updated_at': datetime.now(timezone.utc)
        }

        result = mongo.db.tasks.insert_one(task)
        task['_id'] = result.inserted_id

        return result
    
    @staticmethod
    def find_by_id(task_id, user_id=None):
        try:
            object_id = ObjectId(task_id)
            query = {'_id': object_id}

            if user_id:
                query['user_id'] = user_id

            return mongo.db.tasks.find_one(query)
        except:
            return None
        
    @staticmethod
    def find_all_by_user(user_id):
        return list(mongo.db.tasks.find({'user_id': user_id}))
    
    @staticmethod
    def update(task_id, user_id, update_data):
        try:
            object_id = ObjectId(task_id)
            update_data['updated_id'] = datetime.now(timezone.utc)

            if 'status' in update_data and update_data['status'] not in Task.VALID_STATUSES:
                update_data['status'] = 'pending'

            result = mongo.db.update_one(
                {'_id': object_id, 'user_id': user_id},
                {'$set': update_data}
            )

            return result.modified_count > 0
        except:
            return False
    
    @staticmethod
    def delete(task_id, user_id):
        try:
            object_id = ObjectId(task_id)
            result = mongo.db.tasks.delete_one({'_id': object_id, 'user_id': user_id})
            return result.deleted_count > 0
        except:
            return False
    
    @staticmethod
    def to_json(task):
        if task:
            return {
                'id': str(task['_id']),
                'title': task['title'],
                'description': task['description'],
                'status': task['status'],
                'user_id': task['user_id'],
                'created_at': task['created_at'].isoformat() if isinstance(task['created_at'], datetime) else task['created_at'],
                'updated_at': task['updated_at'].isoformat() if isinstance(task['updated_at'], datetime) else task['updated_at']
            }
        return None
