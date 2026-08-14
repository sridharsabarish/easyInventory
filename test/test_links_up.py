
import pytest
import requests

test_input = ["https://www.google.co.in","https://www.bbc.com/news"]
class TestLinks:        
    @pytest.mark.parametrize("url",test_input)
    def test_internet_connection(self,url):
        try:
            response = requests.head(url)
        except requests.ConnectionError:
            assert False, "Connection Error"
        assert response.status_code == 200