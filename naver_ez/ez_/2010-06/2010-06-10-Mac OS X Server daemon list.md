Title: Mac OS X Server daemon list
Time: 16:37:00

Mac OS X Server에서 제공하는 서비스들이 어떤 프로그램으로 구동되는지 궁금하여 확인해보았다.

기준은 Mac OS X Snow Leopard Server (10.6.3)

  

AddressBook : carddavd

DNS : named (bind9)

Firewall : ipfwloggerd

iCal : caldavd

iChat : jabberd (XMPP)

Mail : amavisd (SMTP) + dovecot (IMAP/POP)

Open Directory : slapd (openldap)

Pust Notification : idavoll

SMB : smbd

Web : httpd (apache)

  

흥미로운 것은, caldav, carddav, idavoll 등 몇몇 서비스는 python이라는 것이다. 그것도 대부분 Twisted
Framework([http://twistedmatrix.com](http://twistedmatrix.com/))을 사용하고 있다.
dovecot을 쓰길래 SMTP도 당연히 postfix, exim, sendmail 류일 것이라 생각했는데, 의외로 낯선 amavisd?
man페이지에는 act as a mini-SMTP server 라고만 되어 있다.
([http://www.ijs.si/software/amavisd/](http://www.ijs.si/software/amavisd/))

  

그 외 처음 본 대몬.

clamd - an anti-virus daemon
([http://www.clamav.net/lang/en/](http://www.clamav.net/lang/en/))

  

ipfwloggerd도 낯설어서 정보를 찾다보니 애플의 오픈소스 디렉터리가 나온다. 체계적으로 관리되고 있는 것으로 보이진 않는 페이지.

[http://www.opensource.apple.com/source/](http://www.opensource.apple.com/sour
ce/)

  

  

