from flask import Blueprint, request, jsonify
from models.task import Task
from utils.auth_utils import token_required

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@tasks_bp.route('/', methods=['POST'])
@token_required
def create_task(user_id):
    data = request.get_json()
    

    if not data or not data.get('title'):
        return jsonify({'message': 'Title is required!'}), 400
    

    try:
        new_task = Task.create(
            title=data['title'],
            description=data.get('description'),
            status=data.get('status', 'pending'),
            user_id=user_id
        )
        
        return jsonify({
            'message': 'Task created successfully!',
            'task': Task.to_json(new_task)
        }), 201
    except Exception as e:
        return jsonify({'message': f'Error creating task: {str(e)}'}), 500

@tasks_bp.route('/', methods=['GET'])
@token_required
def get_tasks(user_id):
    try:
        tasks = Task.find_all_by_user(user_id)
        return jsonify({
            'tasks': [Task.to_json(task) for task in tasks],
            'count': len(tasks)
        }), 200
    except Exception as e:
        return jsonify({'message': f'Error fetching tasks: {str(e)}'}), 500

@tasks_bp.route('/<task_id>', methods=['GET'])
@token_required
def get_task(user_id, task_id):
    try:
        task = Task.find_by_id(task_id, user_id)
        
        if not task:
            return jsonify({'message': 'Task not found!'}), 404
        
        return jsonify({'task': Task.to_json(task)}), 200
    except Exception as e:
        return jsonify({'message': f'Error fetching task: {str(e)}'}), 500

@tasks_bp.route('/<task_id>', methods=['PUT'])
@token_required
def update_task(user_id, task_id):
    data = request.get_json()
    
    if not data:
        return jsonify({'message': 'No update data provided!'}), 400
    
    try:
        task = Task.find_by_id(task_id, user_id)
        
        if not task:
            return jsonify({'message': 'Task not found!'}), 404
        

        update_data = {}
        
        if 'title' in data:
            update_data['title'] = data['title']
        
        if 'description' in data:
            update_data['description'] = data['description']
        
        if 'status' in data:
            if data['status'] not in Task.VALID_STATUSES:
                return jsonify({'message': f'Invalid status! Must be one of: {", ".join(Task.VALID_STATUSES)}'}), 400
            update_data['status'] = data['status']
        
       
        success = Task.update(task_id, user_id, update_data)
        
        if success:
            updated_task = Task.find_by_id(task_id, user_id)
            return jsonify({
                'message': 'Task updated successfully!',
                'task': Task.to_json(updated_task)
            }), 200
        else:
            return jsonify({'message': 'Failed to update task!'}), 500
            
    except Exception as e:
        return jsonify({'message': f'Error updating task: {str(e)}'}), 500

@tasks_bp.route('/<task_id>', methods=['DELETE'])
@token_required
def delete_task(user_id, task_id):
    try:
        task = Task.find_by_id(task_id, user_id)
        
        if not task:
            return jsonify({'message': 'Task not found!'}), 404
        
        success = Task.delete(task_id, user_id)
        
        if success:
            return jsonify({'message': 'Task deleted successfully!'}), 200
        else:
            return jsonify({'message': 'Failed to delete task!'}), 500
            
    except Exception as e:
        return jsonify({'message': f'Error deleting task: {str(e)}'}), 500