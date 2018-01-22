Title: Python simple UDP Server / Client
Time: 21:24:00

UDP Server

  

GIST : [https://gist.github.com/3059844](https://gist.github.com/3059844)

> #!/usr/bin/python

>

> import socket

>

> sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

>

> sock.bind(("", <port>))

>

> while True:

>

> data, addr = sock.recvfrom(1024)

>

> print data.strip(), addr

  

UDP Client

  

GIST : [https://gist.github.com/3059847](https://gist.github.com/3059847)

> #!/usr/bin/python

>

> import socket

>

> sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

>

> sock.sendto("foobar", ("<host>", <port>))

<host>와 <port>를 적절한 값으로 바꿔,UDP 포트 막혀있는지 테스트할 때 사용하면 됩니다.

