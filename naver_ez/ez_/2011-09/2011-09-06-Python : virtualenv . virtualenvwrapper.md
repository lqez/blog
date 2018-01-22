Title: Python : virtualenv / virtualenvwrapper
Time: 14:45:00

파이썬을 업무에 본격적으로사용하게 된지 겨우 1년.

파이썬의 언어적인 면에 대해서는 여전히 무지하지만(여전히 stdtypes들의 용법을 찾아 헤맴), 파이썬 기반의 프레임워크들을 쓰기
시작하면서, 좋은 개발 환경에 대한 필요는 늘 있어왔다.

  

brew, port 나 apt-get 으로 설치하는 사이트 패키지와 소스를 직접 받아 설치하는 것들. 그리고 easy_install과
pip의 짬뽕 속에 개발 환경은 늘 누더기가 되어왔다.

  

허나, 최근에 도입한 아래 두 개의 도구를 통해 파이썬 개발 환경을 보다 편리하게 관리할 수 있게 되었다.

  * virtualenv :[http://pypi.python.org/pypi/virtualenv](http://pypi.python.org/pypi/virtualenv)
  * virtualenvwrapper :[http://pypi.python.org/pypi/virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper)

파이썬은 프레임워크나 라이브러리들을 버전별 파이썬 디렉터리 이하의site-packages 경로에 일괄적으로 관리하는 문제점이 있어, 의존성
많은 여러 프로젝트를 동시에 진행하다 보면 라이브러리/프레임워크 버전간 충돌에 따른 문제가 필연적으로 발생하는데, virtualenv를 통해
이런 문제를 해결할 수 있으며, 이것을 더욱 쉽게 사용하게 도와주는 툴킷이 virtualenvwrapper다.

  

이 글에서는 virtualenv를 보다 편리하게 사용할 수 있도록 해주는 도구의 집합인 virtualenvwrapper에 대해서 알아본다.

  

  

Installation

**  
**

pip는 easy_install의 대체품으로virtualenv 및 virtualenvwrapper를 설치하기 위해서는 pip의 설치가
선행되어야한다. pip는 easy_install 보단 (외형적으로나마) 향상된 패키지 설치 및 관리를 가능하게 한다. pip는 다음의 경로를
통해 받아 설치할 수 있다.[http://pypi.python.org/pypi/pip#downloads](http://pypi.python.
org/pypi/pip#downloads)

  

pip를 설치한 후에는 아래의 명령어로 간단히 두 패키지를 설치할 수 있다. (virtualenv는 의존성 검사를 통해 자동으로 설치된다)

> $ sudo pip install virtualenvwrapper

**  
**

Configuration

**  
**

virtualenvwrapper를 사용하기 위해서, 파이썬 가상 환경을 저장할 디렉터리를 지정해야 한다. 앞으로 생성할 가상 환경은 이
디렉터리의 하위 디렉터리로 생성된다.

> $ export WORKON_HOME=~/VirtualEnvs

>

> $ mkdir -p $WORKON_HOME

>

> $source /usr/local/bin/virtualenvwrapper.sh

사용하는 쉘 기동 스크립트에 WORKON_HOME이나 source 작업 등을 기업해, 다음 번 쉘 실행시에 편리하게 사용할 수 있도록 한다.
홈 디렉터리의 .profile 등에 위의 내용을 동일하게 기입한다.

> export WORKON_HOME=~/VirtualEnvs

>

> source /usr/local/bin/virtualenvwrapper.sh

Usage

**  
**

mkvirtualenv 명령어 뒤에 생성할 가상 환경의 이름을 입력한다.

> $ mkvirtualenv test

위 명령을 입력하면, 아래와 같이 가상 환경을 구성하고, 가상 환경으로 진입하게 된다. ( 프롬프트 앞의 (test)로 확인 가능 )

> New python executable in test/bin/python

>

> Installing setuptools............done.

>

> Installing pip...............done.

>

> virtualenvwrapper.user_scripts creating
/Users/lqez/VirtualEnvs/test/bin/predeactivate

>

> virtualenvwrapper.user_scripts creating
/Users/lqez/VirtualEnvs/test/bin/postdeactivate

>

> virtualenvwrapper.user_scripts creating
/Users/lqez/VirtualEnvs/test/bin/preactivate

>

> virtualenvwrapper.user_scripts creating
/Users/lqez/VirtualEnvs/test/bin/postactivate

>

> virtualenvwrapper.user_scripts creating
/Users/lqez/VirtualEnvs/test/bin/get_env_details

>

> (test)$

이 상태에서 pip로 패키지를 설치하면, 해당 환경 내에서 사용할 수 있도록 설치된다.

> (test)$ pip install django

이후에 다시 해당 환경에 진입하기 위해서는 workon 명령어를 사용한다. workon 명령어 입력 후 tab을 입력하면 사용할 수 있는
가상 환경의 목록이 자동 완성되는 것도 장점. 사용중이던 가상 환경에서 나오기 위해서는 deactivate 명령어를 사용한다.

> $ workon (tab 입력)

>

> test test1 test2 (이미 생성된 가상 환경의 리스트가 표시된다 )

>

> $ workon test

>

> (test)$

>

> ...

>

> (test)$ deactivate

>

> $

라이브러리 외에, 여러 버전의 파이썬이 설치되어 있을 때, 특정 버전을 사용해야할 때가 있다. 이 때, --python 옵션을 통해 파이썬
버전을 지정할 수 있다. 아래는 2.6 버전을 지정하여 설치하는 경우를 보여준다.

> $ mkvirtualenv --python=python2.6 test2

>

> Running virtualenv with interpreter /usr/bin/python2.6

>

> New python executable in test2/bin/python2.6

>

> Also creating executable in test2/bin/python

명령어에 대한 더 많은 도움말은[http://www.doughellmann.com/docs/virtualenvwrapper/command_r
ef.html](http://www.doughellmann.com/docs/virtualenvwrapper/command_ref.html)
를 참조한다.

  

  

