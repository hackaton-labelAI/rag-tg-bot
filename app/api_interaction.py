import json

import requests

from app.config import SERVER

server_address = ''


def proccess_question(question: str):
    headers = {
        'accept': 'application/json',
    }

    data = {
        "session_id": None,
        "context": [{
            "text_data": {
                "role": "user",
                "content": question
            },
            "rag_data": None
        }]
    }
    chunks = requests.post(url=f'{SERVER}/api/chat', data=data, headers=headers)['data']
    data = {
        'question': question,
        'chunks': chunks
    }
    response = requests.post(url=f'{SERVER}/api/telegram_get_response', data=data)

    return json.loads(response.text)


def proccess_pdf(document):
    pass
    # return все ок или не ок
