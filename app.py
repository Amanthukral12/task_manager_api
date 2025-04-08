from flask import Flask, jsonify
from flask_cors import CORS
from models import mongo
from routes.auth import auth_bp
from routes.tasks import tasks_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    mongo.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    
    @app.route('/')
    def index():
        return jsonify({
            'message': 'Welcome to Task Manager API',
            'version': '1.0.0',
            'documentation': 'Check README.md for API documentation'
        })
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'message': 'Endpoint not found!'}), 404
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({'message': 'Internal server error!'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)