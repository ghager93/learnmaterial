import pytest

from app import app


@pytest.fixture
def client(app):
    return app.test_client()