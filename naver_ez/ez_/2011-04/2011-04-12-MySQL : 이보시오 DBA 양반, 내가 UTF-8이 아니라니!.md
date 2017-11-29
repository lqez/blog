Title: MySQL : 이보시오 DBA 양반, 내가 UTF-8이 아니라니!
Time: 20:33:00

![](c0058317_4c518474c55c3.jpg)

  

MySQL에서 한글을 저장하다보면, 분명 캐릭터셋을 utf8으로 지정한 것 같은데, 실제로는 UTF-8이 아닌(?) 경우가 생긴다.

  1. MySQL을 설치하고 데이터베이스를 생성한다.
  2. 테이블을 만들 때, CHARSET을 utf8으로 지정해서 만든다.
  3. 웹서비스를 utf-8으로 작성한다.
  4. 사용자에게 입력값을 받는다.
  5. 웹페이지에 입력받은 값을 쿼리로 추출하여 다시 출력해본다. 잘 나온다.
  6. (중략)
  7. UTF-8 터미널에서 MySQL 클라이언트 프로그램을 통해 서버에 접속한다.
  8. SELECT * FROM [table]을 해보니 한글이 깨져있다. 어?!

  

MySQL 클라이언트에서 SET NAMES latin1을 하고 SELECT 하면 값이 정상적으로 나오는데, SET NAMES utf8을
수행하면 값이 깨져보인다.테이블이나 컬럼의 캐릭터셋은 utf8인데, 값을 저장하는 시점에서 사용된 커넥터의 기본 캐릭터셋이 utf8이
아니었을 때 발생하는 문제다.

  

  

이를 해결하기 위해 일반적으로는 mysqldump를 통해 latin1으로 데이터베이스를 덤프하고, 이 파일을 iconv나 기타 에디터를 통해
latin1 -> utf-8 변환을 수행한 후, 다시 넣는 식으로 작업한다.

  

  

  

나도 늘 이런 방식으로 복원했었는데, 이 작업이 불합리하다고 생각되어 다음과 같이 작업해보았다.

  

  1. ALTER TABLE [table] CONVERT TO CHARSET latin1;
  2. ALTER TABLE [table] MODIFY [column] BLOB;
  3. ALTER TABLE [table] MODIFY [column] VARCHAR(255) CHARSET utf8; // VARCHAR(255)등 원래 형식으로 복원
  4. ALTER TABLE [table] CONVERT TO CHARSET utf8;

  

[http://dev.mysql.com/doc/refman/5.1/en/alter-
table.html](http://dev.mysql.com/doc/refman/5.1/en/alter-table.html)

위 레퍼런스 문서에 따르면, BLOB에서 VARCHAR나 TEXT등으로 ALTER가 발생할 경우에는 별도의 컨버젼이 발생하지 않기 때문에,
올바른 복원이 가능해진다.

  

  

아래에 MySQL 작업 예제를 첨부한다.

  

> mysql> show create table charset_test;

>

> +--------------+------------------------------------------------------------
-------------------------------------------+

>

> | Table | Create Table |

>

> +--------------+------------------------------------------------------------
-------------------------------------------+

>

> | charset_test | CREATE TABLE `charset_test` (

>

> `name` varchar(100) DEFAULT NULL

>

> ) ENGINE=MyISAM DEFAULT CHARSET=utf8 |

>

> +--------------+------------------------------------------------------------
-------------------------------------------+

>

> 1 row in set (0.00 sec)

>

>

>

> mysql> set names latin1;

>

> Query OK, 0 rows affected (0.00 sec)

>

>

>

> mysql> select * from charset_test;

>

> +--------------+

>

> | name |

>

> +--------------+

>

> | 가나다라 |

>

> +--------------+

>

> 1 row in set (0.00 sec)

>

>

>

> mysql> set names utf8;

>

> Query OK, 0 rows affected (0.00 sec)

>

>

>

> mysql> select * from charset_test;

>

> +-----------------------------+

>

> | name |

>

> +-----------------------------+

>

> | e°€e‚˜e‹¤e¼ |

>

> +-----------------------------+

>

> 1 row in set (0.00 sec)

>

>

>

> mysql> alter table charset_test convert to charset latin1;

>

> Query OK, 1 row affected (0.38 sec)

>

> Records: 1 Duplicates: 0 Warnings: 0

>

>

>

> mysql> alter table charset_test modify name blob;

>

> Query OK, 1 row affected (0.05 sec)

>

> Records: 1 Duplicates: 0 Warnings: 0

>

>

>

> mysql> alter table charset_test modify name varchar(100) charset utf8;

>

> Query OK, 1 row affected (0.04 sec)

>

> Records: 1 Duplicates: 0 Warnings: 0

>

>

>

> mysql> alter table charset_test convert to charset utf8;

>

> Query OK, 1 row affected (0.04 sec)

>

> Records: 1 Duplicates: 0 Warnings: 0

>

>

>

> mysql> select * from charset_test;

>

> +--------------+

>

> | name |

>

> +--------------+

>

> | 가나다라 |

>

> +--------------+

>

> 1 row in set (0.01 sec)

>

>

>

> mysql>

  

