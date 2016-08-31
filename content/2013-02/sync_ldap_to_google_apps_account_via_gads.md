Title: Sync LDAP to Google Apps account via GADS
Date: 2013-02-26
Lang: ko
Tags: ldap, google, gads, sync

Google은 - 친절하게도 - Google Apps 계정을 외부 서버와 동기화할 수 있는 기능을 제공할 뿐 아니라, 이를 위한 도구도 배포하고 있다.

* [Google Apps Migration for Microsoft Exchange](http://support.google.com/a/bin/answer.py?answer=172212)
* [Google Apps Directory Sync](http://support.google.com/a/bin/answer.py?answer=106368)
* [Google Apps Password Sync](http://support.google.com/a/bin/answer.py?answer=2611842)

스마트스터디는 사내 계정을 이미 LDAP으로 통합 운용중이라서, Google Apps Directory Sync(이하 GADS)를 선택하였다.

* [Google Apps Directory Sync Administration Guide(in PDF)](http://www.google.com/support/enterprise/static/gapps/docs/admin/en/gads/admin/)


GADS는 단방향 즉, LDAP에서 GADS로의 동기화만을 제공한다. 동기화 가능한 항목은 아래와 같다.

* Organizational Units
* Users Accounts
* Groups
* User Profiles
* Shared Contacts
* Calendar Resources

GADS Configuration Tool은 자바를 이용한 GUI로 작성되어 있는데, 현재는 Windows / Linux 용만 제공된다. 이 툴을 통해 설정한 내용은 XML로 저장되고, 이 파일은 플랫폼 무관하게 사용할 수 있으므로, 일단 가상 머신의 Windows로 설정을 완료한 후에, 설정 파일을 복사하여 Linux에서 사용하였다.

![Screen Shot of GADS](./images/gads_01.png)

Linux용 GADS는 커맨드라인에서 설치하면 동의항목이 HTML로 출력되지만, 계속 엔터키를 입력해 넘기며 진행하면 설치가 가능하다.
root 계정으로 설치하는 경우에 /usr/local/GoogleAppsDirSync 에 설치가 되고, 이 디렉토리 아래에 있는 `sync-cmd` 쉘 스크립트를 통해 동기화를 수행하면 된다.

    $ ./sync-cmd -c <configuration_file.xml>

위와 같이 실행하면 비교만 하고, 실제로 동기화는 하지 않는 dry-run으로 실행되고,

    $ ./sync-cmd -a -c <configuration_file.xml>

`-a` 옵션을 추가해야 실제 동기화가 이뤄진다. 현재는 위 명령을 cron에 넣어 5분 마다 동기화 하도록 설정해두었다.
