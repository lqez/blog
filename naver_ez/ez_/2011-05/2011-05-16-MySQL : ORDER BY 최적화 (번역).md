Title: MySQL : ORDER BY 최적화 (번역)
Time: 17:02:00

####

### 번역 : 박현우(ez.amiryo@gmail.com /[@lqez](http://twitter.com/lqez))

출처 :[http://dev.mysql.com/doc/refman/5.1/en/order-by-
optimization.html](http://dev.mysql.com/doc/refman/5.1/en/order-by-
optimization.html)

원제 : ORDER BY Optimization

  

이전 레퍼런스 번역들과 마찬가지로, mysqlkorea에서도 본 내용을 번역하여 게시하고 있지만, 의역이 마음에 들지 않고 일부 오역이나
삭제된 부분이 있어 다시 번역했다.mysqlkorea의 문서는 다음 링크를 통해 열람할 수 있다.

[http://www.mysqlkorea.co.kr/sub.html?mcode=manual&scode=01_1&m_no=22505&cat1=
827&cat2=963&cat3=980&lang=k](http://www.mysqlkorea.co.kr/sub.html?mcode=manua
l&scode=01_1&m_no=22505&cat1=827&cat2=963&cat3=980&lang=k)

####

#### 7.3.1.11.`ORDER BY`최적화

MySQL은 조건이 만족할 때, ORDER BY 구문을 인덱스를 이용해 추가적인 정렬 없이 수행할 수 있다.

ORDER BY 절과 인덱스가 정확히 일치하지 않은 경우라도, ORDER BY에 사용되는 컬럼 외에 나머지 컬럼들이 WHERE 절에 의해
상수항으로 결정된다면 사용될 수 있다. 다음의 쿼리는 인덱스가 ORDER BY 절에 사용되는 경우이다.

    
    SELECT * FROM t1
      ORDER BY _key_part1_,_key_part2_,... ;
    
    SELECT * FROM t1
      WHERE _key_part1_=_constant_
      ORDER BY _key_part2_;
    
    SELECT * FROM t1
      ORDER BY _key_part1_ DESC, _key_part2_ DESC;
    
    SELECT * FROM t1
      WHERE _key_part1_=1
      ORDER BY _key_part1_ DESC, _key_part2_ DESC;
    

(역주: 위의 예제들은 인덱스가 CREATE INDEX [index_name] ON [table_name] (key_part1,
key_part2) 와 같이 멀티 컬럼 인덱스로 만들어진 경우에 해당된다.)

한편, WHERE 절에서는 인덱스를 사용하지만, ORDER BY 절에 인덱스를 사용하지 못하는 경우가 있다. 다음과 같은 경우가 그러하다.

  * 서로 다른 키를ORDER BY 에사용하는 경우.
    
    SELECT * FROM t1 ORDER BY _key1_, _key2_;
    

  * 키의 일부를 비연속적(비순차적)으로 사용할 때. (역주:멀티 컬럼 인덱스는 앞 부분부터 사용되어야 한다)
    
    SELECT * FROM t1 WHERE _key2_=_constant_ ORDER BY _key_part2_;
    

  * 오름차순과 내림차순을 섞는 경우.
    
    SELECT * FROM t1 ORDER BY _key_part1_ DESC, _key_part2_ ASC;
    

  * ORDER BY 절에 사용된 키와 열을 가져오기 위해 사용된 키가 다른 경우.
    
    SELECT * FROM t1 WHERE _key2_=_constant_ ORDER BY _key1_;
    

  * ORDER BY 에 키의 컬럼 이름이 아닌 다른 표현을 사용했을 경우.
    
    SELECT * FROM t1 ORDER BY ABS(_key_);
    SELECT * FROM t1 ORDER BY -_key_;
    

  * 여러 테이블을 조인할 때,ORDER BY 열을 가져오는데 사용된 컬럼들이 모두 첫번째 비상수(nonconstant) 테이블에 있어야 하는데 그렇지 않은 경우. (EXPLAIN 결과에서 const 조인 형식을 가지지 않는 첫번째 테이블을 의미한다.)

  * ORDER BY 절과 GROUP BY 절이 다를 경우.

  * ORDER BY 절에 사용된 컬럼의 일부분만 인덱스로 만든 경우, 이 인덱스는 정렬에 사용될 수 없다. 예를 들어 CHAR(20) 형식의 컬럼중, 앞 10 바이트만 인덱스로 만든 경우에 10번째 바이트 이후에 대해서는 인덱스로 알 수가 없고, filesort가 필요하게 된다.

  * MEMORY 형식의 테이블의 HASH 인덱스와 같이, 인덱스가 순차적으로 보관되어 있지 않은 경우.

