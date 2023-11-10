from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

url = 'http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List'
params ={
    'serviceKey' : os.environ.get("GOVAPI_AUTH_KEY"), 
    'pageNo' : '1', 
    'numOfRows' : '10', 
    'type' : 'json' 
}

response = requests.get(url,params=params)
obj = response.json()

print(json.dumps(obj, indent=2, ensure_ascii=False))