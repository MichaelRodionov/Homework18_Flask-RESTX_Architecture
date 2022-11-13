from flask import Flask
from config import Config
from setup_db import db
from flask_restx import Api
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object: Config):
    """
    This function is called to create Flask application
    :param config_object: Config
    :return: Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask):
    """
    This function is called to register extensions init database and create api
    :param app: Flask application
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


application = create_app(Config())


@application.errorhandler(404)
def get_404_error(error):
    """404 errorhandler"""
    return '404 error'


@application.errorhandler(500)
def get_500_error(error):
    """500 errorhandler"""
    return '500 error'


if __name__ == '__main__':
    application.run(port=5050)
