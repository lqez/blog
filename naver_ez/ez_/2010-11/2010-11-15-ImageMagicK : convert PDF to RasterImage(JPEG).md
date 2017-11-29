Title: ImageMagicK : convert PDF to RasterImage(JPEG)
Time: 23:08:00

[http://www.imagemagick.org/](http://www.imagemagick.org/)

ImageMagicK는 다양한 벡터/래스터 이미지를 편집/변환할 수 있는 기능을 가진 Apache 2.0 라이센스의 Free-
software이다.

  

또한, 다음과 같은 프로그래밍 언어 인터페이스를 갖추고 있어, 어떠한 환경에서도 손쉽게 사용할 수 있다.

[G2F](http://www.imagemagick.org/script/api.php#ada)(Ada),[MagickCore](http://
www.imagemagick.org/script/api.php#c)(C),[MagickWand](http://www.imagemagick.o
rg/script/api.php#c)(C),[ChMagick](http://www.imagemagick.org/script/api.php#c
h)(Ch),[ImageMagickObject](http://www.imagemagick.org/script/api.php#com+)(COM
+),[Magick++](http://www.imagemagick.org/script/api.php#c++)(C++),

[JMagick](http://www.imagemagick.org/script/api.php#java)(Java),[L-Magick](htt
p://www.imagemagick.org/script/api.php#lisp)(Lisp),[NMagick](http://www.imagem
agick.org/script/api.php#neko)(Neko/haXe),[MagickNet](http://www.imagemagick.o
rg/script/api.php#dot-net)(.NET),[PascalMagick](http://www.imagemagick.org/scr
ipt/api.php#pascal)(Pascal),[PerlMagick](http://www.imagemagick.org/script/api
.php#perl)(Perl),

[MagickWand for PHP](http://www.imagemagick.org/script/api.php#php)(PHP),[IMag
ick](http://www.imagemagick.org/script/api.php#php)(PHP),[PythonMagick](http:/
/www.imagemagick.org/script/api.php#python)(Python),[RMagick](http://www.image
magick.org/script/api.php#ruby)(Ruby),
or[TclMagick](http://www.imagemagick.org/script/api.php#tcl)(Tcl/TK)

  

이 글은 콘솔 환경에서 PDF 파일을 래스터 이미지 파일로 출력하는 방법을 설명한다.

  

**ImageMagicK 설치**

debian

$ sudo apt-get install imagemagick

centos

$ yum install ImageMagicK

mac port

$ sudo port install imagemagick

거의 모든 플랫폼에서 패키지가 제공되고 있으니, 이를 활용하면 되겠다.

  

  

  

**기본 변환**

$ convert foo.pdf bar.jpg

foo.pdf의 모든 페이지를 bar-페이지번호.jpg 형식의 이름을 가진 이미지 파일로 추출한다.

  

  

**해상도 지정하기**

$convert -density 150 foo.pdf bar.jpg

높은 해상도를 가진 이미지로 추출하기 위해 -density 옵션을 사용한다. 단위는 dpi 이다.

-density가 앞에 있는 것에 유의한다. -density 값은 벡터 파일을 읽기 전에 입력되어야 한다.

  

  

**특정 페이지 지정**

$ convert -density 200 foo.pdf[10] bar.jpg

pdf문서에서 10번(11번째) 페이지만 변환한다. 페이지 번호는 0번부터 시작한다.

  

  

**페이지 범위 지정**

$ convert -density 200 foo.pdf[0-99] bar.jpg

pdf문서에서 앞에서부터 100개의 페이지만 변환한다.

  

  

**이미지 크기 지정**

$ convert foo.pdf -resize 100x100 bar.jpg

가로 세로 비율을 무시하고 가로 세로 100 픽셀의 크기를 가진 이미지로 변환한다.

  

$ convert foo.pdf -resize 100x bar.jpg

가로 100 픽셀, 세로는 비율에 맞춰 자동으로 계산된 크기를 가진 이미지로 변환한다.

  

$ convert foo.pdf -resize x100 bar.jpg

위와는 반대로 세로 100 픽셀, 가로는 비율에 맞춰 자동으로 계산된 크기를 가진 이미지로 변환한다.

  

$ convert -density 300 foo.pdf -resize 50% bar.jpg

크기를 절대값으로 지정하지 않고, 원본 이미지의 비율로 지정하는 것도 가능하다.

  

  

  

덧) 파일 이름이 bar-99.jpg, bar-101.jpg와 같이 자릿수가 맞지 않을 땐, 아래의 스크립트를 사용한다.

%05d에서 5를 원하는 자릿수로 바꾸면 된다.

> ls *.jpg | awk '{ split( $1, pre, "-" ); split( pre[2], fn, "." ); printf(
"mv \"%s\" \"%s-%05d.%s\"\n", $1, pre[1], fn[1], fn[2] ) }' | /bin/sh

추가) 위의 스크립트가 마음에 들지
않아,[http://kldp.org/node/119358](http://kldp.org/node/119358) 에 글을 남겼다.

펄로 하면 그나마 나은 듯. (aero님 제안)

> ls *.jpg | perl -nle 'system "mv $_ ".do { s/\d+/sprintf("%05d",$&)/e; $_ }'

2011-04-21 추가) 애초에 imagemagick상에서 할 수 있는 더 간단한 방법이 있어, 적어둔다. 아래와 같이 하면,
foo-00010.jpg, foo-00011.jpg 와 같이 출력해준다. 이게 제일 간단.

> $ convert -density 150 foo.pdf[10-15] foo-%05d.jpg

  

  

