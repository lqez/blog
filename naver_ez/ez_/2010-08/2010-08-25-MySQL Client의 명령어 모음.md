Title: MySQL Client의 명령어 모음
Time: 17:55:00

MySQL Command-line client에서 그동안 help(\h) 명령어만 썼었는데,

오늘 무심코 몇가지 해보니 쓸만한 부분이 있어 글로 정리해본다.

  

명령어에 대한 레퍼런스 페이지는 다음과 같다.

[http://dev.mysql.com/doc/refman/5.1/en/mysql-
commands.html](http://dev.mysql.com/doc/refman/5.1/en/mysql-commands.html)

  

help를 치면 명령어의 목록과 간단한 설명을 볼 수 있다.

쓸모 있는 명령어, 원래 자주 쓰던 것, 그리고 앞으로도 안 쓸만한 명령어로 구분해보았다. ㅎㅎ

  

  

**쓸모 있어 보이는 낯선 명령어들**

  * edit(\e) - Unix 전용
  * 외부 에디터를 통해 현재 입력중인 명령어를 편집함.
  * 쿼리의 일부를 수정하거나, 긴 쿼리를 입력할 때 아주 유용할 듯.
  * pager(\p), nopager(\n)- Unix 전용
  * 결과를 출력할 때 외부 프로그램을 통해 페이징을 할 수 있도록 한다.
  * stdout으로 나오는 결과물을 우회시켜 출력하도록 한 듯. pager more나 pager less 등으로 지정해보니 훌륭하다.
  * tee(\T), notee(\t)
  * 쿼리 수행 결과를 파일로 쓰도록 함. tee [filename]
  * source(\.)
  * 외부 텍스트 파일을 읽어와 실행.
  * 커맨드로 나가 mysql < foo.sql 수행하고, 다시 돌아오는 것 보다 편할 듯.
  * warning(\W), nowarning(\w)
  * 경고가 있는 경우 이를 출력하거나, 출력하지 않도록 함.
  * 기본적으로 꺼져 있는데, 쿼리가 미심쩍을 경우 켜놓으면 상세 설명이 나와 도움이 된다.
  * status(\s)
  * 현재 접속하고 있는 서버의 상태를 보여줌.
  * > mysql> \s
>

> --------------

>

> mysql5 Ver 14.14 Distrib 5.1.49, for apple-darwin10.4.0 (i386) using
readline 6.1

>

>

>

> Connection id: 42

>

> Current database: test

>

> Current user: root@localhost

>

> SSL: Not in use

>

> Current pager: more

>

> Using outfile: '/tmp/tee.out'

>

> Using delimiter: ;

>

> Server version: 5.1.49 Source distribution

>

> Protocol version: 10

>

> Connection: Localhost via UNIX socket

>

> Server characterset: latin1

>

> Db characterset: latin1

>

> Client characterset: utf8

>

> Conn. characterset: utf8

>

> UNIX socket: /opt/local/var/run/mysql5/mysqld.sock

>

> Uptime: 1 day 52 min 52 sec

>

>

>

> Threads: 1 Questions: 5652889 Slow queries: 3 Opens: 72 Flush tables: 1 Open
tables: 26 Queries per second avg: 63.110

>

> --------------

  

**원래 자주 쓰던 명령어들**

  * delimiter(\d)
  * 저장 프로시저나 함수를 작성할 때에는 쓰게 되는 명령어.
  * 당연한 얘기지만, 이 명령어로 기본 딜리미터를 변경해도, 프로시저 내에서는 기본으로 세미콜론(;)을 딜리미터로 사용함.
  * delimiter //과 같이 delimiter [delimiter string]으로 사용함.
  * use(\u)
  * 기본 데이터베이스를 선택.
  * exit, quit(\q)
  * 프로그램을 종료.
  * ego(\G)
  * 명령의 수행 결과를 세로로 풀어서 출력함.
  * 쿼리 결과의 내용이 가로로 너무 길거나, 컬럼이 많은 경우에 유용.

**  
**

**잘 안 쓸 것 같은 명령어들**

  * ?
  * 도움말을 보여준다. help와 같은 기능
  * clear(\c)
  * 입력 중이던 내용을 취소한다.
  * 유닉스/리눅스에서는 Ctrl+U가 있으니 있으나 마나한 기능.
  * connect(\r)
  * 마지막에 연결했던 서버에 다시 연결함.
  * timeout으로 연결이 끊어진 경우엔 엔터만 쳐도 다시 연결이 됨.
  * connect db_name hostname 으로 입력하면 다른 서버에도 연결 가능.
  * print(\p)
  * 입력 중이던 명령어 전체를 출력함.
  * 이 정도로 긴 명령어라면 애초에 따로 편집하지 않을까 싶은데...
  * prompt(\R)
  * 프롬프트( mysql> 이라 나오는 부분 )을 원하는 문자열로 바꿀 수 있는 기능.
  * 여러 서버에 붙여서 작업하는 경우(connect 명령어와 더불어)에 편리할 지도 모르겠다는 생각.
  * > mysql> prompt mysql://\U/\d >
>

> PROMPT set to 'mysql://\U/\d > '

>

> mysql://root@localhost/test >

  * go(\g)
  * 입력했던 내용을 실행한다. 즉, 딜리미터(;) 입력하고 엔터쳐서 실행하는 것과 같다.
  * ego(\G)가 세로로 길게 출력하는 것과 달리 기본 출력 모드(테이블)로 출력하는 것의 의미한다.
  * system(\!) - Unix 전용
  * system으로 돌아가지 않고 커맨드 쉘의 명령어를 실행할 수 있다.
  * rehash(\#)
  * 데이터베이스 이름, 테이블 이름, 컬럼 이름등의 자동 완성 기능(name completion)을 위한 정보를 입력하는 중에 다시 수집한다.
  * 기본적 --auto-rehash 옵션이 켜져 있으므로 특별히 쓸 일은 없어보인다.
  * charset(\C)
  * 기본 캐릭터 셋을 변경하여, SET NAMES 명령을 수행함.
  * auto-reconnect가 활성화 되어 있을 경우에 클라이언트와 서버 사이의 캐릭터셋을 다시 동기화하는 역할을 한다는데, SET NAMES 명령을 그냥 수행하는 것과의 차이를 잘 모르겠음.

  

  

