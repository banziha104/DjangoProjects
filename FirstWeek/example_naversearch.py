# request 모듈 불러오기
import requests

# BeautifulSoup 모듈 블러오기 Plain Text를 보여줌
#pip3 install BeautifulSoup
from bs4 import BeautifulSoup

url = "http://www.naver.com" #Url 설정
r = requests.get(url)
html = BeautifulSoup(r.text, 'html.parser')

search_keywords = html.select(" .PM_CL_realtimeKeyword_rolling .ah_item .ah_a") # id를 불러올땐 # , 클래스를 불러올땐 (.)

for keyword in search_keywords:
    rank = keyword.select_one(".ah_r").text
    search = keyword.select_one(".ah_k").text
    print(rank, search)
    # r.text 받아온 데이터
    # elem.text 태그 안에 있는 문자열