from behave import *
from behave.runner import Context
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.main import app

use_step_matcher("re")


class FastApiContext(object):
    def __init__(self, my_app: FastAPI):
        self.client = TestClient(my_app)
        self.response = None


def assert_fastapi_context_initialized(context):
    try:
        context.fastapi
    except:
        context.fastapi = FastApiContext(app)


def call_api(fastapi_context: FastApiContext, method: str, url: str, body: str | None = None):
    method_call = getattr(fastapi_context.client, method.lower())
    if method.lower() == "get":
        fastapi_context.response = method_call(url=url)
    else:
        fastapi_context.response = method_call(url=url, data=body)


@when("I make a (?P<method>.+) request to (?P<url>.+) with body")
def make_request_to_url_with_body(context: Context, method: str, url: str):
    assert_fastapi_context_initialized(context)
    call_api(context.fastapi, method=method, url=url, body=context.text)


@when("I make a (?P<method>.*) request to (?P<url>.*)")
def make_request_to_url(context, method: str, url: str):
    assert_fastapi_context_initialized(context)
    call_api(context.fastapi, method=method, url=url)


@then("the response status code is (?P<status>.*)")
def response_status_is(context, status: str):
    response = context.fastapi.response
    assert response is not None
    assert response.status_code == int(status), "Expected " + str(status) + " and given " + str(response.status_code)


@then("the response message is (?P<message>.*)")
def response_message_is(context, message: str):
    response = context.fastapi.response
    assert response is not None
    assert response.json() == {"message": message}


use_step_matcher("parse")
