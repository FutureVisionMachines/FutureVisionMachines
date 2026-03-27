import os
from datetime import datetime
from flask import Flask
from config import config
from extensions import db, migrate, limiter, cache, mail

def create_app(config_name=None):
    """Application factory pattern"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)
    cache.init_app(app)
    mail.init_app(app)
    
    # Register blueprints
    from app.routes.public import public_bp
    from app.routes.admin import admin_bp
    
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Template filters
    from app.helpers.utils import format_datetime, get_status_badge_class
    app.jinja_env.filters['format_datetime'] = format_datetime
    app.jinja_env.filters['status_badge'] = get_status_badge_class
    
    # Template context processors
    @app.context_processor
    def inject_globals():
        return {
            'current_year': lambda: datetime.now().year
        }
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
