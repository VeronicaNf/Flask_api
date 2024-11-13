# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Inisialisasi database dan migrasi
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Daftarkan blueprint untuk setiap endpoint
    from .views.user_views import user_bp
    from .views.product_views import product_bp
    from .views.order_views import order_bp
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(order_bp, url_prefix='/orders')

    return app
