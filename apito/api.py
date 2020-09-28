from functools import cached_property
from .http import HTTPMethod


class APIClient:
    def __init__(self, name, url, headers={}):
        self.name = name
        self.url = url
        self.headers = headers

    @cached_property
    def get(self):
        return self._endpoints.get(method=HTTPMethod.GET)

    @cached_property
    def _endpoints(self):
        return Endpoints([
            subcls(self)
            for subcls in ApiEndpoint.__subclasses__()
        ])


class Endpoints:
    def __init__(self, endpoints):
        self.endpoints = endpoints

    def get(self, method):
        NotImplementedError


class ApiEndpoint:
    def __init__(self, api):
        self.api = api

    def request(self):
        raise NotImplementedError

    def url(self):
        return self.api.url

    def payload(self):
        return {}

    def sanitize(self):
        return True
