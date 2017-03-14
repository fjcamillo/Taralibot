import json
import requests
from pprint import pprint

def galeramore(fbid, ngrokurl, page_access_token):
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
                        "title":"Puerto Galera",
                        "image_url":ngrokurl+"/media/1_KHX56ZQ.jpg",
                        "subtitle":"Here lives the greatest puerto of them all",
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
                            "payload":"ABOUT_GALERA"
                          },{
                            "type":"postback",
                            "title":"BOOK NOW",
                            "payload":"BOOK_GALERA"
                          },

                        ]
                      },

                        {
                            "title": "Puerto Galera",
                            "image_url": ngrokurl + "/media/2_BACb51O.jpg",
                            "subtitle": "Here lives the greatest puerto of them all",
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
                        {
                            "title": "Puerto Galera",
                            "image_url": ngrokurl + "/media/3_0ULWlC3.jpg",
                            "subtitle": "Here lives the greatest puerto of them all",
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

                        {
                            "title": "Puerto Galera",
                            "image_url": ngrokurl + "/media/4_S9b7zS2.jpg",
                            "subtitle": "Here lives the greatest puerto of them all",
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

                        {
                            "title": "Puerto Galera",
                            "image_url": ngrokurl + "/media/5_j4KV3Zt.jpg",
                            "subtitle": "Here lives the greatest puerto of them all",
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
