import json

import jsonpath
import pytest
import requests

url="https://reqres.in/api/users"
a=10

@pytest.fixture
def start_exec(scope="module"):
    global file
    file = open('/Users/vikramadityaanand/Desktop/test/t.txt', 'r')


#@pytest.mark.skipif(a>10,reason="This is not valid for current build")
@pytest.mark.Smoke
def test_create_new_user(start_exec):
    json_input=file.read()
    req_json=json.loads(json_input)
    resp=requests.post(url,req_json)
    #print(resp.content)
    assert resp.status_code==201
    print(resp.headers)
    print(resp.headers.get('Content-Type'))
    resp_json=json.loads(resp.text)
    id=jsonpath.jsonpath(resp_json,'id')
    print(id[0])

@pytest.mark.Sanity
def test_create_other_user(start_exec):
    json_input = file.read()
    req_json = json.loads(json_input)
    resp = requests.post(url, req_json)
    # print(resp.content)

    #print(resp.headers)
    #print(resp.headers.get('Content-Type'))
    resp_json = json.loads(resp.text)
    id = jsonpath.jsonpath(resp_json, 'id')
    print(id[0])



