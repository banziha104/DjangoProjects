
# 6Weeks

<li> 폴더로 이동 : cd Desktop/<name>
<li> 파이썬 가상 환경 만들기 :virtualenv myenv --python=python3.6 
<li> 가상 환경 실행 :source myenv/bin/activate
<li> 장고 설치 : pip install django~=1.11.0
<li> 장고 : django-admin startproject mysite . // . 은 현재 파일에 설정
<li> 포토라는 이름의 앱을 만듬 : python manage.py startapp photo
<li> 마이그레이트 : python manage.py migrate
<li> 파이썬 서버 실행 : python manage.py runserver

### In Django

모델 정의

```python
from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    author = models.ForeignKey(User, related_name='photo_posts')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # auto_now_add 처음에만 업데이트
    updated = models.DateTimeField(auto_now=True)     # auto_now     계속 자동 업데이트

    class Meta:                     # 모델안에 미리 정의된 규칙(정렬, 세팅 등)
        ordering = ('-updated',)    # 업데이트 내림차순

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%i:%s")
```


언어및 타임존 변경

```python
LANGUAGE_CODE = 'ko-kr' # 언어변경

TIME_ZONE = 'Asia/Seoul' # 타임존 변경
```

앱 설정

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photo', #photo 앱 추가
]
```

admin 설정 및 페이지설정
```python
from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','author','created','updated') # Admin page 변경
    list_filter = ('author','created','updated')
    
admin.site.register(Photo,PhotoAdmin)
```
### 기타

<li> python manage.py makemigrations   # 마이그레이션 생성
<li> python manage.py sqlmigrate photo 0001 #  데이터베이스 마이그레이션 생성
<li> python manage.py migrate
<li> python manage.py createsuperuser # 유저생성
