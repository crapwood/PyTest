from django.urls import reverse, resolve
from myapp.models import Bot
import pytest
import requests


@pytest.mark.django_db
class Testing:

    def test_url_index(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'

    def test_get_method(self):
        temp_data = {
            "name": "Bot 1",
            "display_name": "Bot A",
            "provider": "Client A",
            "credentials": 1
        }
        url = 'http://127.0.0.1:8000/myapp/'
        r = requests.post(url, json=temp_data)
        assert Bot.is_bot_in_db(Bot, name='Bot 1') == True

    def test_post_method(self):
        temp_data = {
            "name": "Bot 2",
            "display_name": "Bot B",
            "provider": "Client B",
            "credentials": 1
        }
        url = 'http://127.0.0.1:8000/myapp/'
        r = requests.post(url, json=temp_data)
        assert Bot.is_bot_in_db(Bot, name='Bot 2') == True

    def test_put_method(self):
        temp_data = {
            "name": "Bot 2",
            "display_name": "Bot B",
            "provider": "Client C",
            "credentials": 1
        }
        url = 'http://127.0.0.1:8000/myapp/'
        r = requests.put(url, json=temp_data)
        assert Bot.is_bot_in_db(Bot, name='Bot 2') == True

    def test_delete_method(self):
        temp_data = {
            "name": "Bot 1",
        }
        url = 'http://127.0.0.1:8000/myapp/'
        r = requests.delete(url, json=temp_data)
        assert Bot.is_bot_in_db(Bot, name='Bot 1') == False