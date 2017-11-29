Title: Predis, using redis on PHP
Time: 14:57:00

About Redis

  

Redis([http://redis.io/](http://redis.io/))는 진보된 메모리 기반 Key-Value 데이터베이스다.

Memcached([http://memcached.org/](http://memcached.org/))와 비교하면, LIST / HASH /
SET을 비롯하여 정렬된 SET 등 다양한 자료 형식을 제공함과 동시에 AOF / RDB 등 디스크 기반 백업이 가능한 것이 장점이다.

  

Redis의 특징과 장점에 대해서는 다른 글에서 상세히 설명하고 있으므로, 이 글에서는 PHP에서 Redis에 접근하기 위한 방법과 간략한
사용 예를 설명하고자 한다.

  * Redis Data types /[http://redis.io/topics/data-types](http://redis.io/topics/data-types)
  * Redis vs Memcached Benchmark /[http://systoilet.wordpress.com/2010/08/09/redis-vs-memcached/](http://systoilet.wordpress.com/2010/08/09/redis-vs-memcached/)
  * 각종 Key-Value DB들의 비교 /[http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis](http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis)
  * Redis로 빠르고 가벼운 웹어플리케이션 만들기 (by [@tebica](http://twitter.com/tebica)) /[http://dev.paran.com/2011/07/28/redis-buildingfast-lightweight-webapp/](http://dev.paran.com/2011/07/28/redis-buildingfast-lightweight-webapp/)

Redis의 PHP client는[http://redis.io/clients](http://redis.io/clients) 에도 소개되어
있듯 여러 가지가 있는데, 이 글에서는 가장 널리 이용되는
Predis([https://github.com/nrk/predis](https://github.com/nrk/predis))의 설치와 사용
방법을 알아본다.

  

  

  

Predis Installation

  

PHP Packagist / Composer를 통해 설치가 가능하며, 기존 방식인 PEAR에 채널을 추가하는 것으로도 가능하다.
Composer는 brew나 pip와 같이 패키지 의존성을 검사하여 필요한 라이브러리를 자동으로 설치해주는 패키지 매니저의 일종으로, PHP
라이브러리들을 대상으로 하며 Packagist를 통해 패키지를 관리한다.

  

참고 : Predis package in packagist /[http://packagist.org/packages/predis/predis
](http://packagist.org/packages/predis/predis)

참고 : Composer /[http://getcomposer.org/](http://getcomposer.org/)

참고 : Packagist /[http://packagist.org/](http://packagist.org/)

참고 : Predis PEAR /[http://pear.nrk.io/](http://pear.nrk.io/)

  

- Composer로 설치하기

> # Composer 설치 ( Composer를 사용하기 위해선 php.ini에detect_unicode = Off를 설정해야 함 )

>

> $ curl
-s[http://getcomposer.org/installer](http://getcomposer.org/installer)| php

>

> # 의존성 파일 생성

>

> $echo '{ "require": { "predis/predis": "*" } }' > composer.json

>

> # 패키지 설치

>

> $php composer.phar install

설치 후에는 vendor/ 디렉토리 이하에 설치되므로, php에 vender/autoload.php를 포함시켜 간단히 사용할 수 있다.

> <?php

>

> require 'vendor/autoload.php';

>

> Predis\Autoloader::register();

>

> ?>

- PEAR로 설치하기

> # 채널 추가

>

> # pear channel-discover pear.nrk.io

>

> # Predis 패키지 설치

>

> # pear install nrk/Predis

composer의 경우와 달리 PEAR package로 등록되었기 때문에, 포함해야 하는 파일명이 다르다.

> <?php

>

> require 'Predis/Autoloader.php';

>

> Predis\Autoloader::register();

>

> ?>

  

Using Predis

아래는 가장 단순한 형태의 Predis 사용 방법이다. 인자 없이 연결하면 로컬호스트의 기본 포트(6379)를 이용하여 접속을 시도한다.

> <?php

>

> require '...'; // 설치방식에 따라 적절한 파일을 포함한다.

>

> Predis\Autoloader::register();

>

>

>

> $redis = new Predis\Client(); // Redis 서버에 접속.

>

> $redis->set('foo', 'bar'); // 'foo'에 'bar'를 저장.

>

> $value = $redis->get('foo'); // 'bar'가 리턴됨.

>

> ?>

Redis 홈페이지의 명령어 목록이 그대로 함수의 이름과 대응되므로, 편리하게 사용할 수 있다.﻿

참고 :﻿[http://redis.io/commands](http://redis.io/commands)

아래 예제는 redis에서 지원하는 LIST 자료 형식을 사용하는 방법을 보여준다.

> <?php

>

> require '...'; // 설치방식에 따라 적절한 파일을 포함한다.

>

> Predis\Autoloader::register();

>

>

>

> $redis = new Predis\Client(); // Redis 서버에 접속.

>

> $redis->rpush( 'fruit', 'apple' ); // 'fruit' LIST의 끝에 'apple'추가.

>

> $redis->rpush( 'fruit', 'orange' ); // 'orange' 추가.

>

> $redis->rpush( 'fruit', 'banana' ); // 'banana' 추가.

>

>

>

> $value = $redis->lpop( 'fruit' ); // LIST의 왼쪽에서 아이템을 꺼냄. 'apple' 리턴.

>

> ?>

참고 : Predis github
/[https://github.com/nrk/predis](https://github.com/nrk/predis)

참고 : Predis examples /[https://github.com/nrk/predis/tree/v0.7/examples](https
://github.com/nrk/predis/tree/v0.7/examples)

