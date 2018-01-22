Title: Weird result from Naver search
Date: 2018-01-22
Lang: ko

예전부터 네이버 블로그 검색에서 ‘최신순’ 검색을 했을 때 검색어와 무관한 결과가 나와서 갸웃거린 경우가 있었는데, 그냥 네이버 검색이 별론가 생각하고 넘어갔었다.

오늘은 [BMW X3 (G01)](https://en.wikipedia.org/wiki/BMW_X3#Third_generation_(G01;_2018%E2%80%93present))이 출시되었다는 얘기를 듣고 관심이 생겨 네이버에서 검색해보았다.
역시나 최신 기준으로 검색 결과를 보았을 때 이상한 콘텐츠들이 주를 이루지만, 속는 셈 치고 들어가 콘텐츠를 살펴보았다.

![Search result](./images/2018-01/weird-naver-search-01.png)

하지만 포스팅 본문에는 검색 결과에서 보여진 문장이 보이지 않는다.
스타일을 통해 숨겨졌나 싶어 개발자 도구를 통해 소스를 보니, 역시나 자동 생성된 문자들이 `hidden="hidden"` 속성과 함께 본문 사이사이에 포함되어 있다.

```html
<p style="font-family: Tahoma; font-size: 12pt;">
    성능점검과 경정비까지
</p>
<p style="font-family: 나눔고딕,NanumGothic; font-size: 12px;" hidden="hidden">
    기아부터 여자가타기좋은되어야 렉스턴W할수 G25했다고 스마트해서 엠파크허브좋다.
</p>
```

보아하니 `기아`, `스마트` 등 자동차 관련 키워드와 한국어에서 사용하는 관용구와 조사들을 결합한 문자열을 자동 생성해주는 한국형 블로그 마케팅 도구가 있고, 이 도구를 중고차 딜러들이 많이 사용하고 있다고 추측할 수 있겠다.

![hidden attributes](./images/2018-01/weird-naver-search-02.png)

네이버는 이런 문제를 뻔히 알고 있을텐데, 자동 생성되어 맥락과 의미가 없는 숨겨진 문자열들을 검색 대상에 포함시키지 않는다면 검색 결과 개선에 도움이 되지 않을까 싶다.
