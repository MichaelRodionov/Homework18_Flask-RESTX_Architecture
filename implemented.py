from dao.DirectorDAO import DirectorDAO
from dao.GenreDAO import GenreDAO
from dao.MovieDAO import MovieDAO
from service.MovieService import MovieService
from service.DirectorService import DirectorService
from service.GenreService import GenreService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
