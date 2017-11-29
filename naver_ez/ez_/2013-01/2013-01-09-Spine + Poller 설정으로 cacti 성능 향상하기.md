Title: Spine + Poller 설정으로 cacti 성능 향상하기
Time: 15:31:00

Cacti에 대해서 잘 모를 때에 - 지금도 잘 모르지만 - "cacti는 크롤러가 단일 프로세스라서 짜증나요" 같은 얘기를 하고 다녔는데
모두 취소.

1. Cacti에서 크롤러(poller) 역할을 하는 cmd.php를 단일 프로세스가 아니라, 여러 프로세스로 동작시킬 수 있다.

2. 그래도 성능이 부족한 경우 spine을 설치하여 multi process + multi thread 로 성능을 더 향상시킬 수 있다.

spine
:[http://www.cacti.net/spine_info.php](http://www.cacti.net/spine_info.php)

![](Screen_Shot_2013-01-09_at_3.25.04_PM.png)

멀쩡하게 존재하는 concurrent 및 spine 관련 옵션.capture

혹시라도 poller 속도에 불만을 가진 사람이라면 꼭 spine을 설치하지 않아도 Maximum Concurrent Poller
Processes 값만 조정해도 퍼포먼스 향상이 될 듯.

단일 프로세스로 수행하던 때에는 조금 지연되면 몇 분씩 걸리는 경우도 있었는데, 4 processes x 16 threads 로 사용하는
지금은 10초 이내로 처리 끝.

