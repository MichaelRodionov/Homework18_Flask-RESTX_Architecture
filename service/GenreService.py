from dao import GenreDAO


class GenreService:
    """
    Service is needed to work with genres views and GenreDAO
    """
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self) -> list:
        return self.genre_dao.get_all_genres()

    def get_genre(self, genre_id) -> object:
        return self.genre_dao.get_genre_by_id(genre_id)
