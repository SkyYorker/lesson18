from unittest.mock import MagicMock

import pytest
from dao.movie import MovieDAO, Movie


from setup_db import db
from service.movie import MovieService



@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    yellowstone = Movie(id=1, title='Йеллоустоун', 
                   description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»', 
                   trailer='https://www.youtube.com/watch?v=UKei_d0cbP4', 
                   year=2018,
                   rating=8.6,
                   genre_id=17,
                   director_id=1)
    rocketman = Movie(id=5, title='Рокетмен', 
                   description='История превращения застенчивого парня Реджинальда Дуайта, талантливого музыканта из маленького городка, в суперзвезду и культовую фигуру мировой поп-музыки Элтона Джона.', 
                   trailer='https://youtu.be/VISiqVeKTq8', 
                   year=2019,
                   rating=7.3,
                   genre_id=18,
                   director_id=4)
    brokeback_mountain = Movie(id=21, title='Горбатая гора', 
                   description='На фоне живописных просторов штата Вайоминг разворачивается история сложных взаимоотношений двух молодых людей – помощника владельца ранчо и ковбоя родео. Герои случайно встречаются и скоро понимают, что не могут жить друг без друга. Однако судьба упрямо испытывает их на прочность.', 
                   trailer='https://www.youtube.com/watch?v=UKei_d0cbP4', 
                   year=2005,
                   rating=7.6,
                   genre_id=4,
                   director_id=21)

    movie_dao.get_one = MagicMock(return_value=yellowstone)
    movie_dao.get_all = MagicMock(
        return_value=[yellowstone, rocketman, brokeback_mountain])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(21)
        assert movie != None
        assert movie.id != None
        assert movie.description != None
        assert movie.trailer != None
        assert movie.year != None
        assert movie.rating != None
        assert movie.genre_id != None
        assert movie.director_id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {

            "title": 'Горбатая гора',
            "description":'На фоне живописных просторов штата Вайоминг разворачивается история сложных взаимоотношений двух молодых людей – помощника владельца ранчо и ковбоя родео. Герои случайно встречаются и скоро понимают, что не могут жить друг без друга. Однако судьба упрямо испытывает их на прочность.',
            "trailer":'https://youtu.be/VISiqVeKTq8',
            "year":2005,
            "rating":7.6,
            "genre_id":4,
            "director_id":21
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 21,
            "title": 'Горбатая гора',
            "description":'На фоне живописных просторов штата Вайоминг разворачивается история сложных взаимоотношений двух молодых людей – помощника владельца ранчо и ковбоя родео. Герои случайно встречаются и скоро понимают, что не могут жить друг без друга. Однако судьба упрямо испытывает их на прочность.',
            "trailer":'https://youtu.be/VISiqVeKTq8',
            "year":2005,
            "rating":7.6,
            "genre_id":4,
            "director_id":21
        }
        self.movie_service.update(movie_d)
