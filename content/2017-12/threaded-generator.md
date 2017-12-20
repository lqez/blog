Title: Threaded Generator in Python
Date: 2017-12-20
Lang: ko

[커맨드라인 인터페이스(CLI)](https://en.wikipedia.org/wiki/Command-line_interface)를 가진 프로그램을 만들면서 [비동기 처리](https://en.wikipedia.org/wiki/Asynchronous_I/O)를 시도한 적이 없었다.
대부분 선택지를 출력한 후에 사용자로부터 값을 입력받으면 다음 동작을 수행하는 것을 반복하기 때문에 일반적인 [단일 스레드](https://en.wikipedia.org/wiki/Thread_(computing)#Single_threading)로 작성해왔다.

이번에 만든 CLI 프로그램인 [rogrepos](https://github.com/lqez/rogrepos)는 GitHub에서 오픈소스 활동을 오래 하다 보면
수정사항을 작성하기 위한 목적으로 [포크](https://en.wikipedia.org/wiki/Fork_(software_development))했다가
더는 사용되지 않고 방치된 저장소들이 쌓이는데, 이들을 손쉽게 정리하기 위한 도구이다.

GitHub에서 저장소를 삭제하기 위해서는 확인 및 안전 차원에서 저장소 이름을 다시 한 번 입력해야 하는데,
정리해야 하는 저장소가 많으면 이 작업을 반복하는 것이 여간 귀찮은 일이 아니다.
rogrepos를 처음에는 기존처럼 비동기 처리 없이 단일 스레드로 작성하였는데 [GitHub API](https://developer.github.com/) 호출이 여간 느린 게 아니라,
실제로 쓰기에는 실용적이지 못했다. 저장소 목록을 얻어오는 것은 오래 걸리더라도 한 번 기다리면 되니까 괜찮지만,
포크된 저장소인지 여부 등 정보를 추가로 얻어오려면 매번 기다려야 하는 것이 문제였다.

이 문제를 코드를 조금만 고치면서 쓸만하게 만들려고 찾아보니, 반복문으로 작성된 코드를 [제너레이터](https://en.wikipedia.org/wiki/Generator_(computer_programming))를 사용하도록 고치고
제너레이터를 다른 스레드에서 채우도록 변경하는 것이 좋아 보였다.
값을 생성하고 사용할 때에 문제가 없도록 스레드에 안전한 [큐(Queue)](https://docs.python.org/3/library/queue.html)를 사용하면 기존의 동기 코드를 크게 건드리지 않고 백그라운드에서 추가 작업을 진행할 수 있다.
이와 같은 동작을 Threaded Generator라는 이름으로 만들어놓은 [코드 조각(gist)](https://gist.github.com/everilae/9697228)이 있어,
rogrepos에서 [사용](https://github.com/lqez/rogrepos/blob/5513ea4e1b699c64d0c98c54afd8e7849c804673/rogrepos/rogrepos.py#L10-L32)했다.

rogrepos는 아래와 같이 동작하며, 메인 스레드는 사용자 입력을 기다리는 `[y/N]` 부분에서 멈추지만,
다른 스레드에서 저장소를 탐색하며 추가 정보를 계속해서 불러오므로 다음 선택지로 넘어갈 때 사용자 입장에서는 지연을 덜 느끼게 된다.

```
$ rogrepos
Retrieving organizations from GitHub...

    KeyCastr, 1 public repo(s), 0 private repo(s)
    Summernote, 12 public repo(s), 0 private repo(s)

Retrieving 122 repositories from GitHub...

97 of 122
lqez/yuna
    Description: yuna
    Updated    : 2013-11-27 16:13:40 / 1477 day(s) ago
    Size       : 100 KB
    Do you really want to delete? [y/N]: y
    This is not a forked project. Are you sure? [y/N]: y
lqez/yuna was deleted.
```

----

최초의 코드는 아래와 같았다.

    :::python
    for repo in github.get_user().get_repos():
        # do something

이를 제너레이터로 바꾸면 아래와 같이 바뀌고,

    :::python
    def generator_repos(github):
        for repo in github.get_user().get_repos():
            yield repo

    for repo in generator_repos(github):
        # do something

위에서 작성한 Threaded generator로 바꾼 것이 현재의 상태다.

    :::python
    for repo in ThreadedGenerator(generator_repos(github)):
        # do something

반복문 내에 느린 동작이 자주 포함되는 CLI 도구에서는 반복적으로 사용해볼만한 패턴이라고 생각된다.

----

덧) 위 프로젝트를 [/r/github](https://www.reddit.com/r/github/comments/7jporl/)에 올렸는데, 저장소는 지워져서는 안된다는 의견과
[`No Maintenance Intended`](https://www.reddit.com/r/github/comments/7jporl/rogrepos_remove_outdated_github_repositories_in/) 배지에 대한 댓글이 달렸다.
