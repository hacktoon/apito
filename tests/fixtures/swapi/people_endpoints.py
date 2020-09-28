from apito.api import ApiEndpoint
from apito.http import HTTPMethod


class PeopleEndpoint(ApiEndpoint):
    name = 'people'
    method = HTTPMethod.GET

    def url(self, id):
        return f'people/{id}'

    def request(self, **kwargs):
        method = self._api_method(self.method)
        return method(self.url(''))

    def payload(self, domain, csr):
        return {'validations': {}}

    def validate(self):
        return True
