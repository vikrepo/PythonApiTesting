import requests
param={'name':'test','email':'vik@gmail.com'}
response=requests.get('http://httpbin.org/get',params=param)
print(response.text)