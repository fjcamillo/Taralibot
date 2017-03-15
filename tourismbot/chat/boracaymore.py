import json
import requests
from pprint import pprint

def boracaymore(fbid, ngrokurl, page_access_token):
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
                        "title":"Boracay",
                        "image_url":ngrokurl+"/media/2_vDusXpE.jpg",
                        "subtitle":"Here lies the greatest beach of all time",
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
                            "payload":"ABOUT_BORACAY"
                          },{
                            "type":"postback",
                            "title":"BOOK NOW",
                            "payload":"BOOK_BORACAY"
                          },

                        ]
                      },

                        {
                            "title": "Boracay",
                            "image_url": ngrokurl + "/media/3_zLPCdDy.jpg",
                            "subtitle": "Here lies the greatest beach of all time",
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
                            "title": "Boracay",
                            "image_url": ngrokurl + "/media/4_L7DBtb1.jpg",
                            "subtitle": "Here lies the greatest beach of all time",
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
                            "title": "Boracay",
                            "image_url": ngrokurl + "/media/5_BUi6R7J.jpg",
                            "subtitle": "Here lies the greatest beach of all time",
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
                            "title": "Boracay",
                            "image_url": ngrokurl + "/media/5_BUi6R7J.jpg",
                            "subtitle": "Here lies the greatest beach of all time",
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
                    ]
                  }
                }
              }
            })
    pprint(response_msg)
    status = requests.post(post_message_url, headers={"Content-Type" : "application/json"}, data = response_msg)
    pprint(status.json())
    return
