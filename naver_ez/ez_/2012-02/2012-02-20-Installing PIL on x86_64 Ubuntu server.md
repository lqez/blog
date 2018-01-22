Title: Installing PIL on x86_64 Ubuntu server
Time: 11:33:00

x86_64 우분투 서버에서 pip를 통해 PIL 을 설치하면, 필요한 라이브러리가 설치되어 있음에도 불구하고, 아래와 같이 png나
jpeg를 지원할 수 없다는 결과를 보게 된다.

--------------------------------------------------------------------

*** TKINTER support not available

*** JPEG support not available

*** ZLIB (PNG/ZIP) support not available

*** FREETYPE2 support not available

*** LITTLECMS support not available

--------------------------------------------------------------------

  

이는 필요한 파일들이 /usr/lib 이 아닌 /usr/lib/x86_64-linux-gnu 에 설치되어, pip가 필요한 파일을 찾지
못하기 때문이다.

심볼릭 링크를 통해 이 문제를 해결할 수 있다.

  

아래와 같은 작업을 통해 png, jpeg, freetype을 지원하도록 PIL을 설치할 수 있다.

  

  

**# 필수 라이브러리 설치**

sudo apt-get install python-dev libpng-dev libjpeg-dev libfreetype6-dev

  

  

**# 심볼릭 링크 추가**

sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/

sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/

sudo ln -s /usr/lib/x86_64-linux-gnu/libpng.so /usr/lib/

sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/

  

  

**# pip 설치**

sudo apt-get install python-pip

  

  

**# PIL 설치**

sudo pip install PIL

  

  

**# 결과**

--------------------------------------------------------------------

*** TKINTER support not available

--- JPEG support available

--- ZLIB (PNG/ZIP) support available

--- FREETYPE2 support available

*** LITTLECMS support not available

--------------------------------------------------------------------

  

