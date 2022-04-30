import requests
import json

webhook_url = 'https://a8a2-69-204-191-79.ngrok.io'
data = {'name': 'test',
        'Channel URL': 'test url'}

r = requests.post(webhook_url, data=json.dumps(data), headers={
                  'Content-type': 'application/json'})
