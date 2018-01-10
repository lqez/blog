Title: MongoDB : Ubuntu Server에서 MongoDB replication 설정
Time: 20:17:00

Ubuntu Server에서 MongoDB replication 설정 이후, 잊어버릴게 뻔해서 남기는 글.

(MongoDB 1.6 이상에서는 Master - Slave 전략 외에 3-tier의 ReplicaSet을 사용할 것을 추천하고 있다.)

  

대부분의 도움말 & HOWTO 문서가 startup variable 기준인데 비해,

이 글은 daemon + configuration file 기준으로 설명한다.

  

  

설치

  * $ sudo apt-get install mongodb
  * 위 패키지는 서버 바이너리인 mongod와 클라이언트인 mongo를 모두 포함한다.

  

  

설정

  * 기본 설정파일의 위치는 /etc/mongodb.conf
  * Master 설정
    * bind_ip = 127.0.0.1
      * 기본 값인 127.0.0.1은 로컬 접속만 허용하게 되므로, 0.0.0.0 혹은 특정 IP를 바인딩 하도록 값을 수정.
      * 보안을 위해 iptables 등의 방화벽 도구로 접속을 제한한다.
    * port = 27017
      * 기본으로 27017 포트를 사용. 경우에 따라 이 값을 수정.
    * master = true
    * oplogSize = <MB>
      * 별도로 지정하지 않으면, 여유 공간의 5% 정도를 사용하는 것이 기본값.
  * Slave 설정
    * slave = true
    * source = <master>
      * hostname 이나 ip를 입력
      * 포트를 지정해야 하는 경우 hostname:port 또는 ip:port 로 설정.
      * telnet 등을 이용해 미리 master로의 연결을 테스트한다.

  

운영

  * /etc/init.d/mongodb 대신 다음의 유틸리티 사용을 권장하고 있다.
    * 시작
      * $ start mongodb
    * 종료
      * $ stop mongodb
    * 재시작
      * $ restart mongodb

  

레퍼런스 문서 :[http://www.mongodb.org/display/DOCS/Master+Slave](http://www.mongodb
.org/display/DOCS/Master+Slave)

