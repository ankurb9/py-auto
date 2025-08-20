from utils import log
from request_builder import UserBuilder
from utils.apiClient import APIClient, Service

client = APIClient(Service.users)

def test_create_user():


    payload = (UserBuilder()
               .set_name("Ankur")
               .set_email("test9@test.com")
               .set_phone("0123456789")
               .set_username("test9")
               .set_city("Pune")
               .set_state("Maharashtra")
               .set_street("Bhumkar Chowk")
               .set_zipcode("411057")
               .build()
               )

    client.post(payload=payload)



def test_patch_user_details():

    payload = (UserBuilder(exclude_none=True)
               .set_name("Ankur")
               .set_phone("0111111111")
               .build()
    )

    client.patch(identifier=1, payload=payload)


def test_delete_user():

    client.delete(identifier=1)

