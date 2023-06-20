import  requests
url="https://reqres.in/api/users?page=2"

response=requests.get(url)
#print(response.content)
print(response.headers)


print( response.status_code)

assert response.status_code==200

print(response.headers.get('Server'))

print(response.cookies)

print(response.encoding)

print(response.elapsed)




