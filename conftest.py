import pytest
from tests.fixtures import swapi


@pytest.fixture
def test_swapi():
    return swapi.api
