import json

from tests.bases import BaseTestCase


class TestAuth(BaseTestCase):
    """
    Tests if all the endpoints are working correctly.
    """
    def test_authentication_missing_auth_header_raises(self):
        url_methods = [
            ('/energy/water', "GET"),
            ('/energy/water', "POST"),

            ('/energy/water/1', "PUT"),
            ('/energy/water/1', "DELETE"),

            ('/energy/gas', "GET"),
            ('/energy/gas', "POST"),

            ('/energy/gas/1', "PUT"),
            ('/energy/gas/1', "DELETE"),

            ('/energy/electricity', "GET"),
            ('/energy/electricity', "POST"),
            #
            ('/energy/electricity/1', "PUT"),
            ('/energy/electricity/1', "DELETE"),

            ('/energy/compressors', "GET"),
            ('/energy/compressors', "POST"),

            ('/energy/compressors/1', "PUT"),
            ('/energy/compressors/1', "DELETE"),

            ('/role_change/1', "PUT")
        ]

        for url, method in url_methods:
            if method == "GET":
                resp = self.client.get(url)
            elif method == "POST":
                resp = self.client.post(url, data=json.dumps({}))
            elif method == "PUT":
                resp = self.client.put(url, data=json.dumps({}))
            else:
                resp = self.client.delete(url)

            assert resp.status_code == 400
            # assert resp.json == {'message': 'Invalid Token'}