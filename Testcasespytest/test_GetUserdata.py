import  requests
import json
import jsonpath
import pytest


@pytest.mark.Smoke
def test_fetch_user_details():
    url = "https://reqres.in/api/users?page=2"

    response = requests.get(url)
   # print(response)

    json_response = json.loads(response.text)
    # print(json_response)

   # pages = jsonpath.jsonpath(json_response, 'total_pages')
    firstname = jsonpath.jsonpath(json_response, 'data[0].first_name')
    #firstname1 = jsonpath.jsonpath(json_response, 'data[2].first_name')
    #assert pages[0] == 2
    #print(pages[0])
    #print((firstname1[0]))

    for i in range(0, 6):
        firstname_ar = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
        print((firstname_ar[0]))
