
import requests
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from app import app
import pytest

    
    
class TestFlaskEndpoints:
    @pytest.fixture
    def client(self):
        app.testing = True
        with app.test_client() as client:
            yield client
    
    def test_ping_home_page(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_ping_inventory_page(self, client):
        response = client.get('/inventory')
        assert response.status_code == 200
    
    def test_ping_delete_page(self,client):
        response = client.get('/inventory/delete')
        assert response.status_code == 200
    
    def test_ping_display_page(self,client):
        response = client.get('/inventory/display')
        assert response.status_code == 200
    def test_ping_add_page(self,client):
        response = client.get('/inventory/add')
        assert response.status_code == 200
    def test_ping_search_page(self,client):
        response = client.get('/inventory/search')
        assert response.status_code == 200