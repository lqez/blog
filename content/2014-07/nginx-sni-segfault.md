Title: segfault by ssl_session_cache in Nginx
Date: 2014-07-22
Lang: ko
Tags: nginx, openssl


과거에는 SSL 웹서비스를 위해서 도메인 별로 다른 IP를 써야만 했었다.
하지만 [Server Name Indication](http://en.wikipedia.org/wiki/Server_Name_Indication)이 등장한 이후로,
하나의 물리 IP에 여러 도메인의 SSL 웹 서비스가 가능해졌는데, 이를 위해 웹 서버 뿐 아니라 클라이언트에서의 지원도 필요하다.
대표적으로 Internet Explorer 6 등은 SNI를 지원하지 않는다.

 - [SNI를 지원하지 않는 클라이언트 목록](http://en.wikipedia.org/wiki/Server_Name_Indication#Client_side)

회사에서도 SNI를 지원하는 Nginx를 통해 여러 SSL 웹서비스를 운영하고 있는데,
특정 클라이언트로 접속한 경우에 Nginx 가 종료되는 문제가 발생하였다.
최적화를 위해 도입한 `ssl_session_cache` directive를 추가한 이후에 발생한 문제였는데,
검색해보니 동일한 증상이 Nginx Trac에 보고되어 있다.

 - <http://trac.nginx.org/nginx/ticket/235>

덧) 이 글을 처음 썼던 시점으로부터 1년이 지나 2015년 10월에서야 수정되어 Nginx 1.9.6에 반영되었다.

 - <https://trac.nginx.org/nginx/timeline?from=2015-10-20T16%3A38%3A08Z&precision=second>
