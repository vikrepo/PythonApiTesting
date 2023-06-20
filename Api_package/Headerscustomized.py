import requests
headerdata={'T1':'f1','t2':'f2'}
resp=requests.get('http://httpbin.org/get',headers=headerdata)
print(resp.text)