정렬을 위한 인덱스의 사용 여부는 컬럼 별칭(alias)의 용법에 영향을 받는다. t1.a 컬럼이 인덱스되어 있다고 가정하자. 아래
구문에서, SELECT 목록에 있는 컬럼의 이름은 a다. 이는 t1.a를 나타내고, ORDER BY 절의 a는 이를 참조하여 인덱스를
사용하게 된다.

    
    SELECT a FROM t1 ORDER BY a;
    

아래 구문에서도 마찬가지로, SELECT 목록에 있는 컬럼의 이름은 a이지만, 이것은 별칭에 불과하다. ORDER BY 절의 a는
ABS(a)를 가리키게 되고, 인덱스를 사용할 수 없게 된다.

    
    SELECT ABS(a) AS a FROM t1 ORDER BY a;
    

다음 구문에서 ORDER BY 절은 SELECT 목록에 있는 컬럼의 이름을 가리키지는 않는다. 하지만,t1에 a라는 컬럼이 있어, ORDER
BY 절은 이를 참조하여 인덱스를 사용하게 된다.(당연한 얘기지만, 정렬 결과는 ABS(a)와 무관하게 나온다.)

    
    SELECT ABS(a) AS b FROM t1 ORDER BY a;
    

  

MySQL에서는 기본적으로, GROUP BY col1, col2, ... 는 ORDER BY col1, col2, ... 를 지정한 것과
같은 정렬을 동반한다.명시적으로 같은 컬럼들을 대상으로 하여 ORDER BY 절을 작성한 경우, 정렬이 필요하다 해도 MySQL은 속도에
대한 페널티 없이 최적화를 수행할 수 있다. GROUP BY 절이 포함된 쿼리가 정렬에 의해 불필요한 오버헤드가 발생되는 것을 피하기 위해
ORDER BY NULL을 명시할 수 있다.

    
    INSERT INTO foo
    SELECT a, COUNT(*) FROM bar GROUP BY a ORDER BY NULL;
    

