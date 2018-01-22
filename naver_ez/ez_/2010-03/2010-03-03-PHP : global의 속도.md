Title: PHP : global의 속도
Time: 12:21:00

게으르게 개발하기 위해서 global을 사용하고 있는데,

( 이전 포스트 참조 : [http://blog.naver.com/ez_/140100347594](../ez_/140100347594) )

  
php.net을 돌아다니다 global의 속도에 대한 포스팅을 보았다.

[http://kr2.php.net/manual/en/language.variables.scope.php#94259](http://kr2.p
hp.net/manual/en/language.variables.scope.php#94259)

  
자주 사용하는 읽기 전용 글로벌 변수를 매번 $GLOBALS['var']하거나 global $var; $var = ... 하는 것도
일이라서, var() 와 같이 만든 다음에 함수 내부에서 return $GLOBALS['var']해서 쓰고 있는데, 속도가 느리지 않을까
매번 의심만 하다가 이번에 측정해보았다.

  
첨부파일의 예제 php파일을 실행해보면 global scoping에 대한 속도를 알 수 있다.

(1) global $var 로 선언해서 쓰기

(2) $GLOBALS['val']의 superglobal 배열 사용하기

(3) global_var() 와 같이 함수로 만들어서 쓰기

  
예제 파일 실행 결과

(1) 0.0020589828491211

(2) 0.0017449855804443

(3) 0.011854887008667

  
결론

superglobal이 제일 빠르다. 자주 사용하는 경우라면 반드시 superglobal 배열을 쓸 것.

귀찮아서 함수로 만들어 쓰는 경우에는 너무 자주 호출해서 쓰지 말 것.

  
덧

사실 (3) 예제에서는 함수로 리턴된 값이 참조가 아닌 복제라, 어쩔 수 없이 global variable a 를 superglobal
배열에서 참조하고 있다. 이 부분을 제외하더라도 0.003초 이상으로 가장 느리다.

