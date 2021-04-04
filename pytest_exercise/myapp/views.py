from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Bot
import json


@csrf_exempt
def index(request):
    response = {}
    if request.body:
        body = json.loads(request.body.decode('utf-8'))

    if request.method == "GET":
        data_in_db = {}
        count = 0
        for x in Bot.objects.filter():
            data_in_db[f"{count}"] = {
                'name': x.name,
                'display_name': x.display_name,
                'provider': x.provider,
                'credentials': x.credentials
            }
            count += 1
        response = data_in_db

    elif request.method == "POST":
        try:
            bot = Bot(name=body['name'], display_name=body['display_name'], provider=body['provider'],
                      credentials=body['credentials'])
            bot.save()
            response.update({'POST': 'HTTP POST Successful New Data Added'})
        except:
            response.update({'POST': 'HTTP POST Unsuccessful Data supplied is invalid'})

    elif request.method == "PUT":
        try:
            update_bot = Bot.objects.get(name=body['name'])
            update_bot.name = body['name']
            update_bot.display_name = body['display_name']
            update_bot.provider = body['provider']
            update_bot.credentials = body['credentials']
            update_bot.save()
            response.update({'PUT': 'HTTP PUT Successful'})
        except:
            try:
                update_bot = Bot(name=body['name'], display_name=body['display_name'], provider=body['provider'],
                                 credentials=body['credentials'])
                update_bot.save()
                response.update({'PUT': 'HTTP PUT Successful New Data Added'})
            except:
                response.update({'PUT': 'HTTP PUT Unsuccessful fields are missing on the data sent'})

    elif request.method == "PATCH":
        response.update({'PATCH': 'HTTP PATCH Successful'})
    else:
        # TODO for now delete method works only with name attribute to delete the data within the DB
        try:
            Bot.objects.get(name=body['name']).delete()
            response.update({'DELETE': 'Successful'})
        except:
            response.update({'DELETE': 'Unsuccessful'})

    return JsonResponse(response)
