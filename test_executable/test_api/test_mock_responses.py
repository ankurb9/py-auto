import responses
import requests

@responses.activate
def test_mock_api():
    responses.add(
        method=responses.POST,
        url="https://api.example.com/users",
        json={"id": 1, "name": "Mocked"},
        status=201,
    )

    resp = requests.post("https://api.example.com/users", json={"name": "ankur"})
    assert resp.status_code == 201
    assert resp.json() == {"id": 1, "name": "Mocked"}