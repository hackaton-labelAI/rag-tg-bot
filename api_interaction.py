import requests
import json


server_address = ''

def proccess_question(question: str):
    headers = {
        'accept': 'application/json',
    }

    data = pass
    response = requests.post(url=f"{server_address}/api/chat", data=data, headers=headers)

    return json.loads(response.text)


def proccess_pdf(document):
    pass
    # return все ок или не ок