import json
from typing import Literal, Optional, Union, Any
from urllib.parse import urljoin
from jsonpath_ng import parse
from playwright.sync_api import APIResponse, Playwright
from utils import ctx

def __get_json_body(body):

    if isinstance(body, str):

        if body.endswith(".json"):
            with open(f"{ctx.project_root}/payloads/{body}") as f:
                return json.load(f)
        else:
            return json.loads(body)

    if isinstance(body, (dict, list)):
        return body

    return None


def request(playwright: Playwright, url: str,
            method: Literal["GET", "POST", "PUT", "DELETE"],
            body: Optional[Union[str, dict]] = None,
            status_code_expected: int = 200) -> Any | None:

    final_url = urljoin(ctx.api_host, url=url)
    data = __get_json_body(body)
    headers = {"Content-Type": "application/json",
               "x-api-key": "reqres-free-v1"}

    req = playwright.request.new_context(base_url=ctx.api_host, extra_http_headers=headers)

    method_func = {
        "GET": req.get,
        "POST": req.post,
        "PUT": req.put,
        "DELETE": req.delete
    }[method]

    request_args = {
        "url": final_url,
        "headers": headers,
        "max_retries": 5
    }
    if method not in ["GET", "DELETE"]:
        request_args["data"] = data

    res: APIResponse = method_func(**request_args)

    assert res.status == status_code_expected, f"Invalid status code received: {res.status} - {res.status_text}."
    try:
        return res.json()
    except:
        return None


def parse_json(json_body, path) -> list:

    expr = parse(path)

    matches = [match.value for match in expr.find(json_body)]

    return matches