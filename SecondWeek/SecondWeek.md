# Django

### 프레임워크

소프트웨어의 구체적인 부분에 해당하는 설계와 구현을 재사용이 가능하게끔, 일련의 협업화된 형태의 클래스들을 모아놓은 것

### Static Page vs Dynamic Page

<li> 정적인 페이지 : 변수 및 환경에 반응이 없음. 
<li> 동적인 페이지 : 변수 및 환경에 반응함.

### CGI(Common Gateway Interface) : 상호 데이터 교환

### WSGI : 장고 내에 CGI 역할을 담당함.

### Micro VS Full Stack 

<li> 마이크로 프레임워크(Flask) : 기본 기능이 제공되고 추가적으로 기능을 더 넣을 수 있도록 설계된 프레임워크
<li> 풀스택 프레임워크(Django)  : 추가 설치가 거의 필요없이 기본 기능이 있음.

### Web Application Server 

<li> 장고 서버 켜기 : python3 -m http.server 8000
<li> 바인드 설정 장고 서버 켜기 : python3 -m http.server 8000 -bind 127.0.0.1
<li> CGI 옵션 : python3 -m http.server --cgi 8000
<li> chmod a+x cgi01.py

### #!/usr/bin/env python3

맥사용시 CGI 파일사단에 달아줘야됨.

```python
#!/usr/bin/env python3
print('Content-Type:text/html;charset=utf-8\n')
print('Hello World')
```

###  xlsxwriter
pip3 install xlsxwriter
```python

```

### Django

Django 시작하기 : django -admin startproject first_site
Django manage.py : django manage.py migrate
Django 

### 기타 등등

 장고는 자유도 낮아 개발자가 장고에게 맞춰야함. 플라스크는 초기에는 어렵지만 후에는 좋음.