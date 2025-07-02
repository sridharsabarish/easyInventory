def test_dummy():
    assert 1== 1
    
import requests

def test_ping():
    try:
        response = requests.head('http://localhost:5000')
    except requests.ConnectionError:
        assert False, "Connection Error"
    assert response.status_code == 200
