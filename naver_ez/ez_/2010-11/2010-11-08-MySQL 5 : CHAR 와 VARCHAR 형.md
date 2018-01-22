Title: MySQL 5 : CHAR 와 VARCHAR 형
Time: 05:05:00

### [http://dev.mysql.com/doc/refman/5.0/en/char.html](http://dev.mysql.com/do
c/refman/5.0/en/char.html)

CHAR는 고정형이고, VARCHAR는 가변형이라는 정도의 지식만 가지고 데이터베이스를 다루는 한국어권 사용자들을 위해, MySQL 레퍼런스
문서의 해당 내용을 번역해보았다.

  

mysqlkorea에서도 본 내용을 번역하여 게시하고 있지만, 의역이 마음에 들지 않고 일부 삭제된 부분이 있어 다시
번역했다.mysqlkorea의 문서는 다음 링크를 통해 열람할 수 있다.

[http://www.mysqlkorea.co.kr/sub.html?mcode=manual&scode=01&m_no=21688&cat1=11
&cat2=334&cat3=346&lang=k](http://www.mysqlkorea.co.kr/sub.html?mcode=manual&s
code=01&m_no=21688&cat1=11&cat2=334&cat3=346&lang=k)

  

  

아래 문서를 읽는 것 조차 귀찮은 분들을 위해 내용을 요약하고, 첨언하면 다음과 같다.

  * CHAR형은 고정형. 최대 길이는 255.
  * VARCHAR형은 가변형. 최대 길이는 255, MySQL 5.0.3 이후부터는 65,535까지 가능.
  * VARCHAR형은 255글자 이하에는 1바이트, 그 이상은 2바이트의 추가 공간을 필요로 한다.
  * 4.1 이후 버전부터는 CHAR(n), VARCHAR(n)에서 n은 바이트가 아니라, 글자 수를 의미. 즉, 캐릭터 셋의 영향을 받는다.
  * 문자열 뒤에 이어지는 공백들은 열의 형태/버전/SQL 모드에 따라 다르게 처리될 수 있다.
  * 임의의 바이트 배열을 저장할 때에는 BLOB를 선택하라.
  * CHAR / VARCHAR형을 비교하거나 정렬할 때에 뒤따르는 공백은 무시된다. 인덱스도 마찬가지.
  * VARCHAR형이 포함된 열을 삭제/갱신 하는 경우에는 테이블에 사용되지 않는 파편이 생길 수 있다. 이와 같은 가변 길이 행 형태의 테이블은 가끔 OPTIMIZE TABLE [tablename]을 통해 파편을 제거하여 디스크 용량 절약(테이블 스페이스를 쓰지 않는 경우)과 읽기 속도의 개선을 꾀할 수 있다.

  

  

### 10.4.1. CHAR 와 VARCHAR 형

CHAR와 VARCHAR 형은 유사하지만, 저장하고 읽어들이는 부분에는 다르다. MySQL 5.0.3 이후로는 최대 길이와 남은 공간의 보관
여부에 대해서도 달라졌다.

CHAR와 VARCHAR형은 보관하고자 하는 문자열의 최대 길이를 포함하여 선언하게 된다. 예를 들어, CHAR(30)은 30 글자까지
보관할 수 있다.

CHAR열의 길이는 테이블을 만들 때에 지정한 길이로 고정되며, 길이는 0부터 255까지 가능하다. CHAR값을 저장할 때는 문자열의 우측에
공백을 넣어 지정된 길이에 맞추게 된다. 값을 읽어들일 때에는 공백을 제거해서 읽는다.

VARCHAR열의 값은 가변 길이 문자열이다. 지정할 수 있는 길이는 0부터 255까지이며, MySQL 5.0.3 이후에는 0부터
65,535까지 지정할 수 있다. MySQL 5.0.3 이후 버전에서의 VARCHAR 유효 최대 길이는 최대 열 크기(최대
65,535바이트)와 캐릭터 셋의 사용에 영향을 받는다.

CHAR형과는 다르게, VARCHAR형은 1바이트 혹은 2바이트의 값을 앞부분에 저장하며, 이는 값의 크기가 몇 바이트인지 나타낸다.
255글자 이하일 때는 1바이트, 그 이상이면 2바이트를 차지한다.

