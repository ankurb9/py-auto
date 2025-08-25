import json

from utils import log
from reqres_builder import UserBuilder
from utils.apiClient import APIClient, Service
from jsonschema import validate, ValidationError

client = APIClient(Service.users)

def test_create_user():

    user = UserBuilder()
    payload = (user
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

    res = client.post(payload=payload)

    validate(res, schema=user.create_user_schema)


def test_patch_user_details():
    user = UserBuilder()
    payload = (user
               .set_name()
               .set_phone("0111111111")
               .build()
    )

    res = client.patch(identifier=1, payload=payload)
    validate(res, schema=user.path_user_schema)


def test_delete_user():
    client.delete(identifier=1)

