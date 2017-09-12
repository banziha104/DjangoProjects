import requests
import json

url = "http://datalab.naver.com/rc/rankList.naver"

r = requests.post(url)

if r.status_code == requests.codes.ok :
    encoded_json = json.loads(r.text)
    data = encoded_json["data"]
    for section in data:
        print(section["name"])
        for item in section["items"] :
            print(item["rank"],item["keyword"])


