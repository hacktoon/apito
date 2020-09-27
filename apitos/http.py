# coding: utf-8

import json

from enum import Enum
from requests import (
    Request,
    Session,
    HTTPError,
    Timeout,
    ConnectionError,
    RequestException,
)
from urllib.parse import urljoin


class HTTPSession:
    pass


class HTTPRequest:
    def __init__(self, method, url, timeout=1, headers={}):
        self.method = method
        self.url = url
        self.headers = headers
        self.timeout = timeout

    def send(self, **kwargs):
        data = json.dumps(kwargs.get('data', {}))  # TODO: handle client input
        headers = {**self.headers, **kwargs.get('headers', {})}
        request = Request(self.method, self.url, headers=headers, data=data)
        session = Session()
        try:
            prepared_request = request.prepare()
            response = session.send(prepared_request, timeout=self.timeout)
            response.raise_for_status()
            message = response.reason
        except HTTPError as err:
            message, response = err.response.reason, err.response
        except Timeout as err:
            message, response = 'Timeout error', err.response
        except ConnectionError as err:
            message, response = 'Connection error', err.response
        except RequestException as err:
            message, response = 'Request error', err.response

        return HTTPResponse(request, response, message)

    def _request(self, method, path, **kwargs):
        url = urljoin(self.base_url, path)
        #  TODO: get endpoint by name
        request = HTTPRequest(method, url, timeout=3)
        response = request.send()
        return response


class HTTPResponse:
    def __init__(self, request, response, message):
        self.request = request
        self.response = response
        self.url = request.url
        self.method = request.method
        self.message = message

    def __bool__(self):
        return self.response is not None and self.response.ok

    @property
    def text(self):
        return self.response.text if bool(self) else ''

    @property
    def status(self):
        return 0 if self.response is None else self.response.status_code

    def __repr__(self):
        return f'{self.method} {self.url} => {self.status} {self.message}'


class HTTPMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'

    def __repr__(self):
        return self.name
