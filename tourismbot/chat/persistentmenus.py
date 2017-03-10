import json
import requests
from pprint import pprint


class persistentmenu:

    def __init__(self, fbid, page_access_token):
        self.fbid = fbid
        self.page_access_token = page_access_token

    def persistent_mainmenu(self, fbid, page_access_token):
        post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=' + page_access_token
        persistent = json.dumps({
            "setting_type": "call_to_actions",
            "thread_state": "existing_thread",
            "call_to_actions": [
                {
                    "type": "postback",
                    "title": "Main Menu",
                    "payload": "MAIN_MENU"
                },
                {
                    "type": "postback",
                    "title": "Get Location",
                    "payload": "GET_LOCATION"
                },
                {
                    "type": "postback",
                    "title": "Top Destinations",
                    "payload": "TOP_DESTINATION"
                },
                {
                    "type": "postback",
                    "title": "Stories",
                    "payload": "STORIES"
                },
                {
                    "type": "postback",
                    "title": "Subscriptions",
                    "payload": "SUBSCRIPTIONS"
                },
            ],
            "recipient": fbid
        })
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=persistent)
        pprint(status.json())
        return

    def persistent_specific(self, fbid, page_access_token, destination_name):
        post_message_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=' + page_access_token
        persistent = json.dumps({
            "setting_type": "call_to_actions",
            "thread_state": "existing_thread",
            "call_to_actions": [
                {
                    "type": "postback",
                    "title": "Main Menu",
                    "payload": "MAIN_MENU"
                },
                {
                    "type": "postback",
                    "title": "Get Location",
                    "payload": "GET_LOCATION"
                },
                {
                    "type": "postback",
                    "title": "Top Destinations",
                    "payload": "TOP_DESTINATION"
                },
                {
                    "type": "postback",
                    "title": "Stories",
                    "payload": "STORIES"
                },
                {
                    "type": "postback",
                    "title": "Subscriptions",
                    "payload": "SUBSCRIPTIONS"
                },
            ],
            "recipient": fbid
        })
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=persistent)
        pprint(status.json())
        return

