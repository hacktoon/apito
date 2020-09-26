from urllib.parse import urljoin
from .http import HTTPRequest

TIMEOUT_SEC = 2


class APIClient:
    def __init__(self, name, base_url, headers={}):
        self.name = name
        self.base_url = base_url
        self.headers = headers

    def get(self, path, **kwargs):
        return self._request('GET', path, **kwargs)

    def _request(self, method, path, **kwargs):
        url = urljoin(self.base_url, path)
        #  TODO: get endpoint by name
        request = HTTPRequest(method, url, timeout=TIMEOUT_SEC)
        response = request.send()
        return response
