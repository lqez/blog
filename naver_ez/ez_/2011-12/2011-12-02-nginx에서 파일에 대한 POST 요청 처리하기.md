Title: nginx에서 파일에 대한 POST 요청 처리하기
Time: 15:17:00

nginx는 기본적으로 파일과 같은 정적 콘텐츠를 POST로 요청할 경우 HTTP Response 405 ( Method not
allowed )를 리턴한다.

  

요청하는 쪽에서 method를 POST 대신 GET 으로 변경하는 것이 정석이지만, 경우에 따라 변경이 어려울 수 있다.

이럴 경우, nginx 설정 중 proxy_pass 를 이용해 이를 우회 처리한다.

  

> error_page 405 = @post_to_get;

>     location @post_to_get {

>             root [your document root];

>             proxy_pass [http://your hostname];

>             proxy_method GET;

>     }

위의 방법을 사용하면 일단 POST 요청을 보내는 클라이언트를 수정하지 않아도 서비스는 가능하지만, 로컬 소켓 연결이 많아지는 문제가
생긴다. 정적 컨텐츠 요청은 GET을 사용하도록 수정하는 것이 좋다.

  

  

  

  

