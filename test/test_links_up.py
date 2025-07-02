

import requests
class TestLinks:
    def test_dummy(self):
        assert 1== 1
        
    import requests

    def test_ping(self):
        try:
            response = requests.head('http://localhost:5000')
        except requests.ConnectionError:
            assert False, "Connection Error"
        assert response.status_code == 200
    def test_ping_google(self):
        try:
            response = requests.head('https://www.google.co.in')
        except requests.ConnectionError:
            assert False, "Connection Error"
        assert response.status_code == 200