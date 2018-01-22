Title: Oracle adding close source extensions to MySQL
Time: 02:12:00

  

원문 :Oracle adding close source extensions to MySQL / byMonty Widenius ( MySQL
founder )

출처 : [http://monty-says.blogspot.com/2011/09/oracle-adding-close-source-
extensions.html](http://monty-says.blogspot.com/2011/09/oracle-adding-close-
source-extensions.html)

번역 : 박현우( ez.amiryo@gmail.com / @lqez )

  

오역이나 오탈자 지적은 언제나 환영합니다.

  

번역에 도움 주신 분. 감사합니다.

  * 김종원([@2bura](http://twitter.com/#!/2bura))

  

**  
**

Oracle adding close source extensions to MySQL

오라클이 MySQL마저 반-오픈소스 진영으로 집어 삼키고 있다.

  

  

  

오라클은 공식적으로 MySQL은 더이상 완전한 프리(free) 소프트웨어 프로젝트가 아니며, 오픈 코어(Open Core) 모델을 지향할
것이라고 [발표했다](http://www.h-online.com/open/news/item/Oracle-adds-commercial-
extensions-to-MySQL-1344611.html).

  

이는 MySQL의 기존 사업 모델과는 판이하게 다르다. MySQL의 장점은 모든 소스코드가 항시 자유롭게(freely) 열려 있었다는
점이다. 이 덕에 MySQL이 널리 적용될 수 있었고, 수 많은 사용자들이 사용하는 계기가 되었다.

  

MySQL 의원회와 Sun도 이러한 사실을 이해하고 있다. MySQL 서버의 소스 코드를 닫는 것은 어느 경우에도 장기적 관점에서 좋은
선택은 아닐 것이다.

  
  

자유 소프트웨어에 대한 이해나 믿음이 없는 영리(commercial) 세계 출신의 사람들이 MySQL AB에 있었으며, 이들이 일부 소스만
열어두고, 나머지는 폐쇄적으로 하는 오픈 코어 모델에 대해 강하게 주장해왔던 것은 사실이다. 초기에는 MySQL 서버를 오픈 소스로 유지해야
한다는 창립자들의 주주 협약 때문에 이렇게 할 수 없었다. Sun이 MySQL을 인수하게 되면서, 주주 협약이 만료되었고, 그들은 이를
기회로 보고 백업 기능이 영리적 확장 모델(commercial closed source extensions)이 될 것이라고
[발표했다](http://monty-says.blogspot.com/2008/04/mysql-conference-good-bad-and-
ugly.html). 하지만 이 계획은 MySQL의 오픈 소스 프로젝트로써의 진정한 가치와, 닫힌 소스 모델이 가져오는 평가 절하 가능성에
대한 이해가 있는 Sun의 매니저에 의해 취소되었다.

  
MySQL AB가 오픈 코어 모델을 사업 모델로 원하지 않았던 이유 중 하나는, MySQL이 기반 기술(infrastructure)에
해당하는 제품이었기 때문이다. 기반 기술이기에 다른 제품에 포함될 수 있어, MySQL을 자사의 제품에 내장하되, 제품 자체는 오픈 소스가
아닌 경우에 라이센스를 팔 수 있었기 때문이다. (듀얼 라이센싱)

  
  
  
그렇다면, 오픈 코어 모델의 무엇이 문제인가?

  

사업 모델로써 - 특히 자기 자본으로 창업하는 경우 - 오픈 코어는 나쁘지 않은 생각이다. 이는 사용자들에게 비용을 지불하게 하여 개발을
돕게 하는 일종의 레버리지를 제공한다. 허나 결과적으로 더 적은 사용자를 얻고, 프로젝트가 덜 받아들여지게 된다. 수 많은 프로젝트들이
성장하면서 오픈 코어 모델을 포기하는데, 이는 오픈 소스가 더 많은 사용자를 확보할 수 있게 하며, 따라서 더 많은 가치를 주기 때문이다.

  

  

오픈 코어 프로젝트를 이해하는데 있어 가장 중요한 것은, 이것이 오픈 소스 프로젝트와는 아무 상관이 없다는 점이다. 만약 닫힌 소스로
이루어진 콤포넌트만 단 하나만 사용하더라도, 전체 프로젝트를 닫힌 소스 프로젝트로 간주하게 될 것이고, 이에 따라 오픈 소스로써의 모든
장점을 잃게 된다.

  * 특정 업체에 의존하게 된다.
  * 버그를 직접 수정할 수도 없고, 원 공급 업체 외에는 수정을 요청할 수도 없다.
  * 제품의 그 어떤 부분도 시험하거나 향상시킬수 없게 된다.
  * 오픈소스나 기타 상용 확장 기능들을 전혀 사용할 수 없다. 이는 제품의 내부와 관계된 확장 모듈 전체에 적용된다. (대부분의 MySQL 플러그인이 그러하다)
  * 원 공급 업체가 제공하는 플랫폼에서만 사용 가능해진다. (예를 들어 RedHat 6에서는 상용 버전의 신기능을 쓸 수 없는데, 이는 지원되는 플랫폼이 아니기 때문이다)
  * 빌드가 현재와 같이 많은 사용자에 의해 테스트되지 않는다. (더 많은 버그가 생길 것이다)
  * 보안 문제나 백도어 등에 대해 오픈 소스 커뮤니티로부터의 지원을 받을 수 없게 된다.
  * 새로운 기능들이 다른 오픈 소스 프로젝트들에 적용되지 않게 된다. (오히려 충돌이 나게 된다)
  * 업체의 일방적인 가격 결정에 의해 휘둘리게 된다.

재미있는 것은, 새로 추가된 상용 기능들은 오라클에 의해 개발되지 않았다는 점이다. 쓰레드풀(thread pool)은 원래 Ebay가
MySQL 5.0에서 개발하여 MySQL 5.1에 내장되도록 기여했지만, 5.1 버전에는 새로운 스케쥴러 인터페이스 코드만 추가되었을 뿐,
쓰레드풀은 MySQL 6.0에 겨우 - 그것도 우연히 더 느린 구현으로 - 추가되었다. 오라클은 쓰레드풀 코드를 MySQL 5.5 커뮤니티
버전(역주: 무료 버전)에 절대로 넣지 않았고, 심지어 현재는 MySQL 6.0 트리가 삭제되었다.

새로운 PAM 인증을 가능하게 하는 조합형(pluggable) 인증 모듈도 Monty Program Ab의 Segei Golubchik에
의해 오라클에 기여된 부분이다.

  
  
그나마 좋은 소식은, 향상된 쓰레드풀을 포함한 대부분의 중요한 기능이 이미 MariaDB에 구현되어 있다는 것이다. MariaDB는 5.1
이상 버전에 (MySQL 5.1보다 더 좋은) 쓰레드풀을 내장하였고, MySQL 엔터프라이즈 버전에 버금가는 속도의 새로운 구현을
[MariaDB 5.5](http://kb.askmonty.org/en/what-is-mariadb-55)를 위해 준비하고 있다.
MariaDB는 아직 PAM 인증 모듈이 없지만 누군가 그것을 필요로 하거나, 구현 코드를 기여해준다면 당장 개발할 수 있도록 준비되어
있다. 우리는 MySQL과 동일한 조립식 인증 프로토콜을 쓰고 있기 때문에 상대적으로 쉬운 일이 될 것이다.

  

[Steward Smith's thoughts](http://www.flamingspork.com/blog/2011/09/16/mysql-
no-longer-fully-open-source-database)와 블로그에 있는 댓글을 통해 이 프로젝트에 대한 정보를 확인할 수 있다.

  

  

  

