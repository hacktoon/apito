from apito.http import HTTPMethod


def test_swapi_name(test_swapi):
    assert test_swapi.name == 'Star Wars API'


def test_swapi_url(test_swapi):
    assert test_swapi.url == 'https://swapi.dev/api/'


def test_swapi_people_endpoint_static_attrs(test_swapi):
    endpoint = test_swapi.endpoints[0]
    assert endpoint.name == 'people'
    assert endpoint.method == HTTPMethod.GET


def test_swapi_get_attribute(test_swapi):
    assert test_swapi.get
