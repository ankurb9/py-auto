from playwright.sync_api import Page, Route, Request
from pages.reqres import ReqRes

def test_user_response_modify(page: Page):
    res = { "data": {
                "id": 2,
                "email": "ankur.badamikar@reqres.in",
                "first_name": "Ankur",
                "last_name": "Badamikar",
                "avatar": "https://reqres.in/img/faces/2-image.jpg"
            },
            "support": {
                "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
                "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
                }
            }

    def handle(route: Route, request: Request):

        route.fulfill(status=200,
                      json=res,
                      content_type="application/json")

    page.route("**/api/users/2", handle)

    reqres = ReqRes(page=page)

    reqres.click_single_user()
    resp = reqres.get_resp()

    assert res == resp

