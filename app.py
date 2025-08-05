from flask import Flask
from config import Config
from database import init_db
from routes.auth import auth_bp
from routes.tasks import tasks_bp
from routes.main import main_bp
from utils.helpers import get_status_badge_class, get_priority_badge_class

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register template globals
    app.jinja_env.globals.update({
        'get_status_badge_class': get_status_badge_class,
        'get_priority_badge_class': get_priority_badge_class
    })
    
    # Initialize database
    with app.app_context():
        init_db()
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
