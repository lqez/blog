Title: MySQL : MySQL은 메모리를 어떻게 사용할까? (번역)
Time: 21:27:00

### 번역 : 박현우(ez.amiryo@gmail.com /[@lqez](http://twitter.com/lqez))

출처 :[http://dev.mysql.com/doc/refman/5.5/en/memory-
use.html](http://dev.mysql.com/doc/refman/5.5/en/memory-use.html)

원제 : How MySQL Uses Memory

  

### 7.11.4.1 MySQL은 메모리를 어떻게 사용할까?

다음은 mysqld 서버가 메모리를 사용하는 방법에 대한 목록이다. 적용되는 곳에 해당하는 메모리와 관련된 시스템 변수의 이름을 적어두었다.

  * 모든 쓰레드는[`MyISAM`](http://dev.mysql.com/doc/refman/5.5/en/myisam-storage-engine.html)키 버퍼를 공유한다. 이 크기는`[key_buffer_size](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_key_buffer_size)`변수에 의해 결정된다. 서버에서 사용되는 나머지 버퍼들은 필요한 경우에 할당된다.[Section7.11.2, “Tuning Server Parameters”](http://dev.mysql.com/doc/refman/5.5/en/server-parameters.html)를 참고.

  

  * 클라이언트 접속에 사용되는 각 쓰레드는 쓰레드 전용의 공간을 사용한다. 다음은 이에 해당되는 내용과 그 크기를 조절하기 위한 변수의 목록이다.

    * 스택 ([`thread_stack`](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_thread_stack)변수)

    * 연결 버퍼 ([`net_buffer_length`](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_net_buffer_length)변수)

    * 결과값 버퍼 ([`net_buffer_length`](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_net_buffer_length)변수)

연결 버퍼와 결과값 버퍼는 각각`[net_buffer_length](http://dev.mysql.com/doc/refman/5.5/en
/server-system-variables.html#sysvar_net_buffer_length)`바이트로 시작하지만, 필요한 경우
동적으로`[max_allowed_packet](http://dev.mysql.com/doc/refman/5.5/en/server-
system-variables.html#sysvar_max_allowed_packet)`바이트까지 커질 수 있다.결과값 버퍼는 각각의 SQL
명령이 실행된 이후에 다시`[net_buffer_length](http://dev.mysql.com/doc/refman/5.5/en
/server-system-variables.html#sysvar_net_buffer_length)`바이트로 줄어든다. 명령이 실행되고 있는
동안은 해당 명령문의 사본도 할당된다.

  * 모든 쓰레드는 동일한 기본(베이스) 메모리를 공유한다.

  * 쓰레드가 더 이상 필요하지 않으면, 이에 할당된 메모리는 해제되어 시스템으로 반환된다. 단, 쓰레드 캐시로 돌아가는 쓰레드의 메모리는 할당된 상태를 유지한다.

  * 시스템 변수[`myisam_use_mmap`](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_myisam_use_mmap)을 1로 설정하면 모든MyISAM테이블의 메모리-맵핑 기능을 활성화 한다.

  * 테이블을 순차적으로 스캔하는 각각의 요청은_read buffer_(`[read_buffer_size](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_read_buffer_size)`변수) 를 할당한다.

  * 정렬과 같이 임의의 순서로 열을 읽는 경우, _random-read buffer_([`read_rnd_buffer_size`](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_read_rnd_buffer_size)변수)가 디스크 검색을 줄이기 위해 할당될 수도 있다.

  * 모든 조인은 단일 작업(패스)내에서 이루어지며, 대부분 임시 테이블 없이 수행 가능하다. 임시 테이블은 대부분 메모리 기반의 해시 테이블이며, BLOB 컬럼을 가지고 있거나 한 열의 길이(컬럼 길이의 합)가 매우 긴 경우에만 디스크에 보관된다.

메모리에 있던 임시 테이블이 커지면(역주:tmp_table_size 변수의 값보다 커질 경우), MySQL은 이 테이블을
`MyISAM`엔진을 사용하는 디스크 기반의 테이블로 변환한다.필요한 경우, 임시 테이블 크기를[Section7.4.3.3, “How
MySQL Uses Internal Temporary Tables”](http://dev.mysql.com/doc/refman/5.5/en
/internal-temporary-tables.html)에 따라 증가시킬 수 있다.

  * 정렬은 대게 정렬 버퍼를 할당하고, 정렬 결과의 크기에 따라 0~2개의 임시 파일을 사용하게 된다. 이와 관련하여[SectionC.5.4.4, “Where MySQL Stores Temporary Files”](http://dev.mysql.com/doc/refman/5.5/en/temporary-files.html)를 참고한다.

  * 대부분의 파싱과 계산은 쓰레드 로컬 변수와 재사용 가능한 메모리 풀을 통해 수행된다. 작은 아이템들에 대해서는 메모리 오버헤드가 발생하지 않는 덕에, 느린 메모리 할당과 해제가 일어나지 않고, 예상치 못한 큰 문자열에 대해서만 메모리를 할당한다.

  * `MyISAM`테이블을 열 때, 인덱스 파일은 한 번만 열리지만 데이터 파일은 동작중인 쓰레드 별로 열리게 된다. 동작중인 쓰레드는 테이블 구조, 컬럼별 구조 그리고`3 *__``N`크기만큼 메모리를 할당한다.(_`N`_은 BLOB 컬럼을 제외한 나머지 컬럼들 크기의 합)[`BLOB`](http://dev.mysql.com/doc/refman/5.5/en/blob.html)컬럼은 데이터의 길이보다 5-8바이트 정도를 더 필요로 한다.`MyISAM`엔진은 내부 용도로 한 열에 크기에 해당하는 버퍼를 더 유지한다.

  * [`BLOB`](http://dev.mysql.com/doc/refman/5.5/en/blob.html)컬럼을 가진 각각의 테이블들은, 큰[`BLOB`](http://dev.mysql.com/doc/refman/5.5/en/blob.html)값을 읽기 위해 동적으로 버퍼를 확장한다.테이블 전체를 스캔한다면, 가장 큰[`BLOB`](http://dev.mysql.com/doc/refman/5.5/en/blob.html)값의 크기만큼 버퍼를 할당하게 된다.

  * 모든 사용중인 테이블에 대한 핸들러 구조체는 캐시에 저장되고, FIFO로 관리된다. 초기 캐시의 크기는[`table_open_cache`](http://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_table_open_cache)변수의 값으로 시작한다. 두 개의 동작중인 쓰레드가 하나의 테이블을 동시에 사용되고 있으면, 캐시는 해당 테이블에 대한 두 개의 엔트리(역주:핸들러 구조체)를 보관한다.[Section7.4.3.1, “How MySQL Opens and Closes Tables”](http://dev.mysql.com/doc/refman/5.5/en/table-cache.html)를 참고.

  * [`FLUSH TABLES`](http://dev.mysql.com/doc/refman/5.5/en/flush.html)또는[**mysqladmin flush-tables**](http://dev.mysql.com/doc/refman/5.5/en/mysqladmin.html)명령을 통해 사용하지 않는 모든 테이블을 모두 닫고, 사용중인 테이블에 대해서는 현재 쓰레드의 작업이 종료되면 바로 닫도록 표시할 수 있다. 이를 통해 사용중인 메모리를 효율적으로 해제할 수 있다.[`FLUSH TABLES`](http://dev.mysql.com/doc/refman/5.5/en/flush.html)명령은 모든 테이블이 닫힐 때까지 종료되지 않는다.

  * [`GRANT`](http://dev.mysql.com/doc/refman/5.5/en/grant.html),[`CREATE USER`](http://dev.mysql.com/doc/refman/5.5/en/create-user.html),[`CREATE SERVER`](http://dev.mysql.com/doc/refman/5.5/en/create-server.html),[`INSTALL PLUGIN`](http://dev.mysql.com/doc/refman/5.5/en/install-plugin.html)명령의 수행 결과에 대한 정보를 메모리에 캐시한다. 이 메모리는 [`REVOKE`](http://dev.mysql.com/doc/refman/5.5/en/revoke.html),[`DROP USER`](http://dev.mysql.com/doc/refman/5.5/en/drop-user.html),[`DROP SERVER`](http://dev.mysql.com/doc/refman/5.5/en/drop-server.html), [`UNINSTALL PLUGIN`](http://dev.mysql.com/doc/refman/5.5/en/uninstall-plugin.html)등의 명령으로 해제되지 않으며, 따라서 (캐시를 발생시키는) 이러한 명령어를 많이 수행하게 되면, 메모리 사용량이 늘어날 수 있다. 이 캐시된 메모리들은 [`FLUSH PRIVILEGES`](http://dev.mysql.com/doc/refman/5.5/en/flush.html)로 해제할 수 있다.

**ps**와 같은 시스템 상태를 보는 프로그램들에서[**mysqld**](http://dev.mysql.com/doc/refman/5.5/en/mysqld.html)가 많은 메모리를 사용하고 있다고 보고할 수 있는데, 이는 쓰레드 스택이 서로 다른 메모리 영역에 있기 때문이다. 예를 들어, 솔라리스의**ps**는 스택간의 사용하지 않는 메모리를 사용된 메모리로 계산한다. 이를 확인하기 위해, 남아있는 스왑(swap) 영역을 `swap -s`명령어를 통해 확인할 수 있다. 여러 상용 / 오픈소스의 메모리 누수 검사기를 통해[**mysqld**](http://dev.mysql.com/doc/refman/5.5/en/mysqld.html)를 확인했고, 따라서 메모리 누수는 없어야 한다.

  

----

번역에 도움 주신 분(가나다순). 감사합니다.

  * 이희승 [@trustin_ko](http://twitter.com/trustin_ko)
  * 임중근[@junggun_lim](http://twitter.com/junggun_lim)
  * 정재필[@JaepilJeong](http://twitter.com/JaepilJeong)

