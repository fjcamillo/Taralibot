import json
import requests
from pprint import pprint

def bookreceipt(fbid, ngrokurl, page_access_token):
    pprint('---Starting generichorizontaltemplate----')

    payload = {
        "recipient": {
            "id": fbid
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "receipt",
                    "recipient_name": "Francisc Camillo",
                    "order_number": "12345678902",
                    "currency": "PHP",
                    "payment_method": "Visa 2345",
                    "order_url": ngrokurl,
                    "timestamp": "1428444852",
                    "elements": [
                        {
                            "title": "CpE Resort for two",
                            "subtitle": "100% Happiness",
                            "quantity": 2,
                            "price": 50,
                            "currency": "USD",
                            "image_url": ngrokurl + "/media/5_BUi6R7J.jpg"
                        },
                        {
                            "title": "Snorkelling",
                            "subtitle": "100% Happiness",
                            "quantity": 1,
                            "price": 25,
                            "currency": "USD",
                            "image_url": ngrokurl + "/media/4_L7DBtb1.jpg"
                        }
                    ],
                    "address": {
                        "street_1": "Anonas",
                        "street_2": "Corner Pureza",
                        "city": "Manila City",
                        "postal_code": "1300",
                        "state": "NCR",
                        "country": "PH"
                    },
                    "summary": {
                        "subtotal": 75.00,
                        "shipping_cost": 4.95,
                        "total_tax": 6.19,
                        "total_cost": 56.14
                    },
                    "adjustments": [
                        {
                            "name": "New Customer Discount",
                            "amount": 20
                        },
                        {
                            "name": "$10 Off Coupon",
                            "amount": 10
                        }
                    ]
                }
            }
        }
    }

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + page_access_token

    response_msg = json.dumps(payload)
    pprint(response_msg)
    status = requests.post(post_message_url, headers={"Content-Type" : "application/json"}, data = response_msg)
    pprint(status.json())
    return