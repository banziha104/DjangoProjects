import requests
from bs4 import BeautifulSoup
url = "http://datalab.naver.com/keyword/sectionSearch.naver"

r = requests.get(url)

if r.status_code == requests.codes.ok:
    data = BeautifulSoup(r.text, "html.parser")
    keywords = data.select(".sub_title .title")
    for keyword in keywords:
        print(keyword.text)