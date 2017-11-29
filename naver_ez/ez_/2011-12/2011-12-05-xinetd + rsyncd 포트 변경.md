Title: xinetd + rsyncd 포트 변경
Time: 19:41:00

요즘 사용중인 AWS EC2용 Amazon Linux 등 몇몇 리눅스 배포판에서는rsyncd가 xinetd를 통해서 실행되도록 설정되어
있으므로, rsyncd를 위한 별도의 startup script는 없다.아래의 절차를 통해 rsyncd 를 데몬으로 실행하여 사용할 수
있다.

  

**1. xinetd 및 rsync 설치 (확인)**

$ sudo yum install xinetd rsync

  

**2. /etc/rsyncd.conf 및 /etc/rsyncd.secret 파일 생성**

이 과정은 다른 rsyncd 생성 과정과 다를 바 없으므로 생략.

( 참조 : [http://blog.bagesoft.com/767](http://blog.bagesoft.com/767) )

  

**3. rsyncd 활성화**

$ sudo chkconfig rsync on

  

**4. xinetd 재시작**

$ sudo /etc/init.d/xinetd restart

  

**5. 포트 변경 (옵션)**

rsyncd 포트를 변경하고 싶은 경우, /etc/rsyncd.conf에 port 옵션을 사용하는 것으로는 변경이 되지 않으므로,
/etc/services 파일에서 rsync 항목을 찾아 수정후, xinetd 를 재시작한다. 873번이 기본 포트.

rsync 873/tcp # rsync

rsync 873/udp # rsync

  

  

  

