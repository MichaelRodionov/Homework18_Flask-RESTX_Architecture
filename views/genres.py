from flask_restx import Resource, Namespace
from dao.models.models import GenreSchema
from implemented import genre_service


genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @staticmethod
    def get():
        """This view return all genres by GET request"""
        return genres_schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @staticmethod
    def get(genre_id):
        """This view return one genre filtered by genre_id by GET request"""
        return genre_schema.dump(genre_service.get_genre(genre_id)), 200
