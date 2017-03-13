import json
import requests
from pprint import pprint

def mainmenu(fbid, ngrokurl, page_access_token):
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
                        "title":"Official TaraliBot AI-Chat",
                        "image_url":ngrokurl+"/media/Taralibot_Logo_9nqwFVd.png",
                        "subtitle":"Share the world around you",
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
                            "title":"MANAGE SUBSCRIPTIONS"
                          },{
                            "type":"postback",
                            "title":"ABOUT THIS BOT",
                            "payload":"ABOUT_US"
                          },

                        ]
                      },

                        {
                            "title": "Learn about our best seller",
                            "image_url": ngrokurl + "/media/1.jpg",
                            "subtitle": "Know more about the best",
                            "default_action": {
                                "type": "web_url",
                                "url": ngrokurl,
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": ngrokurl
                            },
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "SHOW",
                                    "payload":"SHOW_BEST"
                                }, {
                                    "type": "postback",
                                    "title": "SUBSCRIBE",
                                    "payload": "SUBSCRIBE"
                                },

                            ]
                        },
                        {
                            "title": "Latest Headlines",
                            "image_url": ngrokurl + "/media/1.jpg",
                            "subtitle": "Know more about the Philippines Tourism",
                            "default_action": {
                                "type": "web_url",
                                "url": ngrokurl,
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": ngrokurl
                            },
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "SHOW",
                                    "payload": "SHOW_HEADLINES"
                                }, {
                                    "type": "postback",
                                    "title": "BLOG",
                                    "payload": "BLOG"
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
