from dao import DirectorDAO


class DirectorService:
    """
    Service is needed to work with directors views and DirectorDAO
    """
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> list[object]:
        return self.director_dao.get_all_directors()

    def get_director(self, director_id) -> object:
        return self.director_dao.get_director_by_id(director_id)
