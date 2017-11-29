Title: django + nginx + uwsgi + virtualenv on Mac OS X / brew
Time: 23:02:00

본 문서는 Mac OS X 상에서 django 프로젝트를 virtualenv에 기반한 uWSGI로 실행, nginx를 통해 웹 서비스하는
방법을 소개한다.

패키지 설치는 brew와 pip로 이루어지지만, 다른 패키지 매니저를 사용하더라도 설정 방법은 동일하게 적용될 수 있다.

  

**  
**

**1. django 설정**

pip, virtualenv와 virtualenv wrapper의 설명과 설치 방법은 다음 링크를 참조한다 :[http://blog.nave
r.com/ez_/140138625021](http://blog.naver.com/ez_/140138625021)

  

> $ mkvirtualenv sample

>

> New python executable in sample/bin/python

>

> Installing setuptools............done.

>

> Installing pip...............done.

>

> ...(중략)...

>

> (sample) $ pip install django

>

> (sample) $ django-admin startproject sample/path/to/sample_proj

/path/to/sample_proj 안에 wsgi.py 를 다음과 같이 생성한다. 아래 예제는 sys.path에 wsgi.py의 부모
폴더를 포함시켜 django project 이름을 사용하도록 - sample.settings 와 같이 - 되어 있지만, 프로젝트 이름을
명시적으로 사용하지 않는 경우에는 +'/..' 을 생략한다.

> import sys

>

> import os

>

>

>

> sys.path.append(os.path.abspath(os.path.dirname(__file__))+'/..')

>

> os.environ['DJANGO_SETTINGS_MODULE'] = 'sample.settings'

>

>

>

> import django.core.handlers.wsgi

>

>

>

> application = django.core.handlers.wsgi.WSGIHandler()

**  
**

**2. uWSGI 설정**

> $ brew install uwsgi

>

> $ mkdir /usr/local/etc/uwsgi/

/usr/local/etc/uwsgi 내에 django.ini 를 다음과 같이 생성한다. home에는 virtualenv의 경로를,
pythonpath에는 django의 경로를 기입한다.

1에서 생성한 wsgi 설정 파일의 이름이 wsgi.py 이므로, module에는 wsgi를 입력하였다. 다른 이름을 사용하는 경우에는 해당
이름을 입력한다.

> [uwsgi]

>

> socket = /tmp/django.sock

>

> master = true

>

> processes = 1

>

> module = wsgi

>

> chmod-socket = 666

>

> home = /Users/<사용자명>/VirtualEnvs/sample

>

> pythonpath = /path/to/sample_proj

  

**3. nginx 설정**

> $ brew install nginx

설치 후 출력되는 설명에 따라, .bashrc 또는 .profile의 PATH 항목에 /usr/local/sbin 을 추가한다.

  

/usr/local/etc/nginx/nginx.conf 에서 location / 항목을 찾아 아래와 같이 수정하고, static 파일을
위한 alias를 추가하여, 더 효율적인 static 파일 전송을 하도록 설정한다. 미디어 파일 등을 위한 경로가 추가로 필요한 경우, 같은
방법으로 작성한다.

> location / {

>

> include uwsgi_params;

>

> uwsgi_pass unix:///tmp/django.sock;

>

> }

>

>

>

> location /static {

>

> alias /path/to/sample_proj/static/;

>

> autoindex off;

>

> }

**  
**

**4. uWSGI 시작**

> $ uwsgi --ini-paste /usr/local/etc/uwsgi/django.ini &

  

**5. nginx 시작**

> $ sudo nginx

  

**6. 테스트**

설정된 nginx 기본 포트가 8080이므로, [http://localhost:8080](http://localhost:8080) 으로
접속하여 테스트를 진행한다.

에러 발생시, nginx.conf의 error_log 항목을 활성화하여 자세한 에러 내역을 확인할 수 있도록 수정한 후, nginx을
재시작한다.

  

  

  

본 문서는 다음의 버전을 바탕으로 작성되었음 :Django 1.3.1 /uWSGI 0.9.9.2 /nginx 1.0.10

  

