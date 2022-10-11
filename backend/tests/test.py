from tests import client

def test_base(client):
    response = client.get("/test")

    assert "This is the base route." in response.data