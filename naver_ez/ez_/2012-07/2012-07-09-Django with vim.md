Title: Django with vim
Time: 01:58:00

Django 개발을 위한 에디터로 vim을 주로 사용하고 있다.

하드코어하게 vim을 설정해서 사용하는 사람도 있긴 한데, 나는 험악하게(...) 설정하진 않고 그냥 ctags 만들어서 쓰는 정도.

  

Django 위키에는 Django 개발에 편리하도록 vim을 설정하는 방법에 대한 안내가 있으니 궁금하신 분은 살펴보면 되겠다.

링크 : [https://code.djangoproject.com/wiki/UsingVimWithDjango](https://code.dja
ngoproject.com/wiki/UsingVimWithDjango)

  

  

vimrc

  

Django 위키에서 참고하여, 내가 자주 쓰는 것들만 추려 숏컷을 만들어보았다.

링크 : [https://gist.github.com/3071726](https://gist.github.com/3071726)

  

자신의 vimrc에 위 내용을 포함하면, 다음과 같은 동작이 가능해진다. (이 글을 읽는 사람이라면 자신의 vimrc 위치를 모를리가
없겠지... )

  * \m : 현재 앱의 models.py 열기
  * \v : 현재 앱의 views.py 열기
  * \u : 현재 앱의 urls.py 열기
  * \a : 현재 앱의 admins.py 열기
  * \t : 현재 앱의 templates 디렉토리 열기
  * \T : 프로젝트 루트의 templates 디렉토리 열기
  * \S :프로젝트 루트의settings.py 열기
  * \U : 프로젝트 루트의 urls.py 열기

  

  

  

ctags

  

vim에는 tag 파일을 읽어, 문자 기반으로 함수나 상수 등이 정의되어 있는 위치로 점프하는 기능이 있다.

이 tag 파일을 생성하기 위한 도구가 바로 ctags.

  

Mac OS X에 내장된 ctags 는 평소에 쓰던 ctags 와는 달라, brew로 별도 설치하여 사용하고 있다.

brew 사용자라면 brew install ctags 로 간단하게 설치 가능.

  

이후에 아래의 명령어를 통해 현재의 Django project와 사용중인 virtualenv의 패키지들에 대한 tag를 만들 수 있다.

> $ ctags -R -f <django_project_path> <your_virtualenv_path>

예를 들면, 아래와 같다.

> $ ctags -R -f . ~/VirtualEnvs/comico

위 명령어를 실행하면 실행한 위치에 tags 파일이 생성되는데, 이 파일이 있는 위치에서 vim을 실행해야 해당 tag 파일을 사용할 수
있다.

이것이 귀찮으면 tags 파일을 임의의 위치에 놔두고 vimrc에 tag 파일의 위치를 추가 지정해줘도 사용 가능.

> set tags+=<tag file1>,<tag file2>,...

tag를 설정한 이후에는 함수나 상수의 이름 위에서 Ctrl + ] 로 이동, Ctrl + t 로 원래 위치로 돌아오는 것이 가능한다.

자세한 사용법은 다음 링크를 참고.

링크 :[http://sosal.tistory.com/11](http://sosal.tistory.com/11)

  

