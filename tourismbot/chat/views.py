from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import generic
from django.http import HttpResponse
import requests
from pprint import pprint
import json
import datetime
from . import replierfunc
from .persistentmenus import persistentmenu

verify_token = '5244680129'

page_access_token = 'EAAIwxSTcnu0BALz1yGvBSgnwXgwEQuv6IVoHmob6VYHni2EqCYSWYdZA3oM9e64tZBbeC5tn94mdvHZAoJzKhwzN9Thj8d3cYHzkSTgsbijEGhhZAh6msbG5i5y1eKX7xq6I3t0QPf8owXKhdbdJZAjLrhvZCoS7ZCHqBTgthRBlwZDZD'

class index(generic.View):

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == verify_token:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error', 'Invalid Token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        pprint("\n=============INITIAL JSON RETURN================")
        pprint(incoming_message)
        pprint("\n=============INITIAL JSON RETURN================")
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                mainmenu = persistentmenu(message['sender']['id'], page_access_token)
                mainmenu.persistent_mainmenu(mainmenu.fbid, mainmenu.page_access_token)
                post_facebook_messages(message['sender']['id'], message['message']['text'])
                # location_reply(message['sender']['id'], message)
        return HttpResponse()

def post_facebook_messages(fbid, received_messages):
    """
    :param fbid: Facebook User ID
    :param received_messages: Message Received Sent by Facebook User ID
    :return:
    """
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+page_access_token

    response_msg = json.dumps(
        {"recipient":
             {"id": fbid},
         "message":
             {"text": received_messages}
         })

    print('-----')
    print(response_msg)
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    pprint(status.json())
    return

def receive_postback(fbid):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+page_access_token
    return

def location_reply(fbid, received_messages):
    """
    :param fbid: Facebook User ID
    :param received_messages: Message Received Sent by Facebook User ID
    :return:
    """
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+page_access_token
    latitude = []
    longitude = []
    msg = received_messages['message']
    for attach in msg['attachments']:
        latitude.append(attach['payload']['coordinates']['lat'])
        longitude.append(attach['payload']['coordinates']['long'])

    response_msg = json.dumps(
        {'recipient':
             {'id':fbid},
         'message':
             {'text':
                  "Coordinates: "+str(latitude[0])+","+str(longitude[0])}})

    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    pprint(status.json())
    return
