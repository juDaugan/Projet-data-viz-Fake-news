#genère un Bearer Token 
#curl -u "$API_KEY:$API_SECRET_KEY" --data 'grant_type=client_credentials' 'https://api.twitter.com/oauth2/token'

import requests
import os
import json

url = "https://api.monapi.com/endpoint"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer VotreTokenAPI"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erreur: {response.status_code}")