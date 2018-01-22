Title: Mac OS X Server에서 hostname/ip 변경하기
Time: 17:35:00

처음 서버를 설정할 때에는 도메인과 ip가 실 서비스 환경과 다를 경우가 많다.

그래서 임시 ip와 임시 도메인 네임(example.com)등으로 설정하게 되는데 이를 바꾸기 위해서는 changeip를 사용한다.

changeip [-v] [-d path] old-ip new-ip [old-hostname new-hostname]

  

현재 값 확인을 위해서는 아래의 명령을 실행한다.

changeip -checkhostname

  

  

자세한 내용은 man changeip를 통해 확인한다.

  

  

