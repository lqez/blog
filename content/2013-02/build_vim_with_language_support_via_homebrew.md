Title: Build vim with language support via Homebrew
Date: 2013-02-20
Lang: ko
Tags: vim, python, homebrew

Mac OS X에 기본 설치된 vim은 다른 언어를 위한 지원 옵션 없이 빌드되어, [python-mode](https://github.com/klen/python-mode) 등을 사용할 수 없다.

다행히도, Homebrew에 포함된 [vim.rb](https://github.com/mxcl/homebrew/blob/master/Library/Formula/vim.rb)는 언어 지원을 위한 옵션을 포함하고 있어, 이를 이용해 편리하게 설치가 가능하다. 아래 명령으로 지원하는 옵션을 확인할 수 있다.

    $ brew options vim

Python 지원을 포함하려면 아래와 같이 설치한다.

    $ brew install vim --with-python

vim.rb의 [25-31L](https://github.com/mxcl/homebrew/blob/master/Library/Formula/vim.rb#L25)를 보면, `--with-<language>` 옵션은 configure 시에 `--enable-<language>interp` 옵션으로 변경된다.
