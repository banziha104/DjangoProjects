
# 6Weeks

<li> 폴더로 이동 : cd Desktop/<name>
<li> 파이썬 가상 환경 만들기 :virtualenv myenv --python=python3.6 
<li> 가상 환경 실행 :source myenv/bin/activate
<li> 장고 설치 : pip install django~=1.11.0
<li> 장고 : django-admin startproject mysite . // . 은 현재 파일에 설정
<li> 포토라는 이름의 앱을 만듬 : python manage.py startapp photo
<li> 마이그레이트 : python manage.py migrate
<li> 파이썬 서버 실행 : python manage.py runserver
<li> 사진 라이브러리 : pip install Pillow
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
    list_display = ('id','author','created','updated') # Admin 칼럼 변경
    list_filter = ('author','created','updated')       # 필터 설정
    search_fields = ('text','created')                 # 서치 설정
    raw_id_fields = ('author',)                        # 회원번호 등에서 쓰듯, 검색 가능,은 필수
    ordering = ['updated','created']                   # 모델의 odering과 다름, admin페이지의 오더링순
admin.site.register(Photo,PhotoAdmin)
```

views.py 

```python
from django.shortcuts import render

from .models import Photo

def post_list(request):
    posts = Photo.objects.all()                              # 포스트라는 변수에 모든것을 불러옮.
    return render(request,'photo/list.html',{'posts':posts}) # 템플릿에서 'posts' 라는 변수를 사용함, posts는 이클래스의 값 

```

photo/urls.py

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.post_list,name='post_list'),
]
```

mysite/urls.py

```python
from django.conf.urls import url , include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',include('photo.urls',namespace='photo')),
]

```

photo/templates/photo/list.html(templates 부터는 만들어야함)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Photo list</title>
</head>
<body>
{% for post in posts%} <!--view.py에서 posts를 던짐-->
{{ post.text }}        <!--post를 꺼냄-->
{% endfor %}           <!--for문 종료-->
</body>
</html>
```

models.py에 이미지 추가

```python
from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='NoImage.jpg') # 이미지 추가
    author = models.ForeignKey(User, related_name='photo_posts')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # auto_now_add 처음에만 업데이트
    updated = models.DateTimeField(auto_now=True)     # auto_now     계속 자동 업데이트

    class Meta:                     # 모델안에 미리 정의된 규칙(정렬, 세팅 등)
        ordering = ('-updated',)    # 업데이트 내림차순

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%i:%s")
```

settings.py

```python

MEDIA_URL = '/media/'                          # 웹사이트에서 어디서 보여줄지
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')   # media라는 폴더를 기본으로함

```
### 기타

<li> python manage.py makemigrations   # 마이그레이션 생성
<li> python manage.py sqlmigrate photo 0001 #  데이터베이스 마이그레이션 생성
<li> python manage.py migrate
<li> python manage.py createsuperuser # 유저생성