엄격한 SQL 모드(strict SQL mode)가 활성화되지 않은 상태에서, 열의 최대 길이를 초과하여 값을 저장하면, 값을 잘라서
보관하고 경고를 발생시킨다. 엄격한 SQL 모드를 활성화하면 공백이 아닌 문자열을 자를 때에 경고 대신 에러를 발생시키고 값을 추가하지
못하도록 할 수 있다. 자세한 내용은 다음 링크를 참고한다.[Section5.1.6, “Server SQL
Modes”](http://dev.mysql.com/doc/refman/5.0/en/server-sql-mode.html).

VARCHAR열에 해당 열의 길이를 초과하는 공백들은 SQL 모드에 관계없이 잘린 후 저장되며, 경고를 발생시킨다. CHAR열의 경우에는
마찬가지로 동작하지만, 경고가 발생하지 않는다.

VARCHAR 값은 저장될 때에 공백이 추가되지 않는다. 뒤따르는 공백에 대한 처리는 버전에 따라 다르다. MySQL 5.0.3부터는 표준
SQL과의 호환성을 위해 뒤따르는 공백들을 제거하지 않고 보관하며, 읽어들일 때도 보존해준다. MySQL 5.0.3 이전에는 저장될 때에
뒤따르는 공백들은 제거되었고, 이는 값을 읽어들일 때에도 제거된 채로 읽힘을 의미한다.

MySQL 5.0.3 이전에 뒤따르는 공백들을 유지하기 위해서는 BLOB나 TEXT 형을 선택해야 했다. 또한, 암호화된 값이나 압축 기능을
통해 얻어진 임의의 바이트 형태의 값을 보관할 때에는 CHAR나 VARCHAR형 보다는 BLOB를 선택하는 것이, 데이터의 변형을 가져올
공백 제거에 따른 잠재적인 문제점으로부터 피할 수 있게 해준다.

다음 표는 문자열을 CHAR(4)와 VARCHAR(4) 열에 보관할 때의 결과를 통해 CHAR와 VARCHAR 형의 차이점을 보여준다.
(모든 열은 latin1과 같은 1바이트 캐릭터 셋을 사용하는 것으로 가정한다.)

값`CHAR(4)`필요한 저장소 크기`VARCHAR(4)`필요한 저장소 크기

`''`

`''`

4 bytes

`''`

1 byte

`'ab'`

`'ab'`

4 bytes

`'ab'`

3 bytes

`'abcd'`

`'abcd'`

4 bytes

`'abcd'`

5 bytes

`'abcdefgh'`

`'abcd'`

4 bytes

`'abcd'`

5 bytes

마지막 열의 값은 엄격한 SQL 모드를 사용하지 않을 때만 적용된다. 만약 엄격한 SQL 모드로 MySQL이 동작한다면, 길이를 초과하는
값을 저장되지 않고 에러를 발생시키게 된다.

CHAR 열은 값을 읽을 때, 뒤의 공백을 제거하기 때문에, CHAR(4)와 VARCHAR(4)에 주어진 값과 읽었을 때 얻어진 값은 항상
같지는 않다. 다음은 이 차이를 보여주는 예제이다.

    
    mysql> **CREATE TABLE vc (v VARCHAR(4), c CHAR(4));**
    Query OK, 0 rows affected (0.01 sec)
    
    mysql> **INSERT INTO vc VALUES ('ab  ', 'ab  ');**
    Query OK, 1 row affected (0.00 sec)
    
    mysql> **SELECT CONCAT('(', v, ')'), CONCAT('(', c, ')') FROM vc;**
    +---------------------+---------------------+
    | CONCAT('(', v, ')') | CONCAT('(', c, ')') |
    +---------------------+---------------------+
    | (ab  )              | (ab)                |
    +---------------------+---------------------+
    1 row in set (0.06 sec)
    

  

CHAR와 VARCHAR 열에 쓰여진 값들을 정렬하거나 비교할 때에는 해당 열이 가지고 있는 캐릭터 셋 - 콜레이션(collation)의
영향을 받는다. 모든 MySQL의 콜레이션은PADSPACE이다. 이는 MySQL의 CHAR와 VARCHAR 값들은 뒤따르는 공백의 영향 없이
비교될 수 있음을 의미한다.

    
    mysql> **CREATE TABLE names (myname CHAR(10), yourname VARCHAR(10));**
    Query OK, 0 rows affected (0.09 sec)
    
    mysql> **INSERT INTO names VALUES ('Monty ', 'Monty ');**
    Query OK, 1 row affected (0.00 sec)
    
    mysql> **SELECT myname = 'Monty  ', yourname = 'Monty  ' FROM names;**
    +--------------------+----------------------+
    | myname = 'Monty  ' | yourname = 'Monty  ' |
    +--------------------+----------------------+
    |                  1 |                    1 |
    +--------------------+----------------------+
    1 row in set (0.00 sec)
    

VARCHAR열에 값을 저장하기 전에 공백을 제거하는 MySQL 버전을 사용하고 있어도, SQL 모드의 활성 또는 비활성화되어 있어도 관계가
없으며, 모든 MySQL 버전에 해당한다.

알림

MySQL 캐릭터 셋과 콜레이션은 다음을 참고한다. [Section9.1, “Character Set
Support”](http://dev.mysql.com/doc/refman/5.0/en/charset.html).

이 같은 경우에 대해 뒤따르는 공백들은 제거되거나 비교 시에 무시하게 되므로, 해당 열이 유일한 인덱스(unique index)를 요구하는
경우에, 뒤따르는 공백의 수만 다르고 내용이 같은 문자열들을 입력하면 중복키 에러를 발생시킨다. 예를 들어, 해당 테이블이 'a'를 가지고
있는 상태에서 'a '를 저장하려 하면 중복키 에러가 발생한다.

