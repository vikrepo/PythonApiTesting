import json

import jsonpath
import requests

url="https://reqres.in/api/users/2"

file=open('/Users/vikramadityaanand/Desktop/test/t.txt','r')
json_input=file.read()
req_json=json.loads(json_input)

response=requests.put(url,req_json)

assert response.status_code==200

response_json=json.loads(response.text)
updated_li=jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])