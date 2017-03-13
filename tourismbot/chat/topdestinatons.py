import json
import requests
from pprint import pprint

def topdestinations(fbid, ngrokurl, page_access_token):
    pprint('---Starting generichorizontaltemplate----')
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + page_access_token

    response_msg = json.dumps({
            "recipient": {"id": fbid},
            "message":{
                "attachment":{
                  "type":"template",
                  "payload":{
                    "template_type":"generic",
                    "elements":[
                       {
                        "title":"College of Engineering",
                        "image_url":ngrokurl+"/media/1_iZey8Q8.jpg",
                        "subtitle":"Here lies the great computer engineering students",
                        "default_action": {
                          "type": "web_url",
                          "url": ngrokurl,
                          "messenger_extensions": True,
                          "webview_height_ratio": "tall",
                          "fallback_url": ngrokurl
                        },
                        "buttons":[
                          {
                            "type":"postback",
                            "title":"LEARN MORE",
                            "payload":"ABOUT_CEA"
                          },{
                            "type":"postback",
                            "title":"BOOK NOW",
                            "payload":"BOOK_CEA"
                          },

                        ]
                      },

                        {
                            "title": "Puerto Princessa",
                            "image_url": ngrokurl + "/media/3.JPG",
                            "subtitle": "Paddling through the navigable portion of the 8.2-kilometer Underground River",
                            "default_action": {
                                "type": "web_url",
                                "url": ngrokurl,
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": ngrokurl
                            },
                            "buttons": [
                                {
                                    "type":"postback",
                                    "title":"LEARN MORE",
                                    "payload":"ABOUT_PRINCESSA"
                                }, {
                                    "type":"postback",
                                    "title":"BOOK NOW",
                                    "payload":"BOOK_PRINCESSA"
                                },

                            ]
                        },
                        {
                            "title": "Boracay",
                            "image_url": ngrokurl + "/media/4_FIsSF25.jpg",
                            "subtitle": "Our mission is to connect tourists and businesses to Boracay Island",
                            "default_action": {
                                "type": "web_url",
                                "url": ngrokurl,
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": ngrokurl
                            },
                            "buttons": [
                                {
                                    "type":"postback",
                                    "title":"LEARN MORE",
                                    "payload":"ABOUT_BORACAY"
                                }, {
                                    "type":"postback",
                                    "title":"BOOK NOW",
                                    "payload":"BOOK_BORACAY"
                                },

                            ]
                        },

                        {
                            "title": "El Nido",
                            "image_url": ngrokurl + "/media/1_vbuum73.jpg",
                            "subtitle": "It is a Philippine municipality on Palawan. Famous for its white-sand beaches",
                            "default_action": {
                                "type": "web_url",
                                "url": ngrokurl,
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": ngrokurl
                            },
                            "buttons": [
                                {
                                    "type":"postback",
                                    "title":"LEARN MORE",
                                    "payload":"ABOUT_NIDO"
                                }, {
                                    "type":"postback",
                                    "title":"BOOK NOW",
                                    "payload":"BOOK_NIDO"
                                },

                            ]
                        },

                        {
                            "title": "Puerto Galera",
                            "image_url": ngrokurl + "/media/1.jpg",
                            "subtitle": "Puerto Galera is a soothing vision of shimmering seas surrounded by lush mountains.",
                            "default_action": {
                                "type": "web_url",
                                "url": ngrokurl,
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": ngrokurl
                            },
                            "buttons": [
                                {
                                    "type":"postback",
                                    "title":"LEARN MORE",
                                    "payload":"ABOUT_GALERA"
                                }, {
                                    "type":"postback",
                                    "title":"BOOK NOW",
                                    "payload":"BOOK_GALERA"
                                },

                            ]
                        },
                    ]
                  }
                }
              }
            })
    pprint(response_msg)
    status = requests.post(post_message_url, headers={"Content-Type" : "application/json"}, data = response_msg)
    pprint(status.json())
    return
