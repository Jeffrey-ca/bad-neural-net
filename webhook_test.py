import requests
import json

webhook_url = 'http://a8ea-69-204-191-79.ngrok.io/webhook'

data = { 'big dick': '> 2 inches',
         'small penis': '< 1.9 inch' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-type': 'application/json'})
