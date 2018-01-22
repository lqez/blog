Title: Fool Upstart
Date: 2014-07-17
Lang: ko
Tags: diary, ubuntu

Upstart
=======

[Upstart](http://upstart.ubuntu.com/)는 /sbin/init 를 대체하기 위한 우분투의 기본 서비스 관리자다.
다양한 서비스를 daemon 형태로 관리하고, 죽은 경우에 자동으로 다시 실행할 수 있는 등 편리한 기능을 갖추고 있다.

프로세스 ID를 받아 해당 프로세스가 잘 동작하는지 감시해야 하므로,
해당 서비스가 어떤 형태로 시작되는지 알고 있어야 정확한 프로세스 ID를 얻을 수 있다.
Upstart 설정 중, [expect stanza](http://upstart.ubuntu.com/cookbook/#expect)가 이를 결정하며 일반적인 프로세스는 설정하지 않아도 동작하지만,
해당 프로세스가 fork 되어 동작하거나 daemonize 되는 경우, 별도의 값을 지정해야 정확한 ID 확인이 가능하다.
이 부분에 혼란을 겪은 사람이 꽤 많아, 홈페이지 에서 별도로 안내하고 있을 정도다.

  - [6.13.5 Implications of Misspecifying expect](http://upstart.ubuntu.com/cookbook/#implications-of-misspecifying-expect)


Symptom
-------

보통은 이 값을 잘못 설정한 경우에 서비스가 제대로 감시되지 않거나, 종료되지 않는 등의 문제가 생기는데
오늘은 해당 서비스를 재시작하면서 별다른 설정의 변경이 없었음에도 불구하고, 이상한 상태에 빠지고 말았다.

    $ initctl list | grep flower
    one/flower start/killed, process 14645

이 상황에서는 `start` / `stop` 명령어가 전부 hang이 되어 서비스 재시작이나 종료가 불가능하다.
`start/killed` 로 표시되는 프로세스 ID를 `ps`로 찾아보면 당연히 없는 프로세스 ID다.
한참을 헤매다 혹시나 싶어 upstart configuration 파일을 복제하여 다른 이름으로 바꿨더니, 제대로 동작한다!

    $ initctl list | grep flower
    one/flower start/killed, process 14645
    one/flower_dup start/running, process 17171



Solution
--------

시스템을 재시작하면 복구될 것 같았지만, 당장 재시작할 수 없는 프로덕션 시스템이라
혹시나 하여 구글링을 계속하다보니 누군가 만들어둔 루비 스크립트를 찾게 되었다.

  - <https://github.com/ion1/workaround-upstart-snafu>

프로세스가 `start/killed` 또는 `stop/killed` 상태일 때 사용할 수 있는 이 스크립트는,

  1. 포크하여 프로세스 A를 하나 생성한다.
  2. 프로세스 A에서 문제의 프로세스 ID를 받을 때까지 계속해서 자식 프로세스 B를 포크한다.
  3. 지정된 ID를 얻으면 프로세스 A, B를 모두 종료한다.
  4. Upstart는 이것이 정상적인 프로세스 종료로 판단하고 혼란 상황에서 빠져나온다.

우여곡절 끝에 문제 해결.

    $ initctl list | grep one
    one/flower start/running, process 14810

