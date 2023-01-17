import sys

sys.path.append(r"D:\Pro\Python\lesson18\demostration_solution")


import pytest
from unittest.mock import MagicMock
from service.director import DirectorServie
from dao.director import DirectorDAO, Director

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    taylor = Director(id=1, name='Тейлор Шеридан')
    tarantino = Director(id=2, name='Квентин Тарантино')
    skyyorker = Director(id=3, name='SkyYorker')

    director_dao.get_one = MagicMock(return_value=taylor)
    director_dao.get_all = MagicMock(
        return_value=[taylor, tarantino, skyyorker])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorServie(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id != None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {

            "name": 'SkyYorker'
        }
        director = self.director_service.create(director_d)
        assert director.id != None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "id": 3,
            "name": 'SkyYorker'
        }
        self.director_service.update(director_d)
