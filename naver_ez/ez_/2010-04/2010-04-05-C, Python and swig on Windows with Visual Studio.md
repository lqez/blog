Title: C, Python and swig on Windows with Visual Studio
Time: 18:12:00

wxWidget으로 npk(http://npk.googlecode.com)의 GUI 프론트엔드를 만들려다, 우회적인 접근 방법을 선택하였다.
wxWidget을 직접 쓰는 대신에 npk의 Python extension을 만들고, wxPython을 쓰는 것인데, 이쪽이 시간도 덜
걸리고 Python을 제대로 배워보고자 하는 시점에서 선택할 수 있는 좋은 카드라 생각된다.

  

C/C++ 코드를 Python extension으로 직접 변환하려면 아무래도 손이 많이 가기 마련인데, 직접 하는 대신
swig(http://www.swig.org)를 사용하면 수월하게 작업할 수 있다. 인터넷에 swig를 통해 C/C++코드를 다른 언어로
쓰는 예제([http://www.swig.org/tutorial.html](http://www.swig.org/tutorial.html))가
많이 있지만, Windows 플랫폼에서 Visual Studio를 통해 작업하는 방법을 for dummies 수준으로 제시한 문서는 많지
않아, 예제를 따라하는 과정을 한 번 적어보고자 한다.

  

**(1) 준비사항**

Visual Studio(C++), swig, python

* swig와 python은 설치한 후에 PATH에 등록하여두면 사용하기에 편리하다.

  

**(2) 예제 파일 작성**

아래 파일을 작성하여 example.c로 저장한다.

> /* File : example.c */

  
#include <time.h>

double My_variable = 3.0;

  
int fact(int n) {

if (n <= 1) return 1;

else return n*fact(n-1);

}

  
int my_mod(int x, int y) {

return (x%y);

}

  
char *get_time()

{

time_t ltime;

time(&ltime);

return ctime(&ltime);

}

**(3) 인터페이스 파일 작성**

swig를 위한 인터페이스 파일을 작성한다.

> /* example.i */

%module example

%{

/* Put header files here or function declarations like below */

extern double My_variable;

extern int fact(int n);

extern int my_mod(int x, int y);

extern char *get_time();

%}

  
extern double My_variable;

extern int fact(int n);

extern int my_mod(int x, int y);

extern char *get_time();

원문에서도 나와 있지만, 만약 example.c에 대한 헤더 파일(예:example.h)이 존재한다면, 해당 파일을 이용하여 인터페이스
파일을 보다 간략하게 만들 수 있다.

> %module example

%{

/* Includes the header in the wrapper code */

#include "example.h"

%}

  
/* Parse the header file to generate wrappers */

%include "example.h"

  

**(4) swig를 통해 wrapper와 py파일 생성**

커맨드창(cmd)를 통해 아래의 명령을 수행하면 해당 인터페이스에 대응하는 wrapper와 py파일이 생성된다. 파일 이름이
example.c 였다면, example_wrap.c파일과 example.py 파일이 생성된다.

> > swig -python example.i

  

**(5) Visual Studio로 DLL 생성**

python을 직접 빌드할 생각이라면 static library로 만들어, 링크할 때 넣을 수도 있겠지만, dynamic library로
생성하여 import 후 사용하는 것이 일반적이다.

- Visual Studio의 메뉴 File > New > Project를 통해 새로운 프로젝트를 생성하는데, 이때 project type을 Visual C++ > Win32 > Win32 Project > DLL로 생성하도록 한다. 프로젝트 명은 되도록 모듈명과 일치시켜, 혼란이 없도록 하는 것이 좋다.

- 프로젝트가 생성되면 example.c와 example_wrap.c를 프로젝트에 포함시킨다.

- 프로젝트 빌드 타겟을 release로 바꾼다. debug빌드를 위해서는 Python의 debug 라이브러리가 필요한데, binary 배포판에는 포함되어 있지 않기 때문이다.

- 프로젝트 등록정보(properties)의 C/C++ > General > Additional Include Directories에 Python 설치 디렉터리의 include 디렉터리를 지정한다. ( 예: C:\Python26\include )

- Linker > Input > Additional Dependencies에 Python 라이브러리를 지정한다. ( 예: C:\Python26\libs\python.lib )

- 빌드한 후, Release디렉터리 내에 example.dll이 생성된 것을 확인한다.

  

**(6) 모듈로 사용하기**

우선, example.dll의 이름을 _example.pyd로 변경한다. 그리고 이 파일과 함께 (4)에서 생성했던 example.py을
Python이 설치된 디렉터리의 Lib\site-packages로 복사한다. 전역으로 사용하지 않을거라면, 두 개 파일을 사용하고자 하는
위치로 복사해야 한다.

  

Python 쉘을 실행시키고, 아래와 같이 사용해본다.

> >>> import example

>>> example.fact(5)

120

>>> example.my_mod(7,3)

1

>>> example.get_time()

'Sun Feb 11 23:01:07 1996'

>>>

  

이제 걸음마를 시작했으니, 언제쯤 npk를 래핑해서 GUI 툴을 만들 수 있을지... 과거에 WTL로 작업했던 것이 좀 후회된다. 진작
옳은(좋은게 아니고 옳은) 방법을 선택했다면 좋았을 텐데.

  

  

  

  

