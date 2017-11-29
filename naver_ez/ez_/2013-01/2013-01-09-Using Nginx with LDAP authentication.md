Title: Using Nginx with LDAP authentication
Time: 11:42:00

Nginx는 비동기 이벤트 기반 웹 서버다. 더 이상의 자세한 설명은 생략한다.

  * [http://www.nginx.org/](http://www.nginx.org/)
  * [http://ko.wikipedia.org/wiki/Nginx](http://ko.wikipedia.org/wiki/Nginx)

사내외로 골고루 사용하던 Apache httpd 웹 서버 - 라 쓰고 종합 선물 세트라고 읽는다 - 를 대체하기 위해 Nginx 를 도입하던
중, 대부분의 이슈를 해결하였으나 LDAP 인증이 기본 모듈에 없어, 애플리케이션 레벨에서 다룰까하다 검색해보니 서드파티 플러그인으로
nginx-auth-ldap 이 있어 사용해보았다.

이하 작업은 Ubuntu 12.04(precise) 를 기준으로 작업한 내용을 정리한 것이다.

1. Get Nginx

[http://nginx.org/en/download.html](http://nginx.org/en/download.html)

위 경로에서 적절한 파일을 받는다. 실제 서비스를 위해서는 되도록 stable release를 받는 것이 좋겠다.

2. Get previous configuration

-V 옵션을 통해 기존에 사용하던 Nginx 를 빌드하기 위해 사용한 옵션을 확인할 수 있다.

> $ ./nginx -V

>

> nginx version: nginx/1.1.19

>

> TLS SNI support enabled

>

> configure arguments: --prefix=/etc/nginx --conf-path=/etc/nginx/nginx.conf
--error-log-path=/var/log/nginx/error.log --http-client-body-temp-
path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi
--http-log-path=/var/log/nginx/access.log --http-proxy-temp-
path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-
uwsgi-temp-path=/var/lib/nginx/uwsgi --lock-path=/var/lock/nginx.lock --pid-
path=/var/run/nginx.pid --with-debug --with-http_addition_module --with-
http_dav_module --with-http_geoip_module --with-http_gzip_static_module
--with-http_image_filter_module --with-http_realip_module --with-
http_stub_status_module --with-http_ssl_module --with-http_sub_module --with-
http_xslt_module --with-ipv6 --with-sha1=/usr/include/openssl --with-
md5=/usr/include/openssl --with-mail --with-mail_ssl_module --add-
module=/build/buildd/nginx-1.1.19/debian/modules/nginx-auth-pam --add-
module=/build/buildd/nginx-1.1.19/debian/modules/nginx-echo --add-
module=/build/buildd/nginx-1.1.19/debian/modules/nginx-upstream-fair --add-
module=/build/buildd/nginx-1.1.19/debian/modules/nginx-dav-ext-module

3. Get nginx-auth-ldap

[https://github.com/kvspb/nginx-auth-ldap](https://github.com/kvspb/nginx-
auth-ldap)

세상엔 친절한 사람이 의외로 많은데, 역시 누군가 만들어 공개해두었다. 아래와 같이 git clone 하여 받아둔다.

> $ git clone https://github.com/kvspb/nginx-auth-ldap.git

4. Configuration and Build

미리 확인해둔 옵션에 nginx-auth-ldap 페이지의 설명에서와 같이--add-module 옵션으로 nginx-auth-ldap
디렉토리를 지정하여, 같이 빌드하도록 한다.

필요 없는 모듈은 일부 삭제하여, 아래와 같은 설정으로 빌드하였다. 자신에게 맞는 빌드 옵션을
[http://wiki.nginx.org/InstallOptions](http://wiki.nginx.org/InstallOptions) 를
통해 확인하여 지정하도록 한다.

> $ nginx -V

>

> nginx version: nginx/1.2.6

>

> built by gcc 4.6.3 (Ubuntu/Linaro 4.6.3-1ubuntu5)

>

> TLS SNI support enabled

>

> configure arguments: --prefix=/etc/nginx **--sbin-path=/usr/sbin** --conf-
path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-
client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-
path=/var/lib/nginx/fastcgi --http-log-path=/var/log/nginx/access.log --http-
proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi
--http-uwsgi-temp-path=/var/lib/nginx/uwsgi --lock-path=/var/lock/nginx.lock
--pid-path=/var/run/nginx.pid --with-debug --with-http_addition_module --with-
http_dav_module --with-http_geoip_module --with-http_gzip_static_module
--with-http_image_filter_module --with-http_realip_module --with-
http_stub_status_module --with-http_ssl_module --with-http_sub_module --with-
ipv6 --with-sha1=/usr/include/openssl --with-md5=/usr/include/openssl **--add-
module=/home/ez/nginx-auth-ldap**

이 글을 읽을 분들은 당연히 configure나 make에 익숙할거라 생각하지만, 혹시나 하여 적어본다. libpcre3-dev 나
libssl-dev 등 빌드에 필요한 패키지는 미리 받아두도록 하자.

GD 관련 라이브러리를 달라고 에러를 뱉는 경우가 있는데, 이 때는 libgd2-xpm-dev 등을 받으면 된다.

> $ ./configure --prefix=/etc/nginx ... (생략)

>

> $ make

5. Packaging and Install

아래와 같이 checkinstall 을 이용해 deb 패키징 후 설치하거나, 간단하게 sudo make install 로도 설치할 수 있다.

> $ sudo checkinstall

checkinstall 을 통해 설치하다가, 기존 설치본 때문에 설치할 수 없다는 에러가 발생하면, 아래와 같이 덮어쓰기 옵션을 추가하여
설치할 수 있다.

> $ sudo dpkg -i --force-overwrite <package_file>.deb

6. LDAP configuration

foo.com 의 admin 경로에 대해 LDAP 인증을 추가한다고 가정한다.

/etc/nginx/sites-available 에 있는 사이트별 설정파일에서 foo.com 에 해당하는 파일을 열어, 아래와 같이
수정한다.

> server {

>

> listen 80;

>

> server_name foo.com [www.foo.com;](http://www.foo.com;)

>

> (...생략...)

>

> ** auth_ldap_url
ldap://ldap.foo.com/dc=foo,dc=com?uid?sub?(objectClass=person);**

>

> ** location /admin {**

>

> ** auth_ldap "Administrator page";**

>

> ** auth_ldap_require valid_user;**

>

> ** } **

>

> }

  

그룹 등의 다양한 설정에 대해서는 다음 링크를 참조한다.

[https://github.com/kvspb/nginx-auth-
ldap/blob/master/example.conf](https://github.com/kvspb/nginx-auth-
ldap/blob/master/example.conf)

  

  

