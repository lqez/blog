Title: Mac OS X : mac port
Time: 11:59:00

보통 오픈소스계(라고 불릴 수 있는 계가 존재한다면)에서는 애플리케이션/라이브러리를 설치하는 방법이 크게 두가지가 있다.

  

첫번째는 바이너리 설치.

해당 플랫폼에 얼추 맞게끔 빌드된 바이너리를 다운받아 복사하는 것으로 설치가 완료된다.

레드햇 계열의 rpm이나 데비안(우분투)계열의 apt가 그런 역할을 수행한다.

  

두번째는 소스 설치.

gcc를 비롯한 GNU 툴체인을 확보하고, 이후에 소스를 다운받아 해당 컴퓨터에 맞게 빌드를 수행, 설치를 완료한다.

해당 컴퓨터의 CPU가 가지고 있는 확장 명령어들을 컴파일러가 지원하거나 소스에 그에 걸맞는 코드가 포함되어 있으면 가장 최적화된 형태로
설치할 수 있는 것이 장점이나, 설치하는데 시간이 오래 걸린다.

젠투의 emerge나 FreeBSD의 port, 그리고 Mac OS X로 이식된 mac port 등이 이런 일을 담당한다.

  

올해는 리눅스를 외면하고 당분간 맥돌이 하기로 했으니 오늘은 mac port에 대한 소개글을 적어본다.

  

![](Screen_shot_2010-09-01_at_3.40.57_PM.png)

mac port는 TCL 스크립트와 실제 소스로 구성된 패키지(포트)를 통해, 컴파일/설치/관리/삭제 작업을 편리하게 할 수 있도록 도와주는
프로그램이다. 패키지간 의존성에 대한 정보가 포함되어 있어, 원하는 패키지를 설치하는데 필요한 의존 패키지들을 알아서 설치해준다.

[http://www.macports.org/](http://www.macports.org/)

위의 주소에서 받을 수 있으며, dmg 혹은 압축파일, 소스 등을 받아 설치할 수 있다.

Tiger에서 Snow leopard 까지는 dmg가 준비되어 있으니 해당 dmg를 받아 설치하는 것이 간편.

  

[http://guide.macports.org/](http://guide.macports.org/)

위 링크를 통해 RTFM 하는 것이 좋겠지만, 한국어로 이 글을 쓰는 이유 자체가 이런 매뉴얼을 읽지 않는 사람들을 위한 것이니 간략한
사용법을 적어본다.

  

(참고) 소개에서도 얘기했지만, 바이너리가 아닌 소스를 받아 직접 빌드하므로, 툴체인이 미리 설치되어 있어야 한다.

XCode를 설치했다면 이미 툴체인이 모두 설치된 상태이므로 그대로 진행, 아니라면 아래 링크의 설명을 통해 툴체인을 설치한다.

[http://guide.macports.org/#installing](http://guide.macports.org/#installing)

  

  

  

**> port list**

포트에서 제공하는 패키지 목록을 보여준다. 너무 많으니 이 명령어 대신 search를 사용한다.

  

**> port search [이름]**

특정 이름이 포함된 패키지 목록을 보여준다. 정확한 이름이 생각나지 않을 때, 이를 통해 검색 가능하다. 아래는 mysql을 검색한 결과.

> lqez-mbp:/ lqez$ port search mysql5

>

> mysql5 @5.1.49 (databases)

>

> Multithreaded SQL database server

>

>

>

> mysql5-devel @5.5.2-m2 (databases)

>

> Multithreaded SQL database server

>

>

>

> mysql5-server @5.1.49 (databases)

>

> Multithreaded SQL database server

>

>

>

> mysql5-server-devel @5.5.2-m2 (databases)

>

> Multithreaded SQL database server

>

>

>

> Found 4 ports.

**> port info [패키지명]**

패키지의 세부 정보를 보여준다. 의존성 여부와 제공자 등을 확인할 수 있다.

> lqez-mbp:/ lqez$ port info mysql5

>

> mysql5 @5.1.49 (databases)

>

> Variants: universal

>

>

>

> Description: MySQL is an open-source, multi-threaded SQL database with a
command syntax very similar to mSQL.

>

> Homepage: [http://www.mysql.com/](http://www.mysql.com/)

>

>

>

> Library Dependencies: zlib, openssl, readline

>

> Conflicts with: mysql5-devel, mysql4

>

> Platforms: darwin

>

> License: GPLv2

>

> Maintainers: ryandesign@macports.org

**> port install [패키지명]**

패키지를 설치한다. 의존성이 있는 경우, 해당 패키지들을 추가로 설치한다.

바이너리를 받아 설치하는 것이 아니므로, 파일을 전송받는데는 시간이 적게 걸리는 반면, 빌드하는데 시간이 오래 걸리는 편이다.

  

**> port uninstall [패키지명]**

해당 패키지를 삭제한다. 단, 다른 패키지가 해당 패키지에 의존성을 가지고 있다면, 개별적으로 삭제할 수 없다. 강제로 삭제하길 원한다면
-f (force) 옵션을 주어 삭제한다.

