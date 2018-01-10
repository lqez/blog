Title: Mac OS X Server 에서 sshd 포트 변경하기
Time: 14:45:00

Remote access를 위해 ssh를 사용하게 되는데, (VPN을 쓰더라도) 최소한의 보안을 위해 sshd의 포트를 변경하여 사용하는
것이 일반적이다.

  

Mac OS X Server에서는 openbsd의 sshd를 사용하는데, 다른 unix-ish와 마찬가지로 /etc/sshd_config가
있어, 해당 파일의 Port 값을 변경하면 되는 것으로 생각했다. 그러나, 해당 값을 변경하고 launchctl을 통해
org.openbsd.sshd를 재시작해봐도, 여전히 기본 포트에서 listen을 하기에 구글을 통해 방법을 검색해보았다.

  

해결책:

[http://www.macosxhints.com/article.php?story=20050707140439980](http://www.ma
cosxhints.com/article.php?story=20050707140439980)

  

(1)

/etc/services 파일에 ssh2항목을 추가한다.

    
      ssh2              10022/udp 
      ssh2              10022/tcp

(2)

/System/Library/LaunchDaemons 디렉터리안에 있는 ssh.plist 파일을 수정.

    
      <key>SockServiceName</key>
      <string>ssh2</string>
    
    (3)
    
    #service ssh stop
    
    #launchctl unload /System/Library/LaunchDaemons/ssh.plist
    
    #launchctl load /System/Library/LaunchDaemons/ssh.plist
    
    # service ssh start
    
    위와 같이 sshd 서비스를 재시작한다.
    
    재시작 이후에도 포트가 바뀌지 않았다면, 시스템을 재시작한다.
    
      
    
    
      
    
    
    다른 서비스에 대해서는 Server Admin에서 그럭저럭 기본 설정은 할 수 있는데, 정말 중요한 서비스인 Remote access에 대해 설정 패널을 제공하지 않는 것은 불만이다. 최소한 포트 정도는 바꿀 수 있게 해줬어야 하는게 아닐까 싶은데.
    
      
    
    
      
    

