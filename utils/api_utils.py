import json
from typing import Literal, Optional, Union, Any
from urllib.parse import urljoin
from jsonpath_ng import parse
from utils import ctx, log
import requests
import responses

def __get_json_body(body):
    if not body:
        log.error("Empty payload provided.")
        raise Exception("Empty payload provided.")
    if isinstance(body, str):

        if body.endswith(".json"):
            with open(f"{ctx.project_root}/payloads/{body}") as f:
                return json.load(f)
        else:
            return json.loads(body)

    if isinstance(body, (dict, list)):
        return body

    return None


def request( url: str,
            method: Literal["GET", "POST", "PUT", "DELETE"],
            body: Optional[Union[str, dict]] = None,
            status_code_expected: int = 200,
            mock: bool=False,
            response_json: Optional[Union[str, dict]]= None
            ) -> Any | None:


    final_url = urljoin(ctx.api_host, url=url)
    data = None
    if method not in ["GET", "DELETE"]:
        data = __get_json_body(body)

    headers = {"Content-Type": "application/json",
               "x-api-key": "reqres-free-v1"}

    if mock:
        res: requests.Response= mock_response(url="/api/users",
                            method="POST",
                            body=data,
                            status_code_expected=201)
    else:
        res: requests.Response = requests.request(url=final_url,
                                                  method=method,
                                                  headers=headers,
                                                  data=data)

    assert res.status_code == status_code_expected, f"Invalid status code received: {res.status_code} - {res.text}."
    try:
        return res.json()
    except:
        return None

@responses.activate
def mock_response(url: str,
                    method: Literal["GET", "POST", "PUT", "DELETE"],
                    body: Optional[Union[str, dict]] = None,
                    status_code_expected: int = 200,
                    response_json: Optional[Union[str, dict]]= None
            ) -> Any | None:

    responses.add(
        method=method,
        url=url,
        json=response_json,
        status=status_code_expected,
    )

    return requests.request(url="https://api.example.com/users", method=method, json=body)



def parse_json(json_body, path) -> list:

    expr = parse(path)

    matches = [match.value for match in expr.find(json_body)]

    return matches