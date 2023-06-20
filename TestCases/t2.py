import requests
import json
import jsonpath

def test_add_multiple_students():
    status_code=202
    assert status_code==201