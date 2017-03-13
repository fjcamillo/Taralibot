from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import generic
from django.http import HttpResponse
import requests
from pprint import pprint
import json
import datetime
# from . import replierfunc
# from .persistentmenus import persistentmenu
# from .generictemplates import generate


verify_token = '5244680129'
ngrokurl = 'https://5b3b8ef5.ngrok.io'
page_access_token = 'EAAIwxSTcnu0BALz1yGvBSgnwXgwEQuv6IVoHmob6VYHni2EqCYSWYdZA3oM9e64tZBbeC5tn94mdvHZAoJzKhwzN9Thj8d3cYHzkSTgsbijEGhhZAh6msbG5i5y1eKX7xq6I3t0QPf8owXKhdbdJZAjLrhvZCoS7ZCHqBTgthRBlwZDZD'
post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+page_access_token
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
        if 'entry' in incoming_message:
            for entry in incoming_message['entry']:
                for message in entry['messaging']:

                    # gen = generate(fbid=message['sender']['id'], page_access_token=page_access_token)
                    # gen.generichorizontaltemplate(gen.fbid, gen.page_access_token)
                    # whitelistdomain(message['sender']['id'], page_access_token)
                    generichorizontaltemplate(message['sender']['id'], page_access_token)

                    firstname = getName(message['sender']['id'], page_access_token)['first_name']

                    # mainmenu = persistentmenu(message['sender']['id'], page_access_token)
                    # mainmenu.persistent_mainmenu(mainmenu.fbid, mainmenu.page_access_token)

                    send_message = "Hi {}, Thank You, for trying out TaraliBot. I will now echo your message: {}".format(
                        firstname, message['message']['text'])
                    post_facebook_messages(message['sender']['id'], send_message)
                    # location_reply(message['sender']['id'], message)
        else: pass
        return HttpResponse()

def whitelistdomain(fbid, page_access_token):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messenger_profile?access_token=' + page_access_token
    response_message = json.dumps({
        # "setting_type" : "domain_whitelisting",
        "whitelisted_domains" : [ngrokurl],
        # "domain_action_type": "add",
        "recipient": fbid
             # {"id": fbid}
    })
    print('----')
    print(response_message)
    status = requests.post(post_message_url, headers = {'Content-Type'  : 'application/json'}, data=response_message)
    pprint(status.json())
    return


def location_button(fbid, received_messages):
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

def generichorizontaltemplate(fbid, page_access_token):
    pprint('---Starting generichorizontaltemplate----')
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + page_access_token
    # response = {
    #     'recipient': {'id': self.fbid},
    #     'message':{
    #         'attachment':{
    #             'type':'template',
    #             'payload':
    #         }
    #     }
    # }

    response_msg = json.dumps({
            "recipient": {"id": fbid},
            "message":{
                "attachment":{
                  "type":"template",
                  "payload":{
                    "template_type":"generic",
                    "elements":[
                       {
                        "title":"Welcome to Peter\'s Hats",
                        "image_url":ngrokurl+"/media/1.jpg",
                        "subtitle":"We\'ve got the right hat for everyone.",
                        "default_action": {
                          "type": "web_url",
                          "url": ngrokurl,
                          "messenger_extensions": True,
                          "webview_height_ratio": "tall",
                          "fallback_url": ngrokurl
                        },
                        "buttons":[
                          {
                            "type":"web_url",
                            "url":ngrokurl,
                            "title":"View Website"
                          },{
                            "type":"postback",
                            "title":"Start Chatting",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                          },

                        ]
                      },
                        {
                            "title": "Welcome to Peter\'s Hats",
                            "image_url": ngrokurl + "/media/1.jpg",
                            "subtitle": "We\'ve got the right hat for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": ngrokurl,
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": ngrokurl
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": ngrokurl,
                                    "title": "View Website"
                                }, {
                                    "type": "postback",
                                    "title": "Start Chatting",
                                    "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                },

                            ]
                        },
                        {
                            "title": "Welcome to Peter\'s Hats",
                            "image_url": ngrokurl + "/media/1.jpg",
                            "subtitle": "We\'ve got the right hat for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": ngrokurl,
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": ngrokurl
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": ngrokurl,
                                    "title": "View Website"
                                }, {
                                    "type": "postback",
                                    "title": "Start Chatting",
                                    "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                },

                            ]
                        }
                    ]
                  }
                }
              }
            })
    pprint(response_msg)
    status = requests.post(post_message_url, headers={"Content-Type" : "application/json"}, data = response_msg)
    pprint(status.json())
    return


def getName(fbid, page_access_token):
    """
    Sample Get API Access
    https://graph.facebook.com/v2.6/<USER_ID>?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token=PAGE_ACCESS_TOKEN
    :param fbid:
    :param page_access_token:
    :return:
    """
    post_message_url = 'https://graph.facebook.com/v2.6/'+fbid+'?fields=first_name,last_name&access_token='+page_access_token
    status = requests.get(post_message_url)
    pprint(status.json())
    return status.json()

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
