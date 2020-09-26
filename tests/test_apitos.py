from apitos.api import APIClient


SWAPI_URL = 'https://swapi.dev/api/'


def test_people1():
    swapi = APIClient('Star Wars', SWAPI_URL)
    assert swapi.get('people/1')
