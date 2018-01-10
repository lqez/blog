Title: 2012-05-21 개발일지 : 다수의 LDAP 서버에 대응하는 Apache httpd + mod_authnz_ldap 인증문제
Time: 21:02:00

Symptom

  

같은 건물에 있는 다른 회사에서 공동으로 개발하는 일이 있어, 기존에 사용하던 SVN 서버에 LDAP 인증을 추가하게 되었다.

헌데, mod_authnz_ldap 과 mod_authn_alias 를 동시에 사용하는데 있어 문제가 발생하였다. 조건은 아래와 같다.

  

(1) 디렉토리 구조가 다른 두 개 이상의 LDAP 서버.

(2) Require directive로 valid-user가 아닌, authnz_ldap의 ldap-user 또는 ldap-group
사용.

  

위와 같은 조합에서는, authnz_ldap의 Require directive인 ldap-user나 ldap-group에서 어떤 LDAP
서버의 DN을 의미하는지를 알 수 없으므로, 특정 사용자나 특정 그룹을 지칭하는 것이 불가능하다. 인터넷에서 검색할 수 있는 대부분의
문서들도 가장 기본적인 valid-user 만을 이용하고 있다.

  

문제의 설정 파일은 다음과 같다.

> <AuthnProviderAlias ldap ldap1>

>

> AuthLDAPURL ldap://some-ldap1/

>

> ...

>

> </AuthnProviderAlias>

>

>

>

> <AuthnProviderAlias ldap ldap2>

>

> AuthLDAPURL ldap://some-ldap2/

>

> ...

>

> </AuthnProviderAlias>

>

>

>

> <Location /foo>

>

> AuthBasicProvider ldap1 ldap2

>

> AuthType Basic

>

> AuthzLDAPAuthoritative off

>

> # 문제가 된 부분. ldap-user, ldap-group 사용 불가.

>

> Require ldap-group group_on_ldap1

>

> Require ldap-user user_on_ldap2

>

> # valid-user를 사용하면 문제 없음.

>

> Require valid-user

>

> </Location>

참고 : mod_authnz_ldap의 Require directives / [http://httpd.apache.org/docs/2.2/m
od/mod_authnz_ldap.html#requiredirectives](http://httpd.apache.org/docs/2.2/mo
d/mod_authnz_ldap.html#requiredirectives)

참고 : [http://serverfault.com/questions/140858/authenticating-apache-httpd-
against-multiple-ldap-servers-with-expired-
accounts](http://serverfault.com/questions/140858/authenticating-apache-httpd-
against-multiple-ldap-servers-with-expired-accounts)

참고 : [http://mail-archives.apache.org/mod_mbox/httpd-users/200709.mbox/%3C7eb9
e01c0709180949j2373d709i7116b64bd82d4e7@mail.gmail.com%3E](http://mail-
archives.apache.org/mod_mbox/httpd-users/200709.mbox/%3C7eb9e01c0709180949j237
3d709i7116b64bd82d4e7@mail.gmail.com%3E)

  

﻿

  

A Bad Solution

  

이 문제를 해결하기 위한 가장 단순한 방법은,

> 방법1. Require valid-user 만을 사용한다.

하지만, 세분화된 인증을 반드시 필요로 하거나, (나와 같이) 별 필요는 없지만 ldap-user를 쓰지 않고는 못 배기는 사람들을 위해서
다음과 같은 방법을 제안한다.

  

> 방법2. LDAP 서버별로 서로 다른 포트를 할당하여 서비스 한다.

authn_alias를 사용하지 않으면, authnz_ldap의 기능을 사용할 수 있으므로, Apache httpd에 포트를 추가하여 새로운
LDAP을 사용하는 사용자들은 해당 포트로 접속하도록 유도하였다. 이를 위해서는 아래의 작업이 필요하다. (Ubuntu 기준)

  

(1) /etc/apache2/ports.conf에 새롭게 사용할 포트 지정.

(2) VirtualHost를 별도로 지정하고, 새로운 LDAP을 사용하도록 설정.

  

변경된 설정 파일은 다음과 같다.

> <VirtualHost *:8080>

>

> <Location /foo>

>

> AuthBasicProvider ldap

>

> AuthLDAPURL ldap://some-ldap1/

>

> AuthType Basic

>

> AuthzLDAPAuthoritative off

>

> Require ldap-group group_on_ldap1

>

> </Location>

>

> </VirtualHost>

>

>

>

> <VirtualHost *:8081>

>

> <Location /foo>

>

> AuthBasicProvider ldap

>

> AuthLDAPURL ldap://some-ldap2/

>

> AuthType Basic

>

> AuthzLDAPAuthoritative off

>

> Require ldap-user user_on_ldap2

>

> </Location>

>

> </VirtualHost>

올바르거나 혹은 더 편한 방법이 있으면 꼭 알고 싶다. 개인적으로는 이와 같은 경우에 ldap-user 대신 alias 이름을 사용하여
ldap1-group이나 ldap2-user와 같은 것을 사용했으면 싶지만, 서로 다른 모듈의 조합이라 어려울 것으로 보인다.

