# requests 모듈
# 설치 pip3 install requests
# 설치 윈도우 pip install

#

import requests.cookies

# GET 방식으로 통신
# r = requests.get("http://naver.com")
# print(r.text) # text 웹 페이지의 body를 받아옮

# post 방식으로 통신

# r = requests.post("http://naver.com")
# print(r.text)

url = "https://search.naver.com/search.naver"
payload = {"where": "nexearch", "query": "마광수", "sm": "top_lve", "ie" : "utf-8"} # 딕셔너리 형태로 쿼리 전송
r = requests.get(url, params=payload)


if r.status_code == requests.codes.ok:
    print("서버 응답 성공")
    print(r.text)
else:
    print("서버 응답 오류, 프로그램 종료")

# 첫 로그인
jar = requests.cookies.RequestsCookieJar() #쿠키값 불러오기
login_data = {"id": "myid", "pwd": "mypwd"}
r = requests.get(url,data=login_data, cookies=jar) # 쿠키 던지기

# login 이후
r = requests.get(url,cookies=jar)
