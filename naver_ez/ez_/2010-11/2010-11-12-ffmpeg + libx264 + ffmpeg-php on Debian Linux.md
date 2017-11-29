Title: ffmpeg + libx264 + ffmpeg-php on Debian Linux
Time: 09:29:00

우연한 기회에 ffmpeg + ilbx264 + ffmpeg-php를 통해 트랜스코더를 만들 일이 생겨 그 과정에서 생긴 일들을 적어본다.

일단, 데비안에서 위의 조합을 구현하다 보면, 보통 아래와 같은 길을 따르게 된다.

  

- 데비안 공식 stable/unstable/testing 패키징에는 h.264 free encoder인 libx264가 포함되어 있지 않다.

- 이를 해결하기 위해http://debian-multimedia.org/ 의 패키지를 apt list에 추가하여 최신 ffmpeg + libx264 를 설치한다.

- 하지만, 해당 패키지 제공자에서 ffmpeg-php를 제공하고 있지 않아, 결국 모든 것을 직접 빌드하는 방법 밖에는 없다.

- 직접 빌드해서 실행해도, swscaler가 포함된 ffmpeg는 ffmpeg-php와 호환되지 않아, 소스를 일부 수정해야 한다.

  

  

  

**1. ffmpeg + libx264 설치**

[http://www.adminsehow.com/2009/07/how-to-install-ffmpeg-on-debian-lenny-from-
svn/](http://www.adminsehow.com/2009/07/how-to-install-ffmpeg-on-debian-lenny-
from-svn/)

  

위 페이지는 checkinstall을 통한 설치 안내를 제공하기 때문에, 필요한 경우 얼마든지 이전 상태로 돌아갈 수 있다.

  

절차 중, libtheora는 theora코덱을 사용하기 위한 것으로, 필요 없다면 생략하고, --enable-theora 를 생략한다

또한, 현 시점에서는 ffmpeg에서 AAC 디코더인 FAAD에 대한 대응이 없으므로, --enable-libfaad 를 생략한다.

ffmpeg-php는 ffmpeg에 대한 shared library를 요구하므로, --enable-shared 옵션을 반드시 추가한다.

  

빌드 및 설치가 종료된 이후에 ffmpeg를 그냥 실행해, 올바르게 설치가 되었는지 확인한다.

  

  

**2. ffmpeg-php 설치**

[http://ffmpeg-php.sourceforge.net/](http://ffmpeg-php.sourceforge.net/)

해당 페이지의 설치 도움말을 통해 소스를 다운받아 압축을 해제한다.

압축을 해제한 이후에는, 아래 링크의 내용을 통해 ffmpeg-php.c의 소스를 반드시 수정한다.

[http://minseop.com/52](http://minseop.com/52)

  

소스 수정 후, 아래의 명령어들을 실행하여 빌드 후 설치한다. phpize가 없다면, sudo apt-get install phpize로
설치한다.

$ phpize

$ ./configure

$ make

$ checkinstall --pkgname=php5-ffmpeg --pkgversion "4:0.6.0" --backup=no
--default

(pkgversion엔 무조건 0.6.0을 기입하는 대신 다운로드 받은 소스의 버전을 적도록 한다)

  

빌드 및 설치가 종료된 이후에는 아래의 php소스로 동영상의 첫 프레임을 저장하는 테스트를 진행한다.

$src_path : 동영상 파일의 이름

$dst_path : 저장될 이미지 파일의 이름

  

> <?php

>

> $src_path = "some movie.mov";

>

> $dst_path = "some picture.png";

>

>

>

> $mov = new ffmpeg_movie( $src_path, false );

>

> $frame = $mov->getFrame( 0 );

>

> if( $frame )

>

> {

>

> $gd = $frame->toGDImage();

>

> imagepng( $gd, $dst_path );

>

> }

>

> ?>

ffmpeg-php의 빌드나 테스트에 문제가 발생한다면, /usr/lib/i686/cmov 디렉터리에 기존 데비안 패키지로 설치했던
ffmpeg 라이브러리들이 남아있는지 확인한다. 해당 라이브러리들이 남아 있다면, cmov 디렉터리를 다른 디렉터리로 옮긴 후 다시 테스트를
진행해본다.

  

  
추가적으로, ffmpeg를 사용하다가 생길 수 있는 문제도 아래 링크에 정리해보았다.

[http://blog.naver.com/ez_/140117973968](http://blog.naver.com/ez_/14011797396
8)

