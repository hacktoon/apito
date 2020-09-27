import logging

from functools import cached_property
from .http import HTTPMethod


TIMEOUT_SEC = 2


class APIClient:
    def __init__(self, name, url, headers={}):
        self.name = name
        self.url = url
        self.headers = headers
        self.get = Endpoints(HTTPMethod.GET)
        self.post = Endpoints(HTTPMethod.POST)
        self.put = Endpoints(HTTPMethod.PUT)
        self.delete = Endpoints(HTTPMethod.DELETE)

    @cached_property
    def endpoints(self):
        subclasses = ApiEndpoint.__subclasses__()
        return [
            cls(self, cls.method, cls.name)
            for cls in subclasses
        ]


class Endpoints:
    def __init__(self, method):
        self.method = method

    def get(self, method):
        if method not in self._map:
            logging.error(f'Method "{method}" not implemented.')
        return self._map.get(method)


class ApiEndpoint:
    def __init__(self, api, method, name):
        self.api = api
        self.method = method
        self.name = name

    def request(self, method):
        self.url = self.api_url + method.url
        self.payload()
        self.method(self.url)

    def url(self, cert_type):
        return f'order/certificate/{cert_type}'

    def payload(self, domain, csr):
        return {}

    def validate(self):
        return True

    def filter(self):
        return True