EXPLAIN SELECT ... ORDER BY 구문을 통해 MySQL이 쿼리를 해석하기 위해 인덱스를 사용하는지 여부를 확인할 수
있다.Extra 컬럼에 'Using filesort'는 인덱스를 사용하지 못함을 의미한다.다음 링크를 통해 EXPLAIN에 대한 추가 정보를
확인할 수 있다.[Section7.2.1, “Optimizing Queries
with`EXPLAIN`”](http://dev.mysql.com/doc/refman/5.1/en/using-explain.html).

  

MySQL은 두 가지 결과를 정렬하여 가져오기 위해 filesort 알고리즘을 사용한다. 기존의 방식은 ORDER BY 절의 컬럼들만을
사용한다. 수정된 두번째 방법은 ORDER BY 절의 컬럼들 뿐 아니라, 쿼리에 사용된 모든 컬럼을 사용한다.

옵티마이져는 어떤 filesort 알고리즘을 사용할지 선택한다. 일반적으로, BLOB나 TEXT 컬럼이 있는 경우에만 기존 방식을 사용하고,
그 외의 경우는 수정된 알고리즘을 사용한다.

기존 방식의 filesort 알고리즘은 다음과 같이 동작한다.

  1. WHERE 절에 일치하지 않는 열을 제외하고,테이블 스캐닝이나키에 순서에 따라 모든 열을 읽어들인다.

  2. 각각의 열에 대해 버퍼에 정렬을 위한 키와 열에 대한 포인터의 쌍을 저장해둔다. 버퍼의 크기는 시스템 변수인`[sort_buffer_size](http://dev.mysql.com/doc/refman/5.1/en/server-system-variables.html#sysvar_sort_buffer_size)`의 값에 의해 결정된다.

  3. 버퍼가 가득 차면, 퀵소트를 수행하고 그 결과를 임시 파일에 보관하고, 포인터는 정렬된 블록에 남겨둔다. (만약 모든 쌍이 소트 버퍼안에 들어갈 수 있으면, 임시 파일을 생성하지 않는다.)

  4. 모든 열을 읽을 때까지 위의 과정을 반복한다.

  5. 다른 임시 파일에 대해, 최대 MERGEBUFF(기본값:7)의 영역을 하나의 블록이 될 때까지 다중 병합 작업을 수행한다. 첫번째 파일의 모든 블록이 두번째 파일과 같아질 때까지 반복한다.

  6. MERGEBUFF2(기본값:15) 보다 작은 수의 블록이 남을 때 까지 반복한다.

  7. 마지막 다중 병합 작업시, 정렬 키의 마지막 부분에 해당하는 열을 가리키는 포인터만 결과 파일에 기록하게 된다.

  8. 결과 파일에 기록된 열의 포인터를 이용해, 열을 정렬된 상태로 읽어들인다. 이 과정을 최적화하기 위해, 열 포인터들을 큰 블럭으로 읽고, 정렬한 후, 이를 이용해 정렬된 상태로 열을열 버퍼로읽어들인다. 이 버퍼의 크기는 시스템 변수인[`read_rnd_buffer_size`](http://dev.mysql.com/doc/refman/5.1/en/server-system-variables.html#sysvar_read_rnd_buffer_size)에 의해 결정되며, 이 작업은`sql/records.cc`소스 파일 안에 들어 있다.

이 방식의 하나의 단점은, 열을 두 번씩 읽게 된다는 점이다. WHERE 절을 평가하는 과정에서 한 번 읽고, 쌍(역주:키 값과 열에 대한
포인터에 대한 쌍)을 정렬하는 과정에서 한 번 더 읽게 된다.게다가, 처음에 열을 순차적으로 읽어들인 경우에도(테이블 스캔이 된 경우),
두번째에는 랜덤하게 접근할 수 밖에 없다. (정렬 키는 순서대로지만, 열의 실제 위치는 아니므로)

수정된 filesort 알고리즘은 정렬키와 열 위치뿐 아니라 쿼리에서 요구하는 컬럼들까지도 같이 저장하는 최적화를 구현했다.이를 통해 열을
두 번 읽지 않게 되었고, 이는 다음과 같이 동작한다.

  1. WHERE 절에 해당하는 열을 읽는다.

  2. 각 열에 대해, 정렬에 해당하는 키 값과 열의 위치, 그리고 쿼리에 필요한 컬럼들이 결합된 튜플을 저장한다.

  3. 정렬 키의 값을 이용해 튜플을 정렬한다.

  4. 정렬된 결과로부터 열을 얻어낸다. 필요한 컬럼은 테이블을 한번 더 읽는 대신, 정렬된 튜플에서 바로 읽어들인다.

수정된 filesort 알고리즘을 사용하면, 튜플의 크기가 원래 방식에 비해 커지므로 튜플을 정렬 버퍼(sort_buffer_size에 의해
결정되는)에 더 적게 넣게 된다. 이 결과, 추가적인 I/O 를 발생시킬 수 있고, 이로 인해 더 느려질 수 있다. 이를 방지하기 위해
정렬에 사용되는 튜플의 크기가 시스템
변수인[`max_length_for_sort_data`](http://dev.mysql.com/doc/refman/5.1/en/server-
system-variables.html#sysvar_max_length_for_sort_data)보다 크지 않은 경우에만 이 알고리즘이
사용된다. ( 이 값을 크게 하는 경우, 높은 디스크 이용율과 낮은 CPU 이용율을 겪게 된다. )

filesort가 사용되지 않는 느린 쿼리(slow query)에
대해서는[`max_length_for_sort_data`](http://dev.mysql.com/doc/refman/5.1/en
/server-system-variables.html#sysvar_max_length_for_sort_data)값을 낮춰, filesort가
일어나도록 조정할 수 있다.

ORDER BY 의 속도를 개선하기 위해서는 MySQL이 추가적인 정렬 없이 인덱스를 바로 사용하도록 해야하지만, 그러지 못할 경우에
대해서는 다음의 전략을 시도해볼 수 있다.

  * [`sort_buffer_size`](http://dev.mysql.com/doc/refman/5.1/en/server-system-variables.html#sysvar_sort_buffer_size)의 값을 높인다.

  * [`read_rnd_buffer_size`](http://dev.mysql.com/doc/refman/5.1/en/server-system-variables.html#sysvar_read_rnd_buffer_size)의 값을 높인다.

  * 저장해야 할 값의 최대 크기(길이)에 적합하게 설계해, 메모리를 덜 사용하도록 한다. 예를 들어, 값이 16글자를 넘지 않는 경우에 대해 CHAR(16)이 CHAR(200)보다 좋은 선택이다.

  * [`tmpdir`](http://dev.mysql.com/doc/refman/5.1/en/server-system-variables.html#sysvar_tmpdir)를 충분한 여유 공간을 가진 별도의 파일 시스템을 가리키도록 변경한다. 이 옵션에 여러 경로를 지정하는 경우에는 라운드-로빈 전략이 적용되어, 여러 디렉토리로 부하를 분산할 수 있게 된다. 경로는 유닉스에서는 콜론 문자(":")로 구문되며, 윈도우즈나 NetWare, OS/2 에서는 세미콜론(";")으로 구분된다. 각 경로는 같은 물리 디스크 내의 서로 다른 파티션이 아니라, 서로 다른 물리적 디스크에 존재해야만 한다. (역주: tmpdir을 통해 filesort가 수행되는데, 이 I/O 부하를 분산시키는데 같은 물리 디스크를 사용하는 것은 아무 의미가 없다.)

  

