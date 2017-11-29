Title: ucloud storage + cloudfuse
Time: 22:35:00

얼마 전에 ucloudbiz에 대한 불만 글([http://blog.naver.com/ez_/140146229569](http://blog.
naver.com/ez_/140146229569))을 썼지만, 어쨌든 쓰긴 써야 하는 형편이다 보니 결국 세팅 했다.

(공식 사이트 자료실에서 제공하는 cloudfuse 관련 도움말은 [여기(링크)](https://ucloudbiz.olleh.com/menu
al/SS_BETA_SERVICE_GUIDE_20110531_V2.2.pdf)에 포함되어 있는 단 한 페이지에 불과하다.)

  

**0. cloudfuse**

[https://github.com/redbo/cloudfuse](https://github.com/redbo/cloudfuse)

cloudfuse는 FUSE 기반의 Rackspace Cloud 파일 시스템을 마운팅하기 위한 오픈소스 프로젝트이다.

Rackspace Cloud도 ucloud storage처럼 Rackspace에서 제공하는 스토리지 서비스이며, 같은 OpenStack의
Swift프로토콜을 사용하고 있으므로, 설정 변경을 통해 ucloud storage를 사용할 수 있다.

  

  

**1. cloudfuse 설치**

github에서 cloudfuse를 클론 후 빌드한다.필요한 경우 libfuse-dev를 설치한다.

> $ git clone https://github.com/redbo/cloudfuse.git

>

> $ cd cloudfuse

>

> $ make && sudo make install

**  
**

**2. 마운트**

cloudfuse는 기본적으로 Rackspace Cloud를 위해 빌드되어 있으므로, authurl 옵션을 별도로 설정해야 한다.

  

설정 파일 없이 바로 사용하려면, 커맨드라인에서 바로 옵션을 입력한다.

> $ cloudfuse -o username=[사용자명],api_key=[발급받은
KEY],authurl=https://ssproxy.ucloudbiz.olleh.com/auth/v1.0 [마운트 위치]

설정 파일(~/.cloudfuse)에 미리 값을 입력해두면 마운트 위치만 지정하여 사용 가능하다.

> username=[사용자명]

>

> api_key=[발급받은 KEY]

>

> authurl=https://ssproxy.ucloudbiz.olleh.com/auth/v1.0

**  
**

**3. 언마운트**

일반적인 파일 시스템의 언마운트와 같다.

> $ umount [마운트 위치]

  

  

**4. 디버그 모드**

cloudfuse 실행시 -d 옵션을 주면 debug 모드로 실행되며, 아래와 같은 내용을 볼 수 있게 된다. 접속에 문제가 있는 경우 이
옵션을 통해 추가 정보를 얻을 수 있다.

> !!! Authenticating...

>

> * About to connect() to ssproxy.ucloudbiz.olleh.com port 443 (#0)

>

> * Trying xxx.xxx.xxx.xxx... * connected

>

> * Connected to ssproxy.ucloudbiz.olleh.com (xxx.xxx.xxx.xxx) port 443 (#0)

>

> * successfully set certificate verify locations:

>

> * CAfile: none

>

> CApath: /etc/ssl/certs

>

> * SSL connection using DHE-RSA-AES256-SHA

>

> * Server certificate:

>

> * subject: C=KR; ST=Gyeonggi-do; L=Seongnam-si; O=KT; OU=Cloud Business
Department; CN=*.ucloudbiz.olleh.com

>

> * start date: 2011-07-18 00:00:00 GMT

>

> * expire date: 2012-07-17 23:59:59 GMT

>

> * issuer: C=US; O=Thawte, Inc.; CN=Thawte SSL CA

>

> * SSL certificate verify ok.

>

> > GET /auth/v1.0 HTTP/1.1

>

> User-Agent: CloudFuse

>

> Host: ssproxy.ucloudbiz.olleh.com

>

> Accept: */*

>

> ...(중략)...

>

> FUSE library version: 2.8.4

>

> nullpath_ok: 0

>

> unique: 1, opcode: INIT (26), nodeid: 0, insize: 56

  

