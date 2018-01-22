Title: MySQL : Mac OS X에서 mac port로 설치하기
Time: 15:18:00

아래 글([http://blog.naver.com/ez_/140113920581](http://blog.naver.com/ez_/140113
920581))을 통해 mac port에 대해 간략하게 알아보았다.

이 글은 mac port를 통해 MySQL 5의 서버와 클라이언트를 설치하는 방법을 설명한다.

  

mac port를 통해 MySQL을 설치하는 것 자체는 간단하지만, 설치된 결과는 여타 Unix-ish 시스템과는 다른 부분이 있어, 실제
MySQL을 운용 및 테스트하는데 사소한 문제들이 있다. 아래 설치 가이드는 기본 설치 위치인 /opt/local/ 을 변경하지 않음을
전제로 한다.

  

  

**(1) 설치**

> sudo port install mysql5 +server

mysql5 뒤의 +server는 port의 variant를 의미하는데, 이에 대한 설명은 mac port 매뉴얼을 참고한다.
+server를 하지 않아도 mysql-client와 mysql-server가 모두 설치되는데, 이 variant를 추가해야
LaunchDaemons에 필요한 start/stop 스크립트 등이 추가 설치된다.

**  
**

**(2) 초기화**

>sudo /opt/local/lib/mysql5/bin/mysql_install_db5 --user=_mysql

사용자가 mysql이 아니라 _mysql임을 유의. Leopard 부터는 daemon 사용자의 경우 _(언더스코어)를 붙이는 것이 관례.

**  
**

**(3) 서버 시작**

**>sudo /opt/local/share/mysql5/mysql/mysql.server start**

**아래와 같은 메세지가 나오면 정상.**

> Starting MySQL

>

> . SUCCESS!

******(4) 패스워드 설정**

**처음 설치한 이후에는 root 패스워드가 없으므로, 이를 지정한다.**

**>**mysqladmin5 -u root password

  

더 안전한 설정을 위해 아래 스크립트를 실행한다. (root계정의 외부 접속 제한, test db의 drop등을 수행한다.)

> mysql_secure_install5

  

  

**(5) 재시작시 같이 시작되도록 등록**(필요한 경우)

> sudo launchctl load -w /Library/LaunchDaemons/org.macports.mysql5.plist

  

**(6) 시작/종료 명령어의 alias 생성**(필요한 경우)

> vi ~/.proflie

파일 내에 아래의 문구를 삽입한다. 혹은 아래의 명령어를 직접 입력해 MySQL 서버를 시작/종료 시키면 된다.

> alias mysqlstart='sudo /opt/local/share/mysql5/mysql/mysql.server start'

>

> alias mysqlstop='sudo /opt/local/share/mysql5/mysql/mysql.server stop'

**(7) my.cnf 파일 생성** (필요한 경우)

> sudo touch /opt/local/etc/mysql5/my.cnf

추가로 MySQL을 설정할 부분이 있으면, 위의 파일을 사용한다.

  

또한, Unix-ish 시스템에 익숙한 사용자는 일단 로컬 소켓인 mysql.sock의 위치가 /tmp/mysql.sock이 아니라 당황할
수도 있다. 아래의 내용을 my.cnf에 추가하면 기본 위치를 바꿀 수 있다. (서버의 재시작이 필요함)

> [mysqld_safe]

>

> socket = /tmp/mysql.sock

>

>

>

> [mysqld]

>

> socket = /tmp/mysql.sock

>

>

>

> [client]

>

> socket = /tmp/mysql.sock

  

  

