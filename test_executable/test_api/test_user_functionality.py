from playwright.sync_api import Page
from utils.context import Context
from utils.api_utils import request, parse_json

ctx = Context()
def test_create_user(page: Page):

    res = request(page=page,
                url="/api/users",
                method="POST",
                body={"name": "morpheus","job": "leader"},
                status_code_expected=201)

    assert parse_json(res, "$.name")[0] == "morpheus"

    userid = parse_json(res, "$.id")

    res = request(url="/api/users/2")

