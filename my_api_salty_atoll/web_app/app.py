from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate
from web_app.api import my_routes
from flask_cors import CORS


def create_app():
    """Instaniate the Strainiac Flask API application."""
    app = Flask(__name__)
    CORS(app)
    # app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_DATABASE_TRACKING"] = False

    # db.init_app(app)
    # migrate.init_app(app, db)

    app.register_blueprint(my_routes)

    return app
