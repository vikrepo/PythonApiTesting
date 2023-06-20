import json

import jsonpath
import pytest


import requests
from requests.auth import HTTPBasicAuth

def test_with_auth():
        auth = HTTPBasicAuth('user', 'pass')
        response=requests.get('https://httpbin.org/basic-auth/user/pass', auth=auth)
        print(response.text)
        print(response)

