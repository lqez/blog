Title: The Curse of Understanding
Date: 2017-11-13
Lang: ko


> The curse of the monad is that once you get the epiphany, once you understand, 
> you lose the ability to explain it to anybody else.
>
> Douglas Crockford - [‘Monads & Gonads’ at YUIConf 2012](https://www.youtube.com/watch?v=dkZFtimgAcM)


[모나드](https://en.wikipedia.org/wiki/Monad_(functional_programming))는 함수형 프로그래밍 언어에 대해서 얘기할 때 거의 매번 언급되는 주제이다.
모나드라는 개념이 절차형 프로그래밍 언어에 익숙한 사람들에게는 익숙한 개념이 아니기 때문에, 
[모나드 괴담](https://e.xtendo.org/haskell/ko/monad_fear/slide) 같은 글이 쓰여질 정도다. (해당 문서는 매우 훌륭하다!)

어떤 개념을 비로소 깨닫는 순간을 [‘Aha moment’](https://www.merriam-webster.com/dictionary/aha%20moment)라 부르기도 하는데,
더글라스 크록포드의 말을 인용하자면, 모나드를 이해하는 Aha moment를 겪는 순간,
다른 사람에게 모나드를 설명할 수 없게 되는 [저주](https://stackoverflow.com/questions/19544794/what-is-crockfords-law)에 걸린다고 한다.

그런데, 모나드만 그러한가? 세상의 많은 이해와 문제들이 비슷한 상황에 놓여 있다.
간략화한 적당한 비유를 통해 설명하는게 처음 접하는 사람들에게 쉽게 느껴지겠지만, 대부분의 경우는 결국 불필요한 오해를 가져온다.
*프로그래밍이란 무엇인가요?* *캐시(cache)는 쓰면 좋은가요?* 정확하게 이해하려면 많은 정보와 이해를 필요로 하지만 과연 어디서부터 얼만큼 설명할 것인가?
한 개인이 이해한 것을 다른 사람에게 설명하는 일은 매우 어렵다. 이해와 사전 지식이 다르기 때문에 자신이 어떤 문제에 대해 깨달은 길을 그대로 다른 사람에게 걷게 해도, 그 사람은 깨닫거나 이해하지 못할 수 있다.

도리어 경험과 노력이 부족하여 충분히 이해하지 못하거나 깨닫지 못한 ‘가짜 전문가’가 더 많이 얘기하고 설명하는 경우도 보게 된다.
이런 사람은 틀린 정보를 거부감 없이 받아들이고, 해석하려고 하지 않으며, 흘려 들은 정보를 마음대로 가공하여 다른 사람에게 조언하거나 추천하기도 한다.
상대적으로 많은 것을 제대로 알고 있는 사람은 다음의 문제를 겪기도 한다.

  - 문제에 대해 설명하는 경우
    - 많은 사람을 위해 온전히 설명하면 충분히 쉽게 말하지 못해 ‘잘 모르는 사람’ 취급을 받는다.
    - 자세한 것을 건너뛰고 핵심만 말하면 엉뚱한 얘기를 하는 ‘잘 모르는 사람’이 된다.
  - 설명하지 않고 침묵하는 경우
    - 마찬가지로 ‘잘 모르는 사람’ 취급을 받는다.

나는 이런 문제들을 일반화하여 **이해의 저주(The Curse of Understanding)**라고 부르고 싶다.

덧) 이 생각을 [트윗](https://twitter.com/lqez/status/759061524820299776)으로 썼더니, @tebica 님이 이에 공감하여 블로그 [포스팅](http://earlybird.kr/1938)을 남겼다. 
