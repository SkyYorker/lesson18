from unittest.mock import MagicMock
import sys

import pytest
from dao.genre import GenreDAO, Genre

from setup_db import db
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    comedy = Genre(id=1, name='Комедия')
    family = Genre(id=2, name='Семейный')
    mockumentary = Genre(id=3, name=' Мокьюментари')

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(
        return_value=[comedy, family, mockumentary])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {

            "name": 'Мокьюментари'
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id != None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {
            "id": 3,
            "username": 'Мокьюментари'
        }
        self.genre_service.update(genre_d)
