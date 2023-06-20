import json
import requests
import jsonpath

def test_oauth_api():
    token_url="http://thetestingworldapi.com/Token"
    data = {
        'grant_type':'password',
        'username':'admin',
        'password':'adminpass'
    }
    response=requests.post(token_url,data)
    print('token'+response.text)
    API_URL='https://thetestingworldapi.com/api/StDetails/1105'
    response=requests.get(API_URL)
    #print(response.text)