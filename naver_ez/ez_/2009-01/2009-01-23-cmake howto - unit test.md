Title: cmake howto - unit test
Time: 03:36:00

지난 번의 cmake 소개에 이은, cmake를 통한 unit test.

회사동료인 haje01님께서 잘 가르쳐 주시는 덕분에 빨리 익힐 수 있었다.

( haje01님 블로그 : [http://blog.naver.com/haje01](http://blog.naver.com/haje01) )

  

일반적인 cmake 유닛 테스트 수행과정은 다음과 같다.

> AmiBook:build_make lqez$ make test

>

> Running tests...

>

> Start processing tests

>

> Test project /Users/lqez/Documents/npluto/minidom/build_make

>

> 1/ 3 Testing load Passed

>

> 2/ 3 Testing get Passed

>

> 3/ 3 Testing query Passed

>

>

>

> 100% tests passed, 0 tests failed out of 3

>

> AmiBook:build_make lqez$

make 한 이후에 make test를 통해 testing build target을 수행할 수 있다.

이를 위한 CMakelists.txt는 좀 복잡한데, 보통은 다음과 같다.

> **루트의 CMakelists.txt**

>

> ...

>

> enable_testing()

>

> add_subdirectory( tests )

> **tests 디렉토리의 CMakelists.txt**

>

> ...

>

> create_test_sourcelist( TESTS

>

> tests.cpp

>

> load.cpp

>

> get.cpp

>

> query.cpp

>

> )

>

>

>

> add_executable( tests ${TESTS} )

>

> target_link_libraries( tests minidom )

>

>

>

> remove( TESTS tests.cpp )

>

>

>

> foreach( test ${TESTS} )

>

> get_filename_component( TName ${test} NAME_WE )

>

> add_test( ${TName} tests ${TName} )

>

> endforeach( test )

  1. 루트 CMakelists.txt에서 enable_testing()을 통해 유닛 테스트 수행을 선언한다.

  2. tests와 같은 유닛 테스트용 디렉토리를 작성한다. 이 때 이름을 test로 하면 충돌 가능성이 있다.

  3. create_test_sourcelist를 통해 유닛 테스트 파일을 등록한다. 첫번째 인자는 SET이름, 다음은 tests.cpp인데, 이 파일은 자동 생성된다. 그 이후에 직접 작성한 유닛 테스트 파일을 등록하면 된다. 유의할 점은, 유닛 테스트용 파일 각각은 main이 없는 대신, main과 같은 형태의 [확장자를 제외한 파일 이름]의 함수를 가지고 있어야 한다. 즉, query.cpp는 int query( argc, argv ) 함수를 반드시 가지고 있어야 한다.

  4. tests.cpp는 유닛 테스트 파일이 아니므로 remove명령을 통해 TESTS로부터 삭제한다.

  5. iteration을 통해 유닛 테스트를 추가한다.

위의 방법이 꼭 정답은 아니고, 다양한 방법이 있을 듯 하다. ( cmake는 문법이 유별나게 지저분하기에 더욱 다양한 방법이 나올 것
같다. )

  

모든 테스트가 Passed 되면 재미가 없으므로, 한 유닛 테스트에서 일부러 에러를 발생시켜 그 결과를 보면,

> AmiBook:build_make lqez$ make test

>

> Running tests...

>

> Start processing tests

>

> Test project /Users/lqez/Documents/npluto/minidom/build_make

>

> 1/ 3 Testing load Passed

>

> 2/ 3 Testing get Passed

>

> 3/ 3 Testing query ***Exception: Other

>

>

>

> 67% tests passed, 1 tests failed out of 3

>

>

>

> The following tests FAILED:

>

> 3 - query (OTHER_FAULT)

>

> Errors while running CTest

>

> make: *** [test] Error 8

>

> AmiBook:build_make lqez$

위와 같이 Exception을 표시해준다. c++의 에러 핸들러에서 제공하는 내용 정도를 대충 보여주는 듯 한데, assert와 같이 파일
이름과 에러 라인 번호가 나오지 않아 아쉽다. 그래서 make test에서 통과 못한 테스트가 있을 때, 해당 테스트를 tests.cpp를
거치지 않고 바로 수행하여 해당 에러를 보거나 디버깅 할 수 있는 환경을 자동으로 추가하도록 만들어 보았다. 위의
CMakelists.txt를 조금만 수정하면 된다.

> **수정된 tests/CMakelists.txt - 추가된 부분은 굵게 표시**

>

> ...

>

> **set_target_properties( tests**

>

> ** PROPERTIES**

>

> ** COMPILE_DEFINITIONS __UNITTEST__**

>

> ** )**

>

>

>

> foreach( test ${TESTS} )

>

> get_filename_component( TName ${test} NAME_WE )

>

> add_test( ${TName} tests ${TName} )

>

> ** add_executable( ${TName} ${test} )**

>

> ** target_link_libraries( ${TName} minidom )**

>

> endforeach( test )

add_executable를 통해 유닛 테스트 파일들을 각각의 실행 파일로 만들어 주었는데, 문제는 각 유닛 테스트 파일에는 main이 없는
것이다. 이를 위해서 매크로를 도입해, __UNITTEST__가 있는 경우에는 int query(argc, argv)와 같은 형태로, 없는
경우에는 일반적인 int main(argc, argv) 형태를 가지도록 하였다. 이를 위한 매크로는 아래와 같다. ( 유의할 것은
set_target_properties 이전에 build target이 등록되어 있어야 한다. )

> #ifdef __UNITTEST__

>

> #define UNITTEST_MAIN( X ) \

>

> int (X)( int argc, char * argv [] )

>

> #else

>

> #define UNITTEST_MAIN( X ) \

>

> int main( int argc, char * argv [] )

>

> #endif

위의 매크로를 통해 각 유닛 테스트 내 함수를 UNITTEST_MAIN(query)와 같이 선언하면, 테스트용 함수와 실행 파일용 함수를
동시에 지원할 수 있게 된다. 아무튼 이런 귀찮은 과정을 거쳐 만들어진 문제가 있는 유닛 테스트 실행 파일을 실행해보면 다음과 같다.

> AmiBook:tests lqez$ ./query

>

> Assertion failed: (s.size() == 5), function main, file
/Users/lqez/Documents/npluto/minidom/tests/query.cpp, line 14.

>

> Abort trap

>

> AmiBook:tests lqez$

아직은 cmake 초보 단계지만, 활용처가 너무 다양한 프로그램이라 잘 사용하면 빌드 프로세스 개선에 큰 도움을 줄 솔루션임이 분명하다.

  

**추가> 위의 __UNITTEST__ 방법은 일반적인 상황에서는 필요가 없다. test 빌드를 통해 생성된 tests 실행파일을 그냥 실행하면 다음과 같은 메뉴가 나오고 각각의 유닛 테스트를 바로 실행해볼 수 있다.**

> lqezs-computer:tests lqez$ ./tests

>

> Available tests:

>

> 0. load

>

> 1. get

>

> 2. query

>

> To run a test, enter the test number: 2

>

> book = (/bookstore/book) [ style="autobiography" ]

>

> book = (/bookstore/book) [ style="textbook" ]

>

> book = (/bookstore/book) [ style="novel" id="myfave" ]

>

> book = (/bookstore/book) [ style="leather" price="29.50" ]

>

> lqezs-computer:tests lqez$

