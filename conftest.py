import pytest

@pytest.fixture(scope="session")
def book_url(scope = 'session'):
    return "http://pulse-rest-testing.herokuapp.com/books"

@pytest.fixture(scope="session")
def role_url(scope = 'session'):
    return "http://pulse-rest-testing.herokuapp.com/roles"
