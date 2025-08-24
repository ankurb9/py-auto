from utils import log
from request_builder import UserBuilder
from utils.apiClient import APIClient, Service

client = APIClient(Service.users)

def test_create_user():


    payload = (UserBuilder()
               .set_name()
               .set_email("test@gmail.com")
               .set_phone()
               .set_username("testingFaker")
               .set_city()
               .set_state()
               .set_street()
               .set_zipcode()
               .build()
               )

    client.post(payload=payload)



def test_patch_user_details():

    payload = (UserBuilder()
               .set_name()
               .set_phone("0111111111")
               .build()
    )

    client.patch(identifier=1, payload=payload)


def test_delete_user():

    client.delete(identifier=1)

