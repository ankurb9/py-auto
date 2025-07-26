from playwright.sync_api import Playwright
from utils.context import Context
from utils.api_utils import parse_json
from utils.log import get_logger
from utils.api_actions import create_user, get_user, update_user, delete_user, get_delete_user

ctx = Context()
log = get_logger()

def test_create_user(playwright: Playwright):

    log.info("Creating user.")
    res = create_user(playwright, {"name": "morpheus","job": "leader"})

    assert parse_json(res, "$.name")[0] == "morpheus"

    userid = int(parse_json(res, "$.id")[0])

    log.info("Validating the user created.")
    res = get_user(playwright, userid)
    assert  parse_json(res, "$.data.name")[0] == "morpheus"


def test_update_user(playwright: Playwright):

    log.info("Creating the user.")
    res = create_user(playwright, {"name": "morpheus","job": "leader"})

    assert parse_json(res, "$.job")[0] == "leader"

    userid = int(parse_json(res, "$.id")[0])

    res = update_user(playwright, userid, "update_user.json")
    assert parse_json(res, "$.name")[0] == "morpheus"

    # res = get_user(playwright, userid)
    # assert parse_json(res, "$.data.job")[0] == "Updated_leader"


def test_delete_user(playwright: Playwright):
    log.info("Creating the user.")
    res = create_user(playwright, {"name": "morpheus", "job": "leader"})

    assert parse_json(res, "$.job")[0] == "leader"

    userid = int(parse_json(res, "$.id")[0])

    delete_user(playwright, userid)

    get_delete_user(playwright, userid)
