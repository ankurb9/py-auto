from utils.apiClient import APIClient, Service

client = APIClient(Service.users)

def test_mock_api():

    client.mock({})

