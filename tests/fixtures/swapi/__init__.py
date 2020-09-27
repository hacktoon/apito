from apitos.api import APIClient

from . import people_endpoints  # noqa!


URL = 'https://swapi.dev/api/'


api = APIClient('Star Wars API', URL)
