Title: Some-blog-system over Xtorage
Time: 03:27:00

User ( 혹은 Account )

- 세션/쿠키/권한 관리

Layout ( 혹은 Page )

- 가장 바깥 프레임을 묘사.

View ( 혹은 Menu )

- 특정 문서 종류만, 또는 특정 문서 종류만 제외하고 선택 가능.

- 테마는 View 단위로 지정됨. ( 게시판 형태 / Matrix 형태선택 등 )

Doctype ( 혹은 Type )

- XSD 1개, List XSL과 Body XSL로 구성됨.

- Mobile XSL이 가능할 듯? -> CSS 변경만으로 달라질지도?

- 사용자별 권한 설정 가능.

Doc ( 혹은 Post )

- type에 기반한 Highly restricted document.

- XML

- Comment 연결 여부 선택 가능.

Comment

- Doc에 1:N으로 연결.

------

(사용예)

Blog View - Memo Doctype과 Guestbook Doctype을 제외하고 모두 표시한다. Post Doctype의 List
XSL은 Body XSL과 같아, 블로그와 같은 표시가 가능하다.

Photolog View - Post Doctype을 PhotoList XSL로썸네일만 출력하도록 하고, Body XSL은 그대로 사용.
단, 사진이 있는 문서만 표시.

Videolog View - Photolog View와 유사.

Memo View - Memo Doctype을 일반 게시판처럼 표시.

Guest View - Guestbook Doctype을 표시한다. Blog Doctype과 유사함. 단, Guestbook Doctype은
anonymous 상태에서 작성 가능하도록 한다.

