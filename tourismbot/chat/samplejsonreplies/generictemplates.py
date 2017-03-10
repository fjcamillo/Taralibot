import json
import requests
from pprint import pprint

class generate:

    def __init__(self, fbid=" ", message=" ", page_access_token = 'EAAIwxSTcnu0BALz1yGvBSgnwXgwEQuv6IVoHmob6VYHni2EqCYSWYdZA3oM9e64tZBbeC5tn94mdvHZAoJzKhwzN9Thj8d3cYHzkSTgsbijEGhhZAh6msbG5i5y1eKX7xq6I3t0QPf8owXKhdbdJZAjLrhvZCoS7ZCHqBTgthRBlwZDZD'):
        self.fbid = fbid
        self.message = message
        self.page_access_token = page_access_token

    def generichorizontaltemplate(self):
        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + self.page_access_token

        # response = {
        #     'recipient': {'id': self.fbid},
        #     'message':{
        #         'attachment':{
        #             'type':'template',
        #             'payload':
        #         }
        #     }
        # }

        response_msg = {
            "recipient":{"id": self.fbid},
            "message":{
                "attachment":{
                  "type":"template",
                  "payload":{
                    "template_type":"generic",
                    "elements":[
                       {
                        "title":"Welcome to Peter\'s Hats",
                        "image_url":"https://petersfancybrownhats.com/company_image.png",
                        "subtitle":"We\'ve got the right hat for everyone.",
                        "default_action": {
                          "type": "web_url",
                          "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
                          "messenger_extensions": True,
                          "webview_height_ratio": "tall",
                          "fallback_url": "https://peterssendreceiveapp.ngrok.io/"
                        },
                        "buttons":[
                          {
                            "type":"web_url",
                            "url":"https://petersfancybrownhats.com",
                            "title":"View Website"
                          },{
                            "type":"postback",
                            "title":"Start Chatting",
                            "payload":"DEVELOPER_DEFINED_PAYLOAD"
                          }
                        ]
                      }
                    ]
                  }
                }
              }
            }
        pprint(response_msg)
        status = requests.post(post_message_url, headers={"Content-Type" : "application/json"}, data = response_msg)
        pprint(status.json())
        return