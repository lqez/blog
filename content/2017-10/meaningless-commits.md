Title: Meaningless commits
Date: 2017-10-31
Lang: ko

하고 있는 일에 지나치게 몰입하여 주변을 살피지 못하게 되면, 보다 의미있는 결과를 내기가 어렵다.
요즘 아무도 사용할 것 같지 않은 기능들을 만드는데 시간을 낭비하고 있다.

 - 마크다운 목록 정렬하기
 - 한글 처리를 위한 Django template filter/tag 만들기
 - 위지윅 에디터 만들기

## mdls - Markdown List Sorter

<https://github.com/lqez/mdls>

먼저, [마크다운](https://daringfireball.net/projects/markdown/)은 애초에 표현과 내용의 분리를 중요하게 생각하고, 글을 – 비교적 – 체계적으로 쓰기를 원하는 사람들이 선호하는 글의 형식인데,
이런 유형의 글에 포함되어 있는 목록을 정렬하는 프로그램을 만들겠다는 것 자체가 별 의미가 없다.
마크다운의 목록은 대체로 글쓴이의 의도대로 정렬되어 있을 가능성이 높기 때문이다. ordered list 뿐만 아니라 unordered list 의 경우도 마찬가지다.

이 기능을 만든 유일한 이유는 관리하고 있던 [awesome-summernote](https://github.com/summernote/awesome-summernote/)의 플러그인 목록 때문이다.
각 분류에 속해있는 목록을 이제까지는 추가된 순서대로 보관해왔는데, 어떤 기여자가 자신이 추가한 플러그인을 [가장 아래가 아닌 곳에 추가](https://github.com/summernote/awesome-summernote/pull/43/files)하면서 고민이 시작되었다.
만약 기계적으로 목록을 정렬할 수 있다면, 해당 pull request가 유효한지 검증할 수도 있고, 그렇지 않은 경우 자동으로 정렬하는 것도 가능하기 때문이다.

하지만, 이는 많은 목록을 관리하기에 애초에 적합하지 않은 마크다운 형식을 쓰는 것 자체가 문제인데, 이를 잘못된 방법으로 해결하려는 것에 가깝게 느껴진다.
그래도 일단 시작했으니 해당 프로젝트의 빌드 과정에 적용할 때까지는 해보려고 한다.

## django-tossi

<https://github.com/lqez/django-tossi>

[Korean](http://pythonhosted.org/korean/)은 한글의 형태소를 다루는 라이브러리였다.
과거형으로 적는 이유는 저작자가 이 프로젝트를 deprecate 시키고 [Tossi](https://github.com/what-studio/tossi)라는 새로운 라이브러리를 만들고 있기 때문이다.
예전에 Korean 라이브러리를 사용하여 Django template 상에서 적절한 조사를 선택하여 출력하는 것을 도와주는 django-template-korean 확장을 만들었는데,
아예 [Korean 모듈 내부로 내장](https://github.com/sublee/korean/pull/3)하면서 해당 프로젝트도 중단했었다.

하지만 Korean 라이브러리는 개발이 중지되었으므로 Tossi를 이용해서 django-template-korean을 django-tossi로 다시 살려보려고 한다.
헌데, Korean 라이브러리에 있던 [proofreading](http://pythonhosted.org/korean/#proofreading-legacy-text) 기능이 Tossi에서는 사라졌다.
이 기능을 django-tossi 내에 구현을 할까 아니면 Tossi 쪽에 추가하는 PR을 보낼까 고민을 했는데, 이 기능을 만들기 전에 과연 이 기능을 얼마나 자주, 중요하게 쓰고 있었는지 생각해볼 필요가 있다는 생각이 들었다.
원래 있었던 것이 없어졌다고 해서 그냥 만드는 것이 아니라, 왜 없어졌을까, 그동안 이 기능을 유용하게 썼는가 한 번 따져봐야겠다.

## summernote

<https://github.com/summernote/summernote>

2013년부터 참여해오고 있는 프로젝트. 요즘에 누가 위지윅 에디터를 만드냐 싶을 정도로 예전보다는 관심이 많이 줄어든 것이 사실이다.
대부분 의식하지 못하고 있어서 그렇지 [페이스북의 글쓰기 창도 위지윅](https://github.com/facebook/draft-js)이다.
이 프로젝트에 시간을 쏟는 것이 어떤 긍정적인 변화를 가져올지 아직 잘 모르겠지만, 한번 시작한 일은 책임지자는 마음으로 계속 조금씩 기여하고 있다.

하지만, 최근에는 예전만큼 기여하지 못하고 있기도 하고, 다른 기여자들도 실무가 바뀌가 시간이 없어져 프로젝트 관리가 제대로 되고 있지 못하다.
어떤 기여자는 프로젝트 작성자와 기존 기여자들이 제대로 활동하지 않는 것에 걱정과 [불만을 가지고 있다](https://github.com/summernote/summernote/issues/2526).
계속 꾸준히 하는 것 외에 어떻게 잘 할 수 있을지 고민이 필요하다.


그냥 오늘 손댔던 일들을 적어본 글.
