Title: Using wxwidget on Visual C++
Time: 22:18:00

Visual C++에서의 wxwidget 사용하기.

일단은 [http://wiki.wxwidgets.org/Microsoft_Visual_C%2B%2B_Guide](http://wiki.wxw
idgets.org/Microsoft_Visual_C%2B%2B_Guide)이곳을 참조.

다른 플랫폼에서의 빌드도 해당 위키에서 확인할 수 있다.

(1) wxwidget을 다운받아, wxWidgets\build\msw 의 wx.dsw나 wx_dll.dsw를 연다. Visual C++
6.0 부터 지원하므로, dsw/dsp로 제공되지만, 상위 버전으로의 컨버팅에 문제는 없다. 기본적으로 양쪽 모두 static/shared
library에 대한설정이 포함되어 있지만, 애초에 사용하고자 하는 형태의 솔루션을 선택하여 사용하는 것이 좋다.

(2) 주의할 것은, wxwidget의 wx.dsw에 포함된 모든 프로젝트가 Code generation을 Multi-threaded DLL
( Debug DLL )을 사용하고 있다는 점이다. Unicode/Multibyte - Debug/Release -
Shared/Static은 쪼개져 있지만, Code generation은 어쩌하지 못한 듯. 미리 바꿔서 빌드해야 한다.

(3) 컴파일러의 Preprocessor에 다음을 등록 : __WXMSW__ ( debug모드일 경우는 __WXDEBUG__ )

(4) 컴파일러의 General > Additional Include Directories 에 $(WXWIN)\include,
$(WXWIN)\include\msvc 을등록. Visual Studio IDE의 환경 설정에서 WXWIN을 등록하거나, 위의 디렉터리를
Tool> Options > VC++ Directories의 Include path에 추가해도 된다.

(5) 링커의 General > Additional LibraryDirectories에 $(WXWIN)\lib\vc_lib나
$(WXWIN)\lib\vc_dll을 static/shared library 여부에 따라등록한다. 또는 (4)와 같이 Tool >
Options > VC++ Directories의 Library path에 추가해도 된다.

(6) 링커의 Input > Additional Depedencies 에 comctl32.lib rpcrt4.lib winmm.lib
advapi32.lib wsock32.lib 를 등록한다. comctl32.lib와 rpcrt4.lib는 필수 사항이고, 나머지는 라이브러리
사용 정도에 따라 등록한다. 설명에는 wxmsw28_core.lib와wxbase28.lib를 등록해야 한다고 하지만, 실제로는 wx
header파일에 의해 기본적으로 지정되어 있으므로, 생략 가능하다. (해당 라이브러리 이름은 unicode / debug 에 따라 이름이
달라지므로 적절히 지정)

(7) 아래 코드를코드 상단에 추가한다.

> #include "wx/wxprec.h"

>

> #ifndef WX_PRECOMP

#include "wx/wx.h"

#endif

(8) 예제 코드를 작성하고 빌드.

