import json
import requests
from pprint import pprint
import datetime

def today():
    return datetime.datetime.now()

def flight(fbid, ngrokurl, page_access_token):
    pprint('---Starting generichorizontaltemplate----')
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + page_access_token

    payload = {
        "recipient": {
            "id": fbid
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "airline_boardingpass",
                    "intro_message": "You are checked in.",
                    "locale": "en_US",
                    "boarding_pass": [
                        {
                            "passenger_name": "FRANCISC CAMILLO",
                            "pnr_number": "CG4X7U",
                            "travel_class": "business",
                            "seat": "74J",
                            "auxiliary_fields": [
                                {
                                    "label": "Terminal",
                                    "value": "T1"
                                },
                                {
                                    "label": "Departure",
                                    "value": "30OCT 19:05"
                                }
                            ],
                            "secondary_fields": [
                                {
                                    "label": "Boarding",
                                    "value": "18:30"
                                },
                                {
                                    "label": "Gate",
                                    "value": "D57"
                                },
                                {
                                    "label": "Seat",
                                    "value": "74J"
                                },
                                {
                                    "label": "Sec.Nr.",
                                    "value": "003"
                                }
                            ],
                            "logo_image_url": ngrokurl + "/media/5_BUi6R7J.jpg",
                            "header_image_url": ngrokurl + "/media/5_BUi6R7J.jpg",
                            "qr_code": "M1SMITH NICOLAS  CG4X7U nawouehgawgnapwi3jfa0wfh",
                            "above_bar_code_image_url": ngrokurl + "/media/5_BUi6R7J.jpg",
                            "flight_info": {
                                "flight_number": "KL0642",
                                "departure_airport": {
                                    "airport_code": "NAIA3",
                                    "city": "Manila",
                                    "terminal": "T1",
                                    "gate": "D57"
                                },
                                "arrival_airport": {
                                    "airport_code": "AMS",
                                    "city": "Amsterdam"
                                },
                                "flight_schedule": {
                                    "departure_time": "2017-11-05T17:30",
                                    "arrival_time": "2017-11-05T17:30"
                                }
                            }
                        },
                        {
                            "passenger_name": "JONES FARBOUND",
                            "pnr_number": "CG4X7U",
                            "travel_class": "business",
                            "seat": "74K",
                            "auxiliary_fields": [
                                {
                                    "label": "Terminal",
                                    "value": "T1"
                                },
                                {
                                    "label": "Departure",
                                    "value": "30OCT 19:05"
                                }
                            ],
                            "secondary_fields": [
                                {
                                    "label": "Boarding",
                                    "value": "18:30"
                                },
                                {
                                    "label": "Gate",
                                    "value": "D57"
                                },
                                {
                                    "label": "Seat",
                                    "value": "74K"
                                },
                                {
                                    "label": "Sec.Nr.",
                                    "value": "004"
                                }
                            ],
                            "logo_image_url": ngrokurl + "/media/5_BUi6R7J.jpg",
                            "header_image_url": ngrokurl + "/media/5_BUi6R7J.jpg",
                            "qr_code": "M1JONES FARBOUND  CG4X7U nawouehgawgnapwi3jfa0wfh",
                            "above_bar_code_image_url": ngrokurl + "/media/5_BUi6R7J.jpg",
                            "flight_info": {
                                "flight_number": "KL0642",
                                "departure_airport": {
                                    "airport_code": "NAIA3",
                                    "city": "Manila",
                                    "terminal": "T1",
                                    "gate": "D57"
                                },
                                "arrival_airport": {
                                    "airport_code": "AMS",
                                    "city": "Amsterdam"
                                },
                                "flight_schedule": {
                                    "departure_time": "2017-01-02T19:05",
                                    "arrival_time": "2016-01-05T17:30"
                                }
                            }
                        }
                    ]
                }
            }
        }
    }

    response_msg = json.dumps(payload)
    pprint(response_msg)
    status = requests.post(post_message_url, headers={"Content-Type" : "application/json"}, data = response_msg)
    pprint(status.json())
    return
