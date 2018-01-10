Title: MySQL : InnoDB 테이블을 OPTIMIZE 하려고? 잠깐~! (번역)
Time: 17:21:00

원문 :[Thinking about running OPTIMIZE on your Innodb Table ?
Stop!](http://www.mysqlperformanceblog.com/2010/12/09/thinking-about-running-
optimize-on-your-innodb-table-stop/) /Posted by [Peter
Zaitsev](http://www.percona.com/about-us/our-team/peter-zaitsev/)

링크 :[http://www.mysqlperformanceblog.com/2010/12/09/thinking-about-running-
optimize-on-your-innodb-table-
stop/](http://www.mysqlperformanceblog.com/2010/12/09/thinking-about-running-
optimize-on-your-innodb-table-stop/)

출처 : MySQL Performance Blog (
[http://www.mysqlperformanceblog.com](http://www.mysqlperformanceblog.com) )

번역 : 박현우 (ez.amiryo@gmail.com / [@lqez](http://twitter.com/lqez))

  

InnoDB/XTraDB 테이블은 수시로 재구성을 함으로써 성능적인 혜택을 얻는다. 데이터를 물리적으로 Primary Key 순서에 맞게
나열할 뿐 아니라, Primary Key와 인덱스의 페이지도 재배열하여 더 나은 성능과 더 적은 공간 소비를 가능하게 한다. 허나, 무작정
OPTIMIZE TABLE을 수행하는 것은 최선의 방법이 아니다.

  

만약 Percona Server with XtraDB에서 InnoDB 플러그인을 사용중이라면, '삽입' 방식이 아닌 '정렬' 방식의 인덱스를
생성할 수 있는 '멋진' 기능을 통해 이득을 볼 수 있다. 이 작업은 UUID와 같은 무작위 순으로 입력된 대용량의 인덱스에 대해 특별히
빠르게 수행될 수 있을 뿐 아니라, 더 효율적인 공간 활용을 가능하게 한다. 문제는... InnoDB 테이블에 대한 OPTIMIZE
TABLE 명령은 이유를 불문하고 그러한 장점을 얻을 수 없다.

  

버퍼 풀에 할당된 메모리보다 10배 정도 큰 테이블에 대해 최적화 작업을 수행한 아래 벤치마크를 살펴보자.

  

**SQL:**

  1. **CREATE** **TABLE** `a` **(**
  2. `id` int**(**10**)** **UNSIGNED** **NOT** **NULL** **AUTO_INCREMENT**,
  3. `c` char**(**64**)** **DEFAULT** **NULL**,
  4. **PRIMARY** **KEY** **(**`id`**)**,
  5. **KEY** `c` **(**`c`**)**
  6. **)** ENGINE=InnoDB **AUTO_INCREMENT**=12582913 **DEFAULT** CHARSET=latin1
  7.   8. mysql> **SELECT** * **FROM** a **ORDER** **BY** id **LIMIT** 10;
  9. +_----+------------------------------------------+_
  10. | id | c |
  11. +_----+------------------------------------------+_
  12. | 1 | 813cf02d7d65de2639014dd1fb574d4c481ecac7 |
  13. | 2 | 62960f5d5d50651e5a5983dacaedfa9a73a9ee87 |
  14. | 3 | cea33998792ffe28b16b9272b950102a9633439f |
  15. | 4 | 8346a7afa0a0791693338d96a07a944874340a1c |
  16. | 5 | b00faaa432f507a0d16d2940ca8ec36699f141c8 |
  17. | 6 | 8e00926cf6c9b13dc8e0664a744b7116c5c61036 |
  18. | 7 | f151fe34b66fd4d28521d5e7ccb68b0d5d81f21b |
  19. | 8 | 7fceb5afa200a27b81cab45f94903ce04d6f24db |
  20. | 9 | 0397562dc35b5242842d68de424aa9f0b409d60f |
  21. | 10 | af8efbaef7010a1a3bfdff6609e5c233c897e1d5 |
  22. +_----+------------------------------------------+_
  23. 10 rows **IN** **SET** **(**0.04 sec**)**
  24.   25. _# This is just random SHA(1) hashes_
  26.   27. mysql> **OPTIMIZE** **TABLE** a;
  28. +_--------+----------+----------+-------------------------------------------------------------------+_
  29. | **TABLE** | Op | Msg_type | Msg_text |
  30. +_--------+----------+----------+-------------------------------------------------------------------+_
  31. | test.a | **OPTIMIZE** | note | **TABLE** does **NOT** support **OPTIMIZE**, doing recreate + analyze instead |
  32. | test.a | **OPTIMIZE** | **STATUS** | OK |
  33. +_--------+----------+----------+-------------------------------------------------------------------+_
  34. 2 rows **IN** **SET** **(**3 hours 3 min 35.15 sec**)**
  35.   36. mysql> **ALTER** **TABLE** a **DROP** **KEY** c;
  37. Query OK, 0 rows affected **(**0.46 sec**)**
  38. Records: 0 Duplicates: 0 Warnings: 0
  39.   40. mysql> **OPTIMIZE** **TABLE** a;
  41. +_--------+----------+----------+-------------------------------------------------------------------+_
  42. | **TABLE** | Op | Msg_type | Msg_text |
  43. +_--------+----------+----------+-------------------------------------------------------------------+_
  44. | test.a | **OPTIMIZE** | note | **TABLE** does **NOT** support **OPTIMIZE**, doing recreate + analyze instead |
  45. | test.a | **OPTIMIZE** | **STATUS** | OK |
  46. +_--------+----------+----------+-------------------------------------------------------------------+_
  47. 2 rows **IN** **SET** **(**4 min 5.52 sec**)**
  48.   49. mysql> **ALTER** **TABLE** a **ADD** **KEY****(**c**)**;
  50. Query OK, 0 rows affected **(**5 min 51.83 sec**)**
  51. Records: 0 Duplicates: 0 Warnings: 0

  

어떤가?! 테이블 최적화를 그냥 수행하면 3시간도 넘게 걸리던 것에 비해, Primary Key를 제외한 인덱스를 내리고 테이블 최적화를
진행한 후에 다시 인덱스를 복원하는 작업은 10분 밖에 걸리지 않는다. 거의 20배나 빠를 뿐 아니라, 최종적으로 더 작은 크기의 인덱스를
얻을 수 있다.

  

따라서, 만약 이 트릭을 이용해 테이블 최적화를 수행하고자 한다면, 테이블이 인덱스 없이 노출되어도 괜찮은 슬레이브 단에서 작업하는 것이
좋다. 단, InnoDB 테이블에 락을 걸 때에, 인덱스 없이 테이블을 읽는 많은 수의 쿼리들로 인해 컴퓨터(box)가 멈추는 일이 없어야
함을 보장해야 함을 유의하라.

  

이 트릭을 테이블 재생성을 필요로 하는 ALTER TABLE 시에도 활용할 수 있다. (역주:MySQL은 ALTER TABLE 작업을 새로운
스키마를 가지는 임시 테이블 생성 > 임시 테이블로 복제 > 기존 테이블 DROP > 임시 테이블의 이름을 기존 테이블의 이름으로 변환하는
식으로 수행한다) 모든 인덱스를 제거하고, ALTER를 수행한 후에 인덱스를 복원하는 것이 그냥 ALTER TABLE을 수행하는 것보다 훨씬
빠르다.

  

덧) 왜 이런 경우에 정렬을 통해 인덱스를 생성하는 기능이 지원되지 않는지 모르겠다. 고수준 명령어나 도구들(예를 들어 mysqldump)이
왜 인덱스를 만드는데 느리디 느린 '삽입 방식'을 사용해, 이러한 장점을 가질수 없게 만들어졌는지 이해할 수 없다.

  

  

----

  

과거 MySQL로 MMORPG의 대용량 로그 데이터를 다루던 경험에 비추어 보아도, 아래의 동작들은 정말 이해가 가지 않았다.

(1) Row의 용량이 줄어드는 ALTER TABLE의 경우에도 위에서 언급한 것과 같이 전체 rebuilding을 하는 것.

(2) dump된 데이터를 다시 복원할 때에, CREATE INDEX를 나중에 수행하지 않아 느린 것. -> 생각해보면 MyISAM에
대해서는 /*!40000 ALTER TABLE [table] DISABLE KEYS */; 을 통해서 이미 하고 있었네.

  

