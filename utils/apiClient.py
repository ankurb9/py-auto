import json
from enum import Enum
import requests
import responses
from . import ctx
from . import log


class Service(Enum):
    users = "users"
    posts = "Posts"


class APIClient:
    DEFAULT_HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self, service: Service):
        self.service = service
        self.url = f"{ctx.api_host}/{service.value}"
        self.session = requests.Session()
        self.session.headers.update(self.DEFAULT_HEADERS)

    def post(self, payload: dict, status_code_expected=201):
        log.info(f"URL: {json.dumps(self.url)}")
        log.info(f"Payload: {json.dumps(payload)}")

        resp: responses = self.session.post(url=self.url,json=payload)

        self._validate_status_code(resp.status_code, status_code_expected)

        return self._extract_response(resp)

    def get(self, identifier: str|int, status_code_expected=200):
        resp: responses = self.session.get(url=f"{self.url}/{identifier}")
        self._validate_status_code(resp.status_code, status_code_expected)
        return self._extract_response(resp)

    def delete(self, identifier: str|int, status_code_expected=202):
        resp: responses = self.session.delete(url=f"{self.url}/{identifier}")
        self._validate_status_code(resp.status_code, status_code_expected)

    def patch(self, identifier: str|int, payload, status_code_expected=200):
        resp: responses = self.session.patch(url=f"{self.url}/{identifier}", json=payload)
        self._validate_status_code(resp.status_code, status_code_expected)
        return self._extract_response(resp)

    @staticmethod
    def mock(response: dict):

        return response

    @staticmethod
    def _validate_status_code(actual, expected):
        assert actual == expected, f"Expected status code {expected} doesn't match with actual {actual}"

    @staticmethod
    def _extract_response(resp: responses):
        if resp.headers.get("Content-Type") == "application/json":
            data = resp.json()

        else:
            data = resp.text

        log.info(f"response: {data}")

        return data




