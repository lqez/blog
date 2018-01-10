Title: PHP + mongoDB 사용하기
Time: 14:30:00

**- mongoDB 설치**

mongoDB 설치는 이전에 작성한 포스팅을 참고.

( 참고 :[http://blog.naver.com/ez_/140130471953](http://blog.naver.com/ez_/14013
0471953) )

  

  

  

  

**- php mongoDB 모듈 설치**

현 세대의 PHP에는 mongoDB 모듈이 기본 설치되어 있진 않지만,

unixish 시스템에서는 다음 명령어로 간단히 설치된다.

(참고 :[http://www.php.net/manual/en/mongo.installation.php](http://www.php.net/
manual/en/mongo.installation.php))

> sudo pecl install mongo

  

그리고 사용중인 php.ini에 다음 내용을 추가한다.

extension=mongo.so

**  
**

**  
**

**  
**

**  
**

**- Mongo Core Class 사용법**

mongoDB는 다음과 같은 데이터 구성을 취한다. 기존 RDBMS와 비교하면 스키마를 통해 정의하고 사용했던 Table 대신, 스키마는
없지만 문서(데이터)의 집합을 의미하는 Collection이 사용된다.

mongoDB

Server/Connection

Database

Collection

Cursor

기존 RDBMS

Server/Connection

Database

Table

Cursor

  

  

테스트를 위해 Mongo class의 인스턴스를 생성하고 문서를 저장해본다.

mongoDB는 원래 JSON 개체를 보관하는 데이터베이스이므로, PHP에서는 array를 통해 값을 읽고 쓸 수 있다.

예제 1: 간단한 Mongo Core Class 사용법

<?php

$mongo=newMongo("mongodb://localhost:27017",[array](http://www.php.net/array)(
"persist"=>""));

$testDB=$mongo->test;

  
$user1=[array](http://www.php.net/array)("id"=>"lqez","class"=>"surplus");

$testDB->user->insert($user1);

  
$user2=[array](http://www.php.net/array)("id"=>"trustin","class"=>"superb");

$testDB->user->insert($user2);

  
$user3=[array](http://www.php.net/array)("id"=>"lono","class"=>"superb");

$testDB->user->insert($user3);

  
  
$users=$testDB->user->find();

foreach($usersas$user)

{

[print_r](http://www.php.net/print_r)($user);

}

?>

  

$mongo 인스턴스가 서버 개체이며, $mongo->test 와 같이 임의의 데이터베이스를 선택할 수 있다.

서버 개체 생성시 기본적으로 해당 개체의 해제시, mongoDB로의 연결을 해제하게 되므로, persist 옵션을 통해 지속적인 연결을
사용할 수 있도록 한다. persist의 값으로 해당 연결의 이름을 줄 수 있으며, 같은 이름끼리는 같은 연결을 사용하게 된다.

( 참고 :[http://www.php.net/manual/en/mongo.construct.php](http://www.php.net/ma
nual/en/mongo.construct.php) )

  

위의 예제에서는 코어 클래스를 다음과 같이 사용하고 있다.

Class Mongo

Class MongoDB

Class MongoCollection

Class MongoCursor

$mongo

$testDB

$testDB->user

$users

  

소스의 실행 결과는 다음과 같다.

예제 1의 실행 결과

Array

(

[_id] => MongoId Object

(

[$id] => 4df17e1fb26a459740000000

)

  

[id] => lqez

[class] => surplus

)

Array

(

[_id] => MongoId Object

(

[$id] => 4df17e1fb26a459740000001

)

  

[id] => trustin

[class] => superb

)

Array

(

[_id] => MongoId Object

(

[$id] => 4df17e1fb26a459740000002

)

  

[id] => lono

[class] => superb

)

  

모든 mongoDB 개체는 고유(unique)의 _id 값을 가지며, 인덱스가 지정되어 있어 _id 를 이용해 해당 개체에 빠르게 접근하는
것이 가능하다.

  

위의 예제에서, class가 superb인 user만 얻고 싶을 때는 다음과 같이 조건을 지정할 수 있다.

예제 2. 조건 지정하여 개체 얻기

<?php

$mongo=newMongo("mongodb://localhost:27017",[array](http://www.php.net/array)(
"persist"=>""));

$testDB=$mongo->test;

  

$users=$testDB->user->find([array](http://www.php.net/array)('class'=>'superb'
));

foreach($usersas$user)

{

[print_r](http://www.php.net/print_r)($user);

}

?>

  

  

  

  

**- JavaScript를 직접 사용하기**

모듈에 내장된 코어 클래스를 통해 mongoDB를 사용할 수도 있지만, 경우에 따라서는 mongoDB의 서버쪽에 내장된 자바스크립트 엔진을
사용하는 것이 더 편리한 경우도 있다. 이를 위해 PHP mongoDB 모듈에서는 execute 함수를 제공한다.

( 참고 :[http://www.php.net/manual/en/mongodb.execute.php](http://www.php.net/ma
nual/en/mongodb.execute.php) )

  

예제 3. execute 함수로 자바스크립트 직접 사용하기

<?php

$mongo=newMongo("mongodb://localhost:27017",[array](http://www.php.net/array)(
"persist"=>""));

$testDB=$mongo->test;

  
$ret=$testDB->execute('db.user.find({"class":"superb"}).count()');

print_r($ret);

?>

  

execute 함수를 통해 전달된 코드는 mongoDB 서버에서 해석되어 실행되며, 그 실행 결과와 에러 코드가 리턴된다.

단, 전달된 코드가 실행되는 동안 전체 데이터베이스에 write lock이 걸리므로, 오래 걸리는 요청은 되도록 map/reduce 등으로
변경하여 사용하는 것이 권장된다.

예제 3의 실행 결과

Array

(

[retval] => 2

[ok] => 1

)

  

  

- 참고 링크

mongo DB

[http://www.mongodb.org/](http://www.mongodb.org/)

  

SQL to Mongo Mapping Chart / SQL에 익숙한 사용자는 이 문서를 통해 mongo 문법을 손쉽게 익힐 수 있다.

[http://www.mongodb.org/display/DOCS/SQL+to+Mongo+Mapping+Chart](http://www.mo
ngodb.org/display/DOCS/SQL+to+Mongo+Mapping+Chart)

  

