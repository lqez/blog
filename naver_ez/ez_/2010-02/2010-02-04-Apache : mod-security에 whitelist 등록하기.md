Title: Apache : mod-security에 whitelist 등록하기
Time: 19:04:00

사내/사외에서 운용중인 웹 서버에 mod-security를 적용해서 잘 사용하고 있다.

kisa에서 공급하는 룰 파일을 조금 수정해서 쓰고 있었는데, 가끔 리치에디트에 워드 문서를 붙여넣고 posting하면 튕겨내는 문제가 있어
사내 IP대역을 화이트리스트로 등록해야 했다.

  
구글 검색 결과:

http://www.modsecurity.org/documentation/faq.html#d0e400

  
방법:

SecRule REMOTE_ADDR "^xxx\.xxx\." phase:1,nolog,allow,ctl:ruleEngine=Off

  
위와 같이 정규표현식으로 특정 IP 어드레스 혹은 대역에 대해 ruleEngine을 꺼서 해결하였다.

  
  
  

