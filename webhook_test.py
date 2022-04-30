import requests
import json

webhook_url = 'https://a8a2-69-204-191-79.ngrok.io\webhook'
data = {
    "Yellow Diamond" : "{{plot_1}}",
    "Trend Change" : "{{plot_2}}",
    "Green Dot" : "{{plot_3}}",
    "Red X" : "{{plot_4}}",
    "Manipulation" : "{{plot_5}}",
    "Red Diamond" : "{{plot_6}}",
    "Blood Diamond" : "{{plot_7}}"
}

r = requests.post(webhook_url, data=json.dumps(data), headers={
                  'Content-type': 'application/json'})
