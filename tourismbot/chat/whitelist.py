import json
import requests
from pprint import pprint
import views

page_access_token = 'EAAIwxSTcnu0BALz1yGvBSgnwXgwEQuv6IVoHmob6VYHni2EqCYSWYdZA3oM9e64tZBbeC5tn94mdvHZAoJzKhwzN9Thj8d3cYHzkSTgsbijEGhhZAh6msbG5i5y1eKX7xq6I3t0QPf8owXKhdbdJZAjLrhvZCoS7ZCHqBTgthRBlwZDZD'
ngrokurl = views.ngrokurl
fbid = 1297251120321401

def whitelistdomain(fbid, page_access_token):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messenger_profile?access_token=' + page_access_token
    response_message = json.dumps({"whitelisted_domains" : [ngrokurl],"recipient": fbid})
    print('----')
    print(response_message)
    status = requests.post(post_message_url, headers = {'Content-Type': 'application/json'}, data=response_message)
    pprint(status.json())
    return

whitelistdomain(fbid, page_access_token)
