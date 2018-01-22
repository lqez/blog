Title: 스마트 에디터에 북마클릿으로 Monospace font family 넣기
Time: 23:21:00

아래 북마클릿 코드를 북마크에 등록하면 네이버 블로그 스마트 에디터의 글꼴 메뉴의 Verdana 폰트가 monospace로 변경된다.

네이버 블로그에서 립코딩 블로거라도 되려면 Monospace가 꼭 필요해서 만들어 보았다.

  

> javascript:var f = window.frames.mainFrame.papermain; var e =
$Element(f.$$('.se2_l_font_fam li')); var e = $Element(e._element[10]);
e.html('<button type="button"><span>Monospace<span>(</span><em style="font-
family:monospace;">abcd</em><span>)</span></span></button>');

느낀 점 : jindo framework는 jQuery에 길들여진 내게 정말 안 맞는구나.

  

