Title: EOT : Embedded OpenType
Time: 02:49:00

EOT에 대한 정보를 찾다 OFLB에 관련 아티클이 있어 번역해보았다. 새벽 3시가 다 되어가네...

( 당연히 있을 오역에 대한 지적이나, 좀 더 나은 번역이 있다면 댓글로 남겨주시길. )

  

원문링크 :[http://openfontlibrary.org/wiki/Embedded_OpenType](http://openfontlibra
ry.org/wiki/Embedded_OpenType)

  

  

  

**요약**

  

Embedded OpenType(이하 EOT)는웹 폰트([@font-
face](http://openfontlibrary.org/wiki/Font_linking))을 위한 폰트 포맷이다. 현재는
마이크로소프트사의 웹 브라우저인 인터넷 익스플로러에서만 적용되며, OpenType이나 TrueType 폰트를 .eot 파일로 변환하는
프로그램도 오직 마이크로소프트 윈도우즈 운영체제를 사용하는 PC에서만 작동된다.

  

EOT의 첫번째 목적은 해당 폰트가 어떤 웹 사이트(페이지) 내에서만 사용될 수 있는지에 대한 추가 정보를 주는 것이다. 두번째 목적은
네트워크 사용량을 절약할 수 있는 더 작은 폰트를 만드는데 있다. 파일 크기는 일단 특정 문자의 형태(글리프)를 생략함으로써 줄일 수 있고,
남은 글자들은 특허 등록된 Monotype 기술로 압축할 수 있다. 이 압축과정은 암호화 과정도 포함한다.

  

본래 EOT는 극비 기술로, 세부 구현내용은 기업 비밀에 속했다. 암호화 기술로 보호된 EOT 파일로부터 원래의 글리프를 추출하는 것은 매우
어려운 일이었다. 그러나 2008년 초에 기술 명세서가[World Wide Web Consortium
(W3C)](http://www.w3.org/)에모든 웹 브라우저의 표준 기술로 적용될 수 있도록 제출되었다. 이 명세서는 암호화 과정의
모든 세부 사항을 포함하고 있어, (암호화 기술)자체로써의 가치는 없게 되었지만, 이를 통해 EOT 파일을 쉽게 해독하여, 일반 데스크탑
폰트로 되돌릴 수 있게 되었다.

  

  

  

**역사**

  

웹 페이지는 원래 꾸밈이 없는 단순한 텍스트 파일과 같은 간단한 문서로 취급되었다. 그러나 곧, 사용자들은 이미지와 텍스트 꾸밈을 원하게
되었고, 몇 년 사이에 크게 발전된 월드 와이드 웹은, 전문 디자이너들에게 상업용 웹 페이지 제작을 의뢰할 정도가 되었다.

  

그래픽 디자이너들은 우선 문서의 정보를 전달하는 "문자열"을 달리 보이게 할 수 있기를 기대했다. 글씨의 크기와 굵기는 해당 문자열의
중요성을 나타내고, 서체는 문자의 성격을 부여하는 속성이 되기 때문이다.

  

웹 페이지를 만들기 시작한 그래픽 디자이너 - 다시 말하면, "초기" 웹 디자이너 - 들은 금새 글씨의 크기를 지정할 수 있게 되었다.
하지만 폰트를 지정할 때에는 사용자 컴퓨터에 의존적이 되어, 사용자의 컴퓨터에 지정한 서체가 없다면 포기하고 임의의 폰트를 사용하게
된다.이미지 파일과는 다르게, 웹을 통해 폰트 파일을 전달할 방법이 없었기에, 디자이너가 의도한 대로 페이지를 보여주기 위해 임시로 폰트가
사용될 수도 없었다.

  

요즘엔 웹 디자이너들이 폰트를 직접 사용하지 않고, 이미지로 폰트를 대신하는 많은 방식들 때문에 분노하고 있는 것을 볼 수 있다. 현대적인
사이트들은 '이미지로 대체하기' 기술을 통해 텍스트를 숨기고, 디자인에 맞는 서체의 이미지로 (사용자의 컴퓨터에 해당 서체가 없으니 이미지를
사용함) 교체하는 방식을 사용하는데, 좋은 기술이라 하긴 어렵다.

  

1990년대의 '브라우저 전쟁'의 주인공인 넷스케이프와 마이크로소프트에서 이 문제에 대한 해결책을 내놓았다. 그 와중에, 그들은 기술적인
어려움이 아닌, 그들의 해결책을 성공적으로 채택시키는 것에 대한 위협에 직면했다.

  

이슈는 독점 폰트 소프트웨어 배포사들의 지위를 유지시켜주는데 있었다. 당시엔 정말 몇 안되는 자유 라이센스의 폰트들만 있었고, 폰트는
일반적으로 개인 사용자가 개인 소유의 컴퓨터에서 사용하기 위해 라이센스 되었으며, 당연히 타인에게 배포하기 위한 용도는 아니었다. 서체
디자이너들은 브라우저가 웹을 통해 폰트 파일을 전달하는 것이 허용하면, 라이센스와 관련 없는 폰트가 널리 퍼지게 되는 것을 우려했다. 웹
서핑을 하는 사람이라면 누구나 온라인일 때, 항상 그렇게 할 것이기 때문이다.

  

넷스케이프는 주류에서 벗어났고, 마이크로소프트의 EOT 솔루션은 오직 IE(Internet Explorer)에서만 동작했기 때문에, 관심을
두는 사람의 거의 없었다. 따라서 폰트 배포사들도 그런 옵션에 대해서는 염두에 두지 않았다. 2008년에 마이크로소프트가 EOT를 모든 웹
브라우저에서 지원하도록 W3C에 제안했을 때, 비로소 많은 이들이 관심을 가지게 되었다.

  

  

  

  

**그럼, EOT는 뭐가 잘못된 것인가?**

  

  * 위에서도 얘기했지만, EOT파일을 생성하는데 필요한[encryption](http://www.w3.org/Submission/2008/SUBM-EOT-20080305/#Processing)(암호화)와[compression](http://www.w3.org/Submission/MTX/)(압축)에 관련된 세부 내역은 모두 공개되었다. 따라서, 부도덕한 개발자가 금새 시스템을 무력화 시키고, 브라우저 외부에서 EOT 파일을 해독해내는 프로그램을 만들 수 있다.
  * 이는 '더 큰 문제를 만들어 내는 해결책' 이다. EOT가 뭘 하던간에, 폰트 소프트웨어 배포사들이 손해를 볼 수 있다는 것에 대한 답은 되지 못한다. 폰트 소프트웨어 라이센스의 조건은 이미 깨기가 쉽고, 친구에게 사본을 주기도 쉽다. 부정직한 사람들은 데스크탑 폰트를 웹에도 거리낌 없이 쓸 것이며, 정직한 사람들은 그렇지 않을 것이다. ( 정직한 사용자를 정직하게 만드는 것은 불필요하다 ) EOT는 폰트 배포사와 서체 디자이너들에게 불법 복제에 대한 해결책이 존재 한다고 믿게 만들어 안심시켜, 현실과는 거리가 먼 것들에 대한 이해를 강요한다.
  * 그것은[Digital Rights Management](http://en.wikipedia.org/wiki/Digital_rights_management)(DRM)의 일종이다. 즉, 조항을 이해하고 존중하는 사용자에 의존하기보다는 소프트웨어를 통해 라이센스 조항을 강제하려고 한다. W3C는 이러한 것을 예전부터 절대 권장하지 않았고, 다른 브라우저 제작자들도 이런 것이 자리잡는 것을 보고 싶어하지 않는 선례가 될 것으로 보인다.(역주:해석이 불분명합니다. 원문을 참고하세요:it appears to be a precedent that some browser developers do not wish to see established. )
  * 압축 시스템([compression system](http://www.w3.org/Submission/MTX/))은 Monotype사의 특허이고, 그들은 이 특허를 오직 웹 브라우저들에서만 사용되도록 허용했다. Webkit과 Gecko (애플 사파리와 모질라 파이어폭스는 이를 기반으로 작성되어 있다) 프로그램은 GNU LGPL하에 있고, 이는 그들이 사용처를 제한하지 못한다는 것을 암시함을 의미한다.
  * 일부 기능은 아마 불필요할 것이다. 큰 폰트를 압축하는 것이 중요했던 10여년 전과 달리, 요즘 사람들은 빠른 인터넷 접속 환경을 가지고 있다. 모바일 폰의 인터넷 접속 속도는 대체로 1990년대 후반의 56k모뎀보다 빠르다. 대부분의 라틴 폰트들의 용량은 JPEG 이미지 파일 한 장 정도에 불과해, 높은 압축률이 굳이 필요하지 않다. 게다가 gzip 압축은 이미 웹 서버와 브라우저들에 내장되어 있고, 잘 동작한다. 만약 (과거와 같이) 폰트의 일부(subset)만 제공된다면, 위키, 블로그나 뉴스 사이트와 같은 동적인 컨텐츠를 제대로 표현할 수 없을 것이다. (내용이 갱신될 때, 일부 글자가 표시되지 않을지도 모른다!)
  * 열렬한 지지자가 없다. 최근 한 논평가는 마이크로소프트사가 강한 의지도 없이 EOT를 세상(시장)에 떠넘기고 있다고 주장했다. 이는 브라우저 제작자나 웹 디자이너들에게 업무의 복잡도만 증가시켜, 별 이득도 되지 않는 일에 고된 시간을 보내도록 한다.
  * 현재로썬, 폰트를 EOT파일로 변환하는 소프트웨어를 구동하기 위해 윈도우즈 OS가 필요하다. 게다가, 잘 동작하지도 않는다!([That software doesn’t work very well.](http://jontangerine.com/log/2008/10/font-face-in-ie-making-web-fonts-work))

  

Open Font Library는 typefaces(폰트)를 공유하고 사용하고자 하는 커뮤니티를 독려하는 것이 목적으로 한다. 이는
라이센스에 대한 진정한 존중이 수반되어야 가능한 일이다. 사람들이 라이센스를 무시하기로 마음 먹으면, 라이센스를 적용하는 것은 불가능하다.
이 원칙은 라이센스가 모두에게 이득이 되는 쪽이거나 일부 사용자에게만 사용을 허가하는 경우에도 적용된다.

  

EOT는 사실상 라이센스를 '강제 시스템'으로 대체 하기 때문에, 소프트웨어 라이센스 기반을 약화시킬 뿐 아니라, 라이센스의 중요성에 대한
인식을 사용자들에게 심어주지도 못한다.EOT가 의미있는 이유는 불법적인 폰트 소프트웨어의 사용으로부터의 보호인데, 암호화를 우회할 수 있는
간단한 방법이 공개되어 '강제 시스템'이 무력화 된다면, 이를 지지하는 사용자들은 얼간이 처럼 보이게 될 것이다.

  

  

**미래에는 어떻게 될까?**

  

W3C가 EOT 또는 EOT와 같은 무언가를 웹 표준으로 승인하는데 까지 오랜 시간이 걸릴 것이다. 하지만[font
linking](http://openfontlibrary.org/wiki/Font_linking)을 일반적인 폰트 꾸밈을 위해 사용하는
행위는 매우 빨리 퍼지고 있다.

'the big guys'들과는 달리, 자신만의 폰트를 만들어내는 많은 폰트 디자이너들은 정직한 사용자들이 많다는 것을 알고 있고, 컴퓨터가
정직한 사용자들을 정직하도록 유지할 - 그릇된 아이디어에 기반한 - "성가신" 새 폰트 규격이 나오는 것을 기다리지 않을 것이다. 그들은
당장 웹 폰트를 통해 돈을 벌길 원할 것이고, 웹 페이지에 링크하기 위해서 라이센스가 필요한 - 이미 동작하는 규격에 맞춰 폰트를 출시할
것이다. 그렇지 않으면, 엄청난 판매 기회를 놓치게 되니까!

  

대형 폰트 퍼블리셔가 몇몇의 폰트 디자이너가 큰 돈을 벌며 주도하고 있다는 것을 보게 된다면, 관문은 열릴 것이다.

사용자들은 대중적인 웹 브라우저들에서 웹 폰트가 지원되기를 기대할 것이다.
