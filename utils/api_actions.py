from playwright.sync_api import Playwright
from utils import log
from utils.api_utils import request
from typing import Union

def create_user(playwright: Playwright, payload: Union[str | dict] ):

    log.info("Creating user.")
    return request(url="/api/users",
                   method="POST",
                   body=payload,
                   status_code_expected=201)

def get_user(playwright: Playwright, userid: int):
    log.info("Fetching the user details.")
    return request(url=f"/api/users/{userid}",
                   method="GET",
                   status_code_expected=200)

def get_delete_user(playwright: Playwright, userid: int):
    log.info("Fetching the deleted user details.")
    return request(url=f"/api/users/{userid}",
                   method="GET",
                   status_code_expected=404)

def delete_user(playwright: Playwright, userid: int):
    log.info("Deleting the user details.")
    return request(url=f"/api/users/{userid}",
                   method="DELETE",
                   status_code_expected=204)

def update_user(playwright: Playwright, userid: int, payload: Union[str | dict]):

    log.info("Updating the user.")
    return request(url=f"/api/users/{userid}",
                   method="PUT",
                   body=payload,
                   status_code_expected=200)

