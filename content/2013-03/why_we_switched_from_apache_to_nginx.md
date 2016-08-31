Title: Why we switched from Apache to Nginx
Date: 2013-03-22
Lang: ko
Tags: apache, httpd, nginx, fpm, uwsgi
Status: draft

2004년에 LAMP 스택을 처음 접한 이래로, 거의 10년 동안 Apache httpd(이하 Apache) + mpm_prefork + mod_php5 를 실 서비스에 활용해왔다.

mpm_prefork 모델의 불합리함을 알면서도 바꾸기 귀찮다는 핑계로 스택을 변경하지 않았는데, 
스마트스터디에서 웹 서비스 대부분을 Python 으로 개발하게 되면서 Apache + mod_python 의 한계를 실감하고, 이에 Nginx + uWSGI 조합을 고려하게 되었다.

하지만 PHP 서비스를 바로 완전히 걷어낼 순 없었고, 더군다나 공생 관계에 있는 회사의 PHP 기반 코드들도 남아있었기 때문에 바로 전환할 엄두를 내진 못했다.
게다가 .htaccess 의 RewriteRule magic(==hell)을 건드리는 것도 부담스러운 일이었다.

그렇게 버티다, 어느 날 사용자 접속이 폭주하여 서비스 장애가 발생했다.

직접 빌드하여 `MaxClients 1536`로 설정하여 사용하고 있었지만, 일부 웹 서버는 메모리가 터져버렸고,
메모리가 여유있는 서버도 더 이상의 접속을 허용하지 못하는 단계에 이르렀다. `KeepAlive` 관련 변수 조정으로는 대응하기가 어려워 보여,
동기적으로 처리하던 데이터와 작업들을 일단 다른 서버의 Redis에 버퍼링하여, 나중에 다시 처리할 수 있도록 보관하기로 했다.

Apache 를 Nginx 로 대체함과 동시에, PHP 를 위해 [php-fpm](http://php-fpm.org/) 을 도입했다.



* http://blog.pythonanywhere.com/36/
* http://nbonvin.wordpress.com/2011/03/14/apache-vs-nginx-vs-varnish-vs-gwan/


* nginx + php-fpm : http://blog.kubox.info/?p=175
* nginx + php-fpm tune : http://www.if-not-true-then-false.com/2011/nginx-and-php-fpm-configuration-and-optimizing-tips-and-tricks/

* [Google Apps Directory Sync Administration Guide(in PDF)](http://www.google.com/support/enterprise/static/gapps/docs/admin/en/gads/admin/)
![Screen Shot of GADS](./images/gads_01.png)
