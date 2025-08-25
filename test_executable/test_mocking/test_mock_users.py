import json
from playwright.sync_api import Page
from response_builder.user_response import UserResponse

from utils import log


# ===============================
# 1. ReqRes.in - REST API Testing
# ===============================

def test_reqres_users_api(page: Page):
    """Mock ReqRes.in users API"""
    res = UserResponse()

    mock_users = res.response(5)

    page.route("**/api/users*", lambda route: route.fulfill(
        status=200,
        headers={"Content-Type": "application/json"},
        body=json.dumps(mock_users)
    ))

    page.goto("https://reqres.in/")

