from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_caching import Cache
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter(key_func=lambda: 'global')
cache = Cache(config={'CACHE_TYPE': 'simple'})
mail = Mail()
