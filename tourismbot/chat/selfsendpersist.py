import json
import requests
from pprint import pprint

fbid = 1297251120321401
page_access_token = 'EAAIwxSTcnu0BALz1yGvBSgnwXgwEQuv6IVoHmob6VYHni2EqCYSWYdZA3oM9e64tZBbeC5tn94mdvHZAoJzKhwzN9Thj8d3cYHzkSTgsbijEGhhZAh6msbG5i5y1eKX7xq6I3t0QPf8owXKhdbdJZAjLrhvZCoS7ZCHqBTgthRBlwZDZD'

def persistent_mainmenu(fbid, page_access_token):
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

persistent_mainmenu(fbid, page_access_token)