Title: 2012-08-02 개발일지 : Django Cross-database relationship 제한 회피하기
Time: 15:08:00

Problem

  

서비스의 종류나 형태가 늘어나면, 서비스 사이에 공유되어야 하는 정보가 있고, 공유되지 않아야 하는 정보가 있다.

  

제대로 된 'The Right Way' 구현이라면, 공유되어야 하는 정보는 API 나 라이브러리 형태로 뜯어내 사용해야 하지만,

마음이 급한(이라고 쓰고, '일정이 급한'으로 읽는다) 경우에는 그냥 데이터베이스 레벨에서 공유하고픈 것이 사람 마음.

  

하지만,Django는 서로 다른 데이터베이스 인스턴스 사이의 외래키를 허용하지 않는 문제가 있다.

[https://docs.djangoproject.com/en/dev/topics/db/multi-db/#cross-database-
relations](https://docs.djangoproject.com/en/dev/topics/db/multi-db/#cross-
database-relations)

  

계정은 공유하고 서비스 별 데이터는 따로 쓰고 싶었던 것인데, 위의 제한 때문에 각자의 서비스에서 'ForeignKey(User)'와 같은
공용 모델에 대한 외래키 필드를 설정할 수 없는 문제가 생긴다.

  

구글 검색을 통해 알아본 결과, 이를 우회하기 위한 몇 가지 방법이 있는데,

- ForeignKey를 확장하여 별도 구현하거나,

링크 :[http://stackoverflow.com/questions/5493241/how-to-work-around-lack-of-
support-for-foreign-keys-across-databases-in-
django](http://stackoverflow.com/questions/5493241/how-to-work-around-lack-of-
support-for-foreign-keys-across-databases-in-django)

- ForeignKey로 직접 연결하지 않고, IntergerField 로 생성한 다음, 별도의 함수를 이용해 relation을 보장하는 방법이 있다.

링크 :[http://djangosnippets.org/snippets/2353/](http://djangosnippets.org/snipp
ets/2353/)

  

  

  

Ad-hoc workaround

  

둘 다 작업하기가 귀찮아서(!), MySQL에서 지원하는 VIEW를 사용하여 문제를 우회해보았다.

- 공유해야하는 테이블을 공통으로 사용할 데이터베이스 쪽으로 이전하고,

- 각자의 데이터베이스에 공통 데이터베이스의 테이블에 대한 뷰를 생성한다.

- 입출력 모두 이상 무.

- VIEW를 지원하는 데이터베이스라면 대부분 사용 가능할 것으로 보임.

- 장점 : Django 코드의 수정이 필요 없다.

- 단점 : 'The Right Way'가 아니다! 그리고, 어떤 잠재적인 문제가 있을지 모름.

  

예) comico_svr1 데이터베이스의 account 테이블이 comico_svr2 데이터베이스와 같이 사용해야 할 때, 아래와 같이
작업한다.

> CREATE DATABASE comico;

>

> CREATE TABLE comico.account LIKE comico_svr1.account;

>

> INSERT INTO comico.account SELECT * FROM comico_svr1.account;

>

> DROP TABLE comico_svr1.account;

>

> CREATE VIEW comico_svr1.account AS SELECT * FROM comico.account;

>

> CREATE VIEW comico_svr2.account AS SELECT * FROM comico.account;

InnoDB 등의 database-level relation consistency check가 가능한 데이터베이스에서는, 위와 같이 처리할
경우 django에서 기본적으로 설정하는 외래키 제약조건을 위배하게 된다. 이를 피하기 위해 아래의 시그널을 등록하는 것이 필요하다.

> from django.db.backends.signals import connection_created

>

> from django.dispatch import receiver

>

>

>

> @receiver(connection_created)

>

> def disable_constraints(sender, connection, **kwargs):

>

> connection.disable_constraint_checking()

권장할 만한 방법이라고 생각하지는 않지만, 이런 방법으로도 우회할 수 있다는 정도의 의미.

  

  

