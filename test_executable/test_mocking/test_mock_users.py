import json
from playwright.sync_api import Page

from utils import log


# ===============================
# 1. ReqRes.in - REST API Testing
# ===============================

def test_reqres_users_api(page: Page):
    """Mock ReqRes.in users API"""

    mock_users = {
        "page": 1,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": [
            {
                "id": 1,
                "email": "ankurb9@reqres.in",
                "first_name": "Mock",
                "last_name": "User"
            }
        ]
    }

    page.route("**/api/users*", lambda route: route.fulfill(
        status=200,
        headers={"Content-Type": "application/json"},
        body=json.dumps(mock_users)
    ))

    page.goto("https://reqres.in/")

    log.info("")