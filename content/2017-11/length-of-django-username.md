Title: The length of Django username
Date: 2017-11-16
Lang: ko

오래 전, [Django](https://www.djangoproject.com/)에서 제공하는 사용자 모델의 이름을 저장하는 기본 필드의 길이가 왜 30자인가에 대해 의문을 가진 적이 있었다.
필드의 길이가 짧거나 길어서 그런 생각을 했던건 아니고, 왜 하필 ‘30’ 일까에 대한 의문이었다.
물론 한국 사람들의 이름만 생각하면 30자면 충분하다. 한국 국적을 가진 사람 중에 가장 긴 이름을 가진 사람은 다음과 같다.

 - ‘박 하늘별님구름햇님보다사랑스러우리’(17자)
 - ‘프라이인드로스테쭈젠댄마리소피아수인레나테엘리자벳피아루이제’(30자)
 
출처: <http://www.hani.co.kr/arti/society/society_general/399615.html>

----

그 뒤로 잊고 살았는데, 얼마 전 발표된 [Django 2.0 RC 릴리즈 노트](https://docs.djangoproject.com/en/dev/releases/2.0/)를 보다가,
[사용자 이름 필드의 길이가 150자로 바뀐다](https://docs.djangoproject.com/en/dev/releases/2.0/#abstractuser-last-name-max-length-increased-to-150)는 항목이 눈에 띄었다.

하필이면, 왜 150자일까? 30자도 이상했지만 150자도 이상해서 [git blame](https://git-scm.com/docs/git-blame)을 통해 길이를 바꾼 커밋을 찾아보니,
예전보다 늘렸다는게 아니라 150자로 줄였다는 커밋이 마지막이었다.

 - [Decreased User.username maxlength to 150 characters.](https://github.com/django/django/commit/780bddf75b93784470a2e352ed44ee35a751d667)

그리고 같이 커밋된 도움말의 문서를 보면 다음과 같이 설명되어 있다.

> We considered an increase to 254 characters to more easily allow the use of
> email addresses (which are limited to 254 characters) as usernames but rejected
> it due to a MySQL limitation.  When using the ``utf8mb4`` encoding (recommended
> for proper Unicode support), MySQL can only create unique indexes with 191
> characters by default. Therefore, if you need a longer length, please use a
> custom user model.

이전에 254자로 늘린 이력이 있었는데, MySQL 등에서 유니코드 문자를 저장하는데 주로 쓰이는 `utf8mb4` 인코딩을 사용하는 경우에
인덱스 지정에 문제가 생길 수 있어 150자로 줄이는 선택을 했던 모양이다.
254자로는 언제 늘렸나 보아하니, 2년 전에 이미 머지가 되었던 이력이 있다. 

 - [Increased User.username max_length to 254 characters.](https://github.com/django/django/pull/5497)

그리고 이전에 이미 사용자 이름을 늘리는 것에 대한 PR이 올라왔었지만, 도움말 등을 작성하는게 미진하여 머지되지는 않았다.
오픈소스 프로젝트에서는 정말 흔한 일이라고 생각한다.

 - [Fixed #20846 -- Change username max_length to 254](https://github.com/django/django/pull/4250)

드디어, 사용자 이름을 늘리는 것에 대한 [티켓 #20846](https://code.djangoproject.com/ticket/20846)을 찾았다. 
이 티켓을 읽어보면 다음과 같은 이유로 사용자 이름의 길이를 늘리자고 건의하고 있다.

> Nowadays it is common to use e-mail addresses as usernames (especially if using external auth sources such as OAuth),
> but while the email field is reasonably long (75), the 30 characters for the username seems too short for modern sites.

OAuth 등을 사용하면 이메일 주소를 사용자 이름에 넣는 경우가 흔한데, 이메일 필드의 길이는 상대적으로 긴 75자인데 비해 사용자 이름은 짧으니 늘려보자는 의견이다.
뿐만 아니라, 사용자 이름에 대한 프로그래머들의 흔한 착각에 대해서도 언급하고 있다.
해당 글에서는 프로그래머들에 가지고 있는 흔한 가정들이 잘못되었음을 꼬집고 있다.

 - [Falsehoods Programmers Believe About Names](http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)

자, 이제 거의 마지막까지 왔다. 위 글은 존 그레이엄-커밍의 블로그 글을 링크하고 있다.
대부 존 그레이엄-커밍이 웹 서비스에 가입하다 자신이 이름에 잘못된 문자(invalid characters)가 있다는 메세지에 분노하여 남긴 글이다.
이름에 하이픈(-)이 포함되어 있어서 여러 사이트에서 문제를 겪어왔던 것 같다.

 - [Your last name contains invalid characters](http://blog.jgc.org/2010/06/your-last-name-contains-invalid.html)

----

덧1) 어느 나라나 악플러는 있기 마련인 것 같다. 존 그레이엄-커밍의 블로그 포스팅에도 아래와 같은 사려깊지 못한 댓글이 달려있다. 흠.

> Change your name. Not that big of a deal.

덧2) 이메일 필드는 여전히 75자일까? 그렇지 않다. 사용자 이름 필드가 늘어나기 1년 전에 이미 254자로 늘어나 있었다.

 - [Fixed #20631 -- Increased the default EmailField max_length to 254.](https://github.com/django/django/pull/2867)
 - <https://code.djangoproject.com/ticket/20631>
 - [What is the maximum length of a valid email address?](https://stackoverflow.com/questions/386294/what-is-the-maximum-length-of-a-valid-email-address)
 - [RFC5321 #4.5.3.1, Size Limits and Minimums](https://tools.ietf.org/html/rfc5321#section-4.5.3)

덧3) MySQL의 InnoDB 엔진에서 문자열에 대한 인덱스는 767바이트로 제한되어 있고,
1글자에 4바이트를 사용하는 `utf8mb4` 인코딩에서는 767 ÷ 4 ≈ 191 이기 때문에 191자로 제한된다.
 
 - <https://dev.mysql.com/doc/refman/5.5/en/charset-unicode-conversion.html>
