Title: cmake - remove library prefix
Time: 09:52:00

바로 이전 포스트에서 cmake의 linux/windows에서의 라이브러리 생성시 네이밍 방식이 다른 것에 대한 글을 썼었는데, 완전한 것이
아닐 뿐더러, 더 좋은 방법을 찾아내어 다시 적어본다.

  

시나리오는 다음과 같다.

(1) xxx라는 라이브러리를 만들었다.

(2) xxx라는 라이브러리를 사용하는 xxx라는 실행 가능한 프로그램을 만들려고 한다.

(3) 이름이 xxx로 같아 문제.

(4) 라이브러리 이름을 libxxx로 바꾸어 문제 해결, 인줄 알았지만, linux나 mac build에서는 라이브러리 이름이
liblibxxx로 바뀌는 것이 문제.

  

이는 cmake가 linux/mac 빌드시, 라이브러리 이름에 lib이라는 prefix를 implicit하게 붙여서 발생하는 문제이다.

이를 해결하기 위해 CMAKE_STATIC_LIBRARY_PREFIX와 CMAKE_SHARED_LIBRARY_PREFIX를 제거해주면 된다.
이 값들은 linux/mac 빌드시에만 적용되는 값으로 기본값이 'lib'이다.

  

> set( CMAKE_STATIC_LIBRARY_PREFIX "" )

>

> set( CMAKE_SHARED_LIBRARY_PREFIX "" )

  

  

