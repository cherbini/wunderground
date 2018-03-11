from __future__ import division
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
from pprint import pprint
import numpy as np
import cv2
import imutils
import requests
from requests.auth import HTTPBasicAuth
import pprint
import json
import csv

# API AUTH SETUP
url_prefix = ('http://api.wunderground.com/api/')
api_key = "251c020b3886176c"

# TOKEN SETUP
#date = "/history_20150510"

resp = requests.get(url_prefix + api_key + "/forecast/q/CA/San_Francisco.json")
token = resp.json()
#print(token)

# RESPONSE HANDLER
#jsonResponse = resp.json()
#jsonData = jsonResponse['token']

# ITERATE THROUGH REQUIRED JSON VARS
for day in token['forecast']['simpleforecast']['forecastday']:
    print(day['date']['weekday'] + ":")
    print("Conditions: ", day['conditions'])
    print("High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C", '')
