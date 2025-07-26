from playwright.sync_api import Playwright
from utils.log import get_logger
from utils.api_utils import request
from typing import Union

log = get_logger()
def create_user(playwright: Playwright, payload: Union[str | dict] ):

    log.info("Creating user.")
    return request(playwright=playwright,
                   url="/api/users",
                   method="POST",
                   body=payload,
                   status_code_expected=201)

def get_user(playwright: Playwright, userid: int):
    log.info("Fetching the user details.")
    return request(playwright=playwright,
                   url=f"/api/users/{userid}",
                   method="GET",
                   status_code_expected=200)

def update_user(playwright: Playwright, userid: int, payload: Union[str | dict]):

    log.info("Updating the user.")
    return request(playwright=playwright,
                   url=f"/api/users/{userid}",
                   method="PUT",
                   body=payload,
                   status_code_expected=200)

