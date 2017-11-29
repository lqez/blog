Title: Oracle Berkeley DB XML
Time: 18:27:00

거의묵은지가 되어가는 메타포 이야기를 꺼내본다.

아무튼 xindice 뒤져보다가, 개발은 거의중단된 상태인데, 그 이유는,

- 쓸만한 Native XML DB를 찾다보니, 그럴싸한게 안보였고,

- Xindice는 Java 인터페이스만 제공했고,

- Xtorage라는 RDBMS기반의 php로 작성된 XML storage를 구성하려고 했는데, 능력이 안되서 중단.

헌데 오늘 haje01 님이 오라클의 BDB기반의 XML DB/API를 말씀해주셔서 잠깐 찾아보았다.

[http://www.oracle.com/technology/products/berkeley-
db/xml/index.html](http://www.oracle.com/technology/products/berkeley-
db/xml/index.html)

* Programmatic administration and management - zero human administration 
* Command line tools to load, backup, dump and interact with the XML databases 
* Language support (C++, Java, Perl, Python, PHP, Tcl, Ruby, etc.) 
* Operating system support (Windows, Linux, BSD UNIX, Mac OS/X and any POSIX-compliant operating system) 
* Installer for Microsoft Windows 
* Apache integration 
* Documents up to 256TB 
* Source code, test suite included 

내가 주로 사용하는 데비안 패키지에는 stable/unnstable/testing 어디에도 등록되어 있지 않다는 것이 아쉽긴 하다.

