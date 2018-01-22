Title: gittip.com and /for/korea
Date: 2013-05-14
Lang: ko
Tags: gittip, donate, contribute

얼마 전, [Schema Migrations for Django](http://www.kickstarter.com/projects/andrewgodwin/schema-migrations-for-django) 라는 오픈소스 프로젝트 계획에 대한 모금 활동이 킥스타터에서 큰 성공을 거뒀다. 이제까지 오픈소스를 사용하면서 개발한 이들에게 고마움을 표시하는 방법은 해당 프로젝트를 열심히 사용하며, 버그 제보, 번역, 기능 추가 또는 사용기 발표 정도 밖에 없다고 생각했는데, '금전적인' 후원도 가능하다는 것을 알게 되었다.


Gittip
------

![gittip.png](./images/2013-05/gittip.png)

<https://www.gittip.com> 은 오픈소스 개발자나 오픈소스 그룹에게 정기적으로 후원을 할 수 있는 웹서비스이다. 앞서 언급한 킥스타터와는 달리, 한 번 기부하고 마는 것이 아니라 지정한 금액을 매주 목요일 기부하게 된다.
궁극적으로 이 사이트를 통해 의미있는 오픈소스 개발을 하는 사람이나 단체가 전업으로 오픈소스를 진행할 수 있는 기반을 갖게된다면 좋겠지만, 아직까지 그 정도로 많은 금액이 오고가는 것으로 보이진 않는다. 하지만, 주기적인 기부는 위와 같은 단기적인 프로젝트 기금 마련과는 다른 방향을 가지고 있고, 이는 오픈소스에 보다 긍정적인 문화를 가져올 것 같다.


/for/korea
----------

Gittip 의 커뮤니티 기능이 약 [2주 전에 추가](https://github.com/gittip/www.gittip.com/commit/f2ca1fa1f3eb1c8cabe9b98bebc1e180dd669e61)되었는데, 이에 한국 파이썬 커뮤니티계의 아이돌(...) @hongminhee 님이 한국 개발자 커뮤니티([/for/korea](https://www.gittip.com/for/korea/))를 만들고, 가입을 요청하는 트윗을 올렸다.

@hongminhee/status/333868284195770368

해당 요청은 트위터나 페이스북을 통해 오픈소스에 관심이 있는 한국 개발자들에게 빠르게 전파되었고, 덕분에 몇 시간 지나지 않아 커뮤니티 구성 요건의 최소 인원인 150명에 가장 빠르게 도달하였다. 하지만 개발자 @whit537 도 이처럼 빨리 150명에 도달할 것이라 생각하지 못한 모양이다.

@whit537/status/333945787216175104
@whit537/status/333948844951891969

@whit537 은 다음과 같은 커밋을 통해, 'korea' 커뮤니티의 150명 도달에 긴급히 대비하였다.

 - [#03429b3 Get barely ahead of Korea maybe](https://github.com/gittip/www.gittip.com/commit/03429b36850b163879afc64b35d160f8f3c13146)
 - [#c52b4c8 Korea beat us to this!](https://github.com/gittip/www.gittip.com/commit/c52b4c8d817e9c86453f118bbae72d355dedb0b3)

그는 한국에서 왜 이렇게 많은 가입자가 발생했는지 궁금하였던 모양이다. 그에게 아이돌(...)을 소개시켜 주었는데, 결국 @hongminhee 님은 [freenode IRC](http://freenode.net/) 의 #gittip 채널에 들어가 개발자들과 얘기를 몇 마디 나누더니, 그세 개발에 참여하고 있는 것으로 보인다! ([pull #182](https://github.com/gittip/aspen-python/pull/182), [pull #183](https://github.com/gittip/aspen-python/pull/183)) 

@whit537/status/333951758990733312
@whit537/status/333952649152053248

Small step for us
-----------------

![gittip-korea.png](./images/2013-05/gittip-korea.png)

Gittip의 커뮤니티 중, [/for/korea](https://www.gittip.com/for/korea/)가 가장 먼저 최소 요건인 150명을 돌파하였다. 특정 국가 커뮤니티로써 가장 큰 것일 뿐 아니라, 다른 모든 커뮤니티(예:[/for/python](https://www.gittip.com/for/python/)) 중에서도 가장 인원이 많다. 이렇게 많은 개발자가 이런 사이트에 관심을 가지고 있는 줄 몰랐고, 이렇게 빨리 가입한 것은 더욱 놀랍다. 그럼에도 불구하고 부끄러운 것은, 한국인 커뮤니티에 가입한 사람들이 기부하고 있는 금액이 너무 적다는 점이다. 물론 한국 개발자들 중에서 아직 이 커뮤니티의 존재를 몰라, 가입하지 않은 상태로 기부하고 있을 수도 있겠다. 또는, 페이팔 계정이나 해외에서 자유롭게 결제 가능한 카드를 우리나라에서 만들기가 어려웠던 부분도 있을 것이다. 하지만 이 글을 쓰고 있는 현재, 도합 몇 달러가 채 안되는 금액이라는 것은 조금 아쉽다.
 
나는 예전에 @hongminhee 님에게 [py.test](http://pytest.org/latest/) 의 디버깅 도움을 받아, 이 사이트에서 후원하려다가 아직 계좌 연결을 시켜두시지 않은 관계로, 대신 독콜라(...) 한 박스를 보낸적이 있다. 아무튼 오늘 다시 한 번 사이트에 들어간 차에 적은 금액이지만 주당 $1.50 을 후원하도록 설정하였다.

오픈소스를 만들고 기꺼이 공개한 이들에게 감사를 표시하는 차원에서, 이 글을 읽는 분들도 자기가 쓰고 있는 프로젝트의 개발자나 그룹에 후원해보는 것은 어떨까?
