import requests
import numpy as np
import json

# API AUTH SETUP
url_prefix = ('http://api.wunderground.com/api/')
api_key = "251c020b3886176c"

# TOKEN SETUP
date = "/history_20150510"

resp = requests.get(url_prefix + api_key + date + "/q/CA/San_Francisco.json")
token = resp.json()
#print(token)

lower_wind_threshold = 15.0

# ITERATE THROUGH REQUIRED JSON VARS
for item in token['history']['observations']:
    if float(item['wgustm']) > lower_wind_threshold:
        print(item['date']['pretty'] + ":")
        wspdm = item['wspdm']
        print("Max Wind Sustained: ", wspdm)
        wgustm = item['wgustm']
        print("Max Wind Gust: ", wgustm)
