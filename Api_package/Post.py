import json

import jsonpath
import requests

url="https://reqres.in/api/users"

file=open('/Users/vikramadityaanand/Desktop/test/t.txt','r')
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