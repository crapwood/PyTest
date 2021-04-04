from django.db import models
import requests
import json


# Create your models here.
class Bot(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    credentials = models.IntegerField(default=0)

    def is_bot_in_db(self, name):
        flag = False
        url = 'http://127.0.0.1:8000/myapp/'
        headers = {'content-type': 'application/json'}
        r = requests.get(url)
        data = r.json()
        for bot in data:
            if data[bot]['name'] == name:
                flag = True
        return flag


