Title: live schema 소개
Time: 04:09:00

DDD - Data Driven Development

  

아마 그 옛날 코볼이 DDD가 아니었을까 싶은데, 이 개념은 요새 Web framework들에서 많이 사용하고 있다. Data
modeling(DM)이후의 귀찮은 CRUD는 프레임웍에 맡기고, 뷰는 템플릿과 CSS에 넘긴 다음에, 로직(컨트롤러)만 작성하는 식.

  

고전적인 C 언어나 나름 최신(?)의 Objective-C 2.0이나 위와 같은 프레임웍에 의존하지 않는 이상, 데이터를 선언하고 그 값을
serialize하고 un-serialize 하는 기능을 안 만드는 경우는 없다. 이 작업은 항상 단순 반복 작업이 되어 귀찮게 되는데,
그만큼 실수하지 않고 정확하게 짜는데 스트레스를 받는다. 한창 UML이나 Use-case 같은 얘기가 돌 때, DM을 GUI로 그리고, 그
결과물을 target-language source로 port해주는 기능을 가진 프로그램이 많았는데, 이 기능을 아주 유연하고 깔끔하게
구현해낸 프로젝트가 바로 live schema 이다.

  

live schema -http://code.google.com/p/liveschema/

  

동료인 haje01님께서 만들고 있는데, XML base에 XSLT를 통한 port라는 단순 명료한 방법을 택하고 있다. 이 프로젝트의
목적은 live schema 문법에 맞게 DM을 수행하면, target-language에 해당하는 XSLT를 통해 모델(클래스)을 정의하고
읽고 쓰는 메소드를 작성해주는데 있다. 게다가 읽고 쓰기가 Binary/Text(XML) 듀얼 모드로 지원된다. ( 아직은 바이너리만 되는
듯 )

  

C++ port 완성이 목전인데, 개인적으로는 매우 기대가 되는 프로젝트다. 추가로 HTML로 DM description을 보여주는 기능도
간략하게 보았는데, live schema를 작성하는 툴이 추가 된다면 기획자/매니저가 데이터에 가까워지는데 꽤 도움이 될 것 같다. 모든
사람에게 oxygen이나 xmlspy를 쓰게할 수는 없으니.

  

동문서답/용두사미식 결론 : 관건은 역시 GUI인가?...

  

  

  

