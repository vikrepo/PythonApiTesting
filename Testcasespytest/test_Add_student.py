import requests
import json
import jsonpath

def test_add_multiple_students():
    api_url="https://thetestingworldapi.com/api/studentsDetails"
    f=open('/Users/vikramadityaanand/Desktop/test/AddNewStudent.json')
    json_request=json.loads(f.read())
    response=requests.post(api_url,json_request)
    print(response.status_code)
    print(response.text)
    assert response.status_code==201


