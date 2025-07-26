import json

from jsonpath_ng import parse
from urllib.parse import urljoin
from utils.context import Context
import os
from pathlib import Path
from playwright.sync_api import Page, APIResponse
from typing import Literal, Optional, Union
ctx = Context()

def __get_json_body(body):
    project_root = Path(__file__).resolve().parents[1]

    if isinstance(body, str):
        if os.path.isfile(body):
            config_file = project_root / "config" / body
            with config_file.open() as f:
                return json.load(f)
        else:
            return json.loads(body)

    if isinstance(body, (dict, list)):
        return body

    return None


def request(page: Page, url: str ,
            method: Literal["GET", "POST", "PUT", "DELETE"],
            body: Optional[str | dict] = None,
            status_code_expected: int = 200) -> dict:

    final_url = urljoin(ctx.api_host, url=url)
    data = __get_json_body(body)
    headers = {"Content-Type": "application/json"}

    method_func = {
        "GET": page.request.get,
        "POST": page.request.post,
        "PUT": page.request.put,
        "DELETE": page.request.delete
    }[method]

    request_args = {
        "url": final_url,
        "headers": headers,
        "max_retries": 5
    }
    if method not in ["GET", "DELETE"]:
        request_args["data"] = data

    res: APIResponse = method_func(**request_args)

    assert res.status == status_code_expected, "Invalid status code received"

    return res.json()


def parse_json(json_body, path) -> list:

    expr = parse(path)

    matches = [match.value for match in expr.find(json_body)]

    return matches