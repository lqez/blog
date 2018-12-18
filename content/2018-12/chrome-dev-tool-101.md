Title: 크롬 개발자 도구 101
Date: 2018-12-17
Lang: ko
Slug: chrome-dev-tool-101

[썸머노트](https://github.com/summernote/summernote)를 개발하며 늘 사용하는 크롬 개발자 도구에 대해 한 번도 제대로 공부해본 적이 없었는데, 마침 아샬(@ahastudio)님이 [“아듀 2018”](https://adieu2018.ahastudio.com/)이라는 일종의 [Advent Calender](https://en.wikipedia.org/wiki/Advent_calendar)를 주최하는 것을 보고 재미있겠다 싶어 이걸 기회 삼아 크롬 개발자 도구의 기초 내용을 정리해보게 되었다.

크롬 개발자 도구에 대한 정보는 <https://developers.google.com/web/tools/chrome-devtools/> 에서 얻는 것이 가장 정확하고 빠르다. 이 글에서는 웹 서비스를 개발하는데 있어 필수적인 기본 요소만을 간략하게 소개한다.

### 개발자 도구 활성화

![Chrome menu](./images/2018-12/chrome-dev-tool-101-menu.png)
개발자 도구는 크롬 메뉴바에서 개발자 도구를 선택해서 활성화 할 수 있다. 개발자 도구의 메뉴는 왼쪽부터 차례대로 아래의 기능을 가진다.

  - 단축키: `⌘ + Shift + I` 또는 `Ctrl + Shift + I`

![Developer tool](./images/2018-12/chrome-dev-tool-101-toolbar.png)

#### 요소 선택

![Select element](./images/2018-12/chrome-dev-tool-101-select.png)
화면에서 직접 요소를 선택할 수 있다.

  - 단축키: `⌘ + Shift + C` 또는 `Ctrl + Shift + C`

#### 장치 변경

![Device toggle](./images/2018-12/chrome-dev-tool-101-device.png)
현재 크롬이 동작하는 장치가 아닌 다른 휴대 장치와 같은 화면 크기나 설정을 가지도록 변경하여 여러 환경을 테스트할 수 있도록 한다. 특히 안드로이드와 아이폰 등의 여러 모바일 장치의 값이 미리 등록되어 있어, 모바일 장치를 가정하고 테스트할 때 유용하다.

  - 단축키: `⌘ + Shift + M` 또는 `Ctrl + Shift + M`

#### 요소 (Elements)

[DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)(문서 객체 모델, The Document Object Model, 이하 DOM)을 탐색하고 CSS를 확인하며 변경할 수 있다. 주로 화면에 보이는 내용을 확인하고 편집할 때 사용한다. 화면 왼쪽의 DOM을 통해 요소를 탐색할 수 있고, 오른쪽에서는 현재 적용된 CSS 목록과 계산된(computed) 스타일, 이벤트, DOM에 설정된 중단점(breakpoint) 등을 확인할 수 있다.

선택된 요소에서 우클릭을 하면 컨텍스트 메뉴가 표시되는데, 다음의 기능은 꽤 편리하다.

![Context menu](./images/2018-12/chrome-dev-tool-101-context-menu.png)

  - **Force state**
    - 선택된 요소의 상태를 임의로 변경한다. `:active`, `:hover`, `:visited`와 같은 상태를 임의로 선택하여 버튼 위에 커서가 올라가 있을 때나 링크가 클릭된 경우 등을 가정해볼 수 있다.
  - **Break on**
    - 선택한 요소의 속성이 변경되거나, 하위 노드에 변경이 있을 경우 또는 선택된 요소가 삭제될 때에 중단점을 설정해서 확인할 수 있다. 이러한 변경사항은 자바스크립트나 콘솔에서 직접 지정하는것 보다는 이 메뉴를 통해 지정하는 것이 편리하다.
  - **Store as global variable**
    - 해당 요소를 콘솔의 변수로 만들어준다. 콘솔에서 일부 객체를 얻어 작업하기 위해 일일히 `document.querySelector()`를 입력하지 않고도 이 기능을 통해 선택된 요소를 `temp1`과 같은 변수에 할당이 가능하다.

오른쪽 윈도우에서도 다음의 기능을 알아두면 좋다.

###### 스타일 (Styles)
  - **필터** (Filter)
    ![Filter style](./images/2018-12/chrome-dev-tool-101-style-filter.png)
    - CSS 속성의 이름을 검색해볼 수 있다. 예를 들어, 검색 필터에 `margin`을 입력하면, 선택된 속성에 영향을 주는 여러 CSS 스타일에서 `margin` 값만 찾아볼 수 있다.
  - **`:hov`** (Toggle Element State)
    ![Toggle Element State](./images/2018-12/chrome-dev-tool-101-style-state.png)
    - 앞서 언급했던 `Force state`와 마찬가지로 선택된 요소의 상태를 임의로 지정할 수 있다. 
  - **`+`** (New Style Rule)
    ![New Style Rule](./images/2018-12/chrome-dev-tool-101-style-newrule.png)
    - 선택된 요소의 클래스 이름으로 스타일이 존재하지 않는다면 새로 만들어 지정할 수 있다. 소스 코드상에서 특정 선택자(selector)에 대해 스타일을 지정하지 않은 경우, 개발자 도구에서 임의로 만들어 지정해볼 때 편리하게 사용할 수 있다.

###### 스타일 계산 결과 (Computed)
![Computed style](./images/2018-12/chrome-dev-tool-101-computed.png)
선택된 요소에 적용된 최종 스타일을 확인할 수 있다. 스타일 필터와 마찬가지로 필터를 통해 원하는 스타일만 추려서 볼 수 있다. 특정 스타일을 확장하면 어떤 선택자들을 통해 최종적으로 연산된 값인지 확인할 수 있다.

#### 콘솔 (Console) 
![Console](./images/2018-12/chrome-dev-tool-101-console.png)
콘솔을 통해 페이지에 불려진 DOM과 자바스크립트와 상호 작용하며 디버깅할 수 있다. 기본 콘솔에서는 `verbose` 수준의 메세지는 표시되지 않아 출력 수준을 변경해야 볼 수 있는데, `verbose` 메세지는 개발 도구에서 유용한 내용을 알려주는 경우도 있으니 보는 것이 좋다. 좌상단의 아이콘을 선택해 사이드바를 꺼내면 콘솔 로그를 출력한 주체별로 또는 메세지 레벨별로 나눠서 볼 수 있다. 유닉스의 오래된 단축키 중 하나인 `Ctrl + L`을 이제까지의 콘솔 출력을 지우는 단축키로 사용할 수 있다.

  - **프레임** (Frames)
    ![Frame](./images/2018-12/chrome-dev-tool-101-console-frame.png)
    - 콘솔은 한 번에 하나의 프레임을 대상으로만 작동한다. 문서에 `iframe` 등으로 포함된 프레임이 추가적으로 존재하면 이 메뉴를 통해 주 프레임이 아닌 다른 프레임과 연결해 작업할 수 있다.
  - **표현식** (Expression)
    ![Expression](./images/2018-12/chrome-dev-tool-101-console-expression.png)
    - 눈 모양의 아이콘을 선택하면 일반적인 디버거에서 제공하는 Watch 기능을 사용할 수 있다. 계속해서 변화하는 값을 모니터링할 때 유용하다.
  - **필터** (Filter)
    - 다른 필터 기능과 마찬가지로, 콘솔에 출력된 내용중 지정한 필터에 해당하는 내용만 골라 볼 수 있다.
  - **경과 시간 측정**
    - [`console.time(label)`](https://developer.mozilla.org/ko/docs/Web/API/Console/time)을 통해 특정 작업이 얼마나 걸리는지 편리하게 측정할 수 있다.
    `console.timeEnd(label)`과 같이 사용하여 두 함수의 호출 사이에 얼마나 시간이 흘렀는지 확인할 수 있다.

            :::javascript
            > console.time('timer1');
            > // (... 무언가 긴 작업 ...)
            > console.timeEnd('timer1');
            timer1: 3659.787109375ms

#### 소스 (Sources)
![Source](./images/2018-12/chrome-dev-tool-101-source.png)
소스 메뉴에서는 해당 페이지에 로드된 파일들의 목록을 보며 중단점을 설정하며 본격적인 자바스크립트 디버깅이 가능하다.

  - **페이지** (Page)
    - 현재 페이지에 로드된 파일 목록을 표시한다. *기울어진* 파일 이름은 해당 파일이 컴파일된 소스로부터 [소스맵](https://developers.google.com/web/tools/chrome-devtools/javascript/source-maps)을 통해 매핑된 파일임을 나타낸다.
  - **파일 시스템** (Filesystem)
    ![Filesystem](./images/2018-12/chrome-dev-tool-101-source-filesystem.png)
    - 로컬 디스크의 소스 위치를 지정하면 현재 페이지에 로드된 파일과 매칭하여 디버깅이 가능할 뿐 아니라 바로 편집하는 것도 가능하다. 아이콘의 초록 점은 해당 소스 파일이 소스맵을 통해 매핑된 파일임을 나타낸다.
  - **코드 조각** (Snippet)
    ![Snippet](./images/2018-12/chrome-dev-tool-101-source-snippet.png)
    - [GitHub Gist](https://gist.github.com/)와 같이 코드 조각을 크롬에 저장하고 반복적으로 사용할 수 있다. 이 내용은 크롬에 연결된 사용자 별로 저장되므로 , 서로 다른 사이트에서도 같은 코드 조각 목록을 사용할 수 있다.
    - 이 내용을 크롬에 연결된 구글 계정과 동기화하여 다른 장치에서도 사용할 수 있도록 하는 기능은 아직 개발되지 않았다. [chromium/249030](https://bugs.chromium.org/p/chromium/issues/detail?id=249030)

디버거 창에서는 중단점을 설정하고, 값을 추적하는 등의 기능을 통해 효율적으로 소스 코드를 디버깅할 수 있다.
![Debugger](./images/2018-12/chrome-dev-tool-101-source-debugger.png)

  - **값 추적** (Watch)
    - 중단점에서 지정된 변수의 값을 출력한다.
  - **호출 스택** (Call Stack)
    - 현재 중단된 지점이 어떤 함수 호출을 통해 온 것인지 확인할 수 있다. 이전 스택을 선택하여 해당 호출 상황으로 돌아가 디버깅이 가능하다.
  - **범위** (Scope)
    - 지정된 범위에 포함된 변수를 확인할 수 있다. 지역 변수와 전역 변수 외에도 현재 중단점의 클로저 변수도 확인할 수 있어 유용하다.
  - **중단점** (Breakpoint)
    - 설정된 중단점의 목록을 표시한다. 체크 박스를 해제하면 일시적으로 해당 중단점을 사용하지 않게 할 수 있다. 우클릭을 통해 컨텍스트 메뉴를 호출하여 모든 중단점을 지우거나 비활성화 시키는 등의 작업을 수행할 수 있다.
  

#### 네트워크 (Network)
![Network](./images/2018-12/chrome-dev-tool-101-network.png)
페이지를 표시하는데 필요한 네트워크 작업에 대한 결과를 시간순으로 표시한다. 페이지 로드가 느리다면 이 탭을 통해 그 원인을 파악할 수 있다.

  - **캐시 사용안함** (Disable cache)
    - 캐시를 사용하지 않을 경우 어떻게 네트워크 요청이 이뤄지는지 확인해볼 수 있다.
  - **오프라인** (Offline)
    - 네트워크가 연결되지 않은 상태를 가정하여 페이지를 표시한다. 오프라인 웹 앱을 구성할 때 사용한다.
  - **트래픽 조절** (Throttling)
    ![Preset](./images/2018-12/chrome-dev-tool-101-network-preset.png)
    - 느린 네트워크 상황을 가정하여 페이지를 표시한다. `Fast 3G` / `Slow 3G` 등의 프리셋이 있으며, 원하는 속도와 지연 시간을 지정하여 사용할 수도 있다. 개발할 때 자주 이 기능을 활성화 하여 테스트 해보는 것을 추천한다.

특정 항목을 선택하여 해당 항목이 어떻게 요청되었는지, 어떤 응답을 받았는지를 상세히 확인할 수 있다. 서버에 어떤 헤더를 지정하여 요청했는지, 응답으로는 어떤 헤더를 받았는지 확인하며 네트워크 최적화를 진행하는데 유용하다.
![Request and response header](./images/2018-12/chrome-dev-tool-101-network-header.png)


#### 성능 (Performance)
![Performance](./images/2018-12/chrome-dev-tool-101-performance.png)
네트워크 탭을 통해 원격지와 어떻게 데이터를 요청하고 받았는지 확인하며 최적화를 했다면, 성능 탭에서는 자바스크립트 실행과 화면 그리기를 추적하여 어떤 부분이 웹 애플리케이션을 지연시키고 있는지 확인할 수 있다. 녹화(Record) 버튼을 누른 뒤 페이지를 로드하거나 자바스크립트 작업을 수행한 후, 정지하면 그 사이에 발생한 자바스크립트의 함수별 호출수와 사용된 시간 등을 확인할 수 있다.

타임 라인에서 구간을 선택하고 어떤 함수 호출이 가장 많은 시간을 사용했는지, 또 어떤 흐름으로 작업을 수행했는지 등을 파악할 수 있다.
![Heavist job](./images/2018-12/chrome-dev-tool-101-performance-heavist.png)


#### 애플리케이션 (Application)
![Application](./images/2018-12/chrome-dev-tool-101-application.png)
애플리케이션 탭에서는 웹 페이지가 웹 애플리케이션으로 기능하기 위해 필요한 내용들을 보여준다. 예전 웹 페이지에서는 오직 쿠키로만 정보를 저장하던 것과 달리, [다양한 웹 저장소](https://developers.google.com/web/fundamentals/instant-and-offline/web-storage/)가 추가되어 더 안전하고 빠른 형태로 정보를 읽고 쓸 수 있게 되었다.

  - **선언** (Manifest)
    - 일반적으로 `<link rel="manifest" href="/manifest.json">`로 선언된 [웹 애플리케이션과 관련된 선언](https://developer.mozilla.org/en-US/docs/Web/Manifest)을 표시한다.
  - **서비스 워커** (Service Workers)
    - 현재 페이지에서 사용중인 [서비스 워커](https://developers.google.com/web/fundamentals/primers/service-workers/) 정보를 표시한다.
  - **로컬 저장소** (Local Storage)
    - 키/값 쌍으로 손쉽게 데이터를 읽고 쓸 수 있다. 웹 브라우저마다 도메인별로 할당된 저장 공간의 크기가 다르지만 일반적으로 `10 MiB`까지 허용된다.
    - 데이터는 도메인 단위로 공유되어, 같은 브라우저 내의 서로 다른 창/탭에서도 같은 데이터를 공유할 수 있다.

            :::javascript
            localStorage.setItem('key', 'value');
            localStorage.getItem('key');
            localStorage.removeItem('key');
            localStorage.clear();

  - **세션 저장소** (Session Storage)
    - 로컬 저장소와 기능적으로는 같지만, 사용자가 명시적으로 삭제하지 않으면 지워지지 않는 로컬 저장소와는 달리, 세션 저장소는 브라우저가 닫힐 때 같이 제워진다. 
    - 로컬 저장소와 달리, 같은 도메인일 경우에도 창/탭 단위로 서로 다른 데이터를 사용하게 된다.
  - **인덱스DB** (IndexedDB)
    - 많이 사용되는 관계형 데이터베이스를 브라우저에서도 사용할 수 있다. 일반적으로 `50 MiB`이상 사용할 경우에는 사용자 동의를 필요로 한다. 이전에는 이를 위해 `WebSQL`이 있었지만 [이제는 사용되지 않는다](https://softwareengineering.stackexchange.com/questions/220254/why-is-web-sql-database-deprecated).
  - **쿠키** (Cookies)
    - 현재 페이지에서 사용 중인 쿠키 정보를 보여준다.


#### 보안 (Security)
![Security](./images/2018-12/chrome-dev-tool-101-security.png)
페이지의 인증서와 페이지에서 참조하는 도메인의 인증서 등을 검사하고 그 결과를 보여준다. 모든 사이트에 HTTPS 연결이 강조되므로 이 탭을 통해 페이지에서 참조하는 리소스에 대해서도 확인하는 것이 필요하다.


#### 감사 (Audits)
![Audits](./images/2018-12/chrome-dev-tool-101-audits.png)
[Lighthouse](https://developers.google.com/web/tools/lighthouse/)를 통한 페이지 검사 결과를 표시하고 저장할 수 있다. 기본적인 페이지의 성능과 [PWA](https://developers.google.com/web/progressive-web-apps/), [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization), [접근성](https://www.w3.org/standards/webdesign/accessibility)과 관련된 점수를 제공하므로, [Page speed](https://developers.google.com/speed/)와 함께 사용하여 품질 높은 페이지를 만드는데 참조하면 좋다. 


### 추가 기능 (More tools)
![More tools](./images/2018-12/chrome-dev-tool-101-moretools.png)
개발자 도구의 기본 탭의 오른쪽 끝 메뉴(`⋮`)를 클릭하면 추가 개발자 도구를 확인할 수 있다.

  - **도구 위치** (Dock side)
    - 개발자 도구를 별도의 창으로 분리하거나, 같은 창의 특정 위치로 보낼 수 있다.
  - **콘솔 창 보이기/숨기기** (Show/Hide console drawer)
    - 콘솔과 추가 기능을 별도로 표시하는 창을 보이거나 숨길 수 있다. 
    - 단축키: `Esc`
  - **검색** (Search)
    - 페이지를 표시하는데 쓰인 파일과 개발자 도구에 등록된 파일 시스템, 코드 조각 등의 모든 파일을 대상으로 검색을 수행한다.
  - **명령 실행** (Run command)
    ![Run command](./images/2018-12/chrome-dev-tool-101-moretools-runcommand.png)
    - 개발자 도구의 기능 목록을 보고 검색하여 실행할 수 있다.
  - **파일 열기** (Open file)
    ![Run command](./images/2018-12/chrome-dev-tool-101-moretools-openfile.png)
    - 페이지를 표시하는데 쓰인 파일과 개발자 도구에 등록된 파일 시스템, 코드 조각 등의 모든 파일을 표시하고 검색하여 파일을 열 수 있도록 한다.
  - **추가 기능** (More tools)
    - 개발자 도구의 기본 탭에 표시된 기능 외에 다른 기능들을 추가로 사용할 수 있다.

추가 기능에는 다음 항목이 있으며 각 항목에 대한 자세한 설명은 아래 목록의 링크와 [구글 크롬 개발자 도구 도움말](https://developers.google.com/web/tools/chrome-devtools/)을 참조한다.
 
  - [Animations](https://developers.google.com/web/tools/chrome-devtools/inspect-styles/animations): CSS 애니메이션을 타임라인을 따라 추적하고 캡춰할 수 있다.
  - [Changes](https://developers.google.com/web/updates/2018/01/devtools#changes): 소스 코드 변경 사항을 추적한다.
  - [Coverage](https://developers.google.com/web/updates/2017/04/devtools-release-notes#coverage): 해당 페이지에서 파일별로 얼마나 많은 부분을 실제로 사용했는지 표시.
  - JavaScript Profiler: 성능(Performance)와 유사한 기능을 제공한다.
  - [Network conditions](https://developers.google.com/web/tools/chrome-devtools/network-performance/network-conditions): 네트워크(Network)의 트래픽 조절(Throttling)과 같은 기능.
  - [Request blocking](https://developers.google.com/web/updates/2017/04/devtools-release-notes#block-requests): 패턴 매칭을 통해 특정 요청만 제한하는 테스트가 가능하다.
  - [Sensors](https://developers.google.com/web/tools/chrome-devtools/device-mode/device-input-and-sensors): 모바일 장치의 위치 정보와 가속도 센서를 에뮬레이션.
 

### 설정 (Settings)
![Settings](./images/2018-12/chrome-dev-tool-101-settings.png)
개발자 도구 자체에 대한 다양한 설정이 제공되며, 주요 기능은 다음과 같다.

  - **Appearance**
    - Theme: Light/Dark 테마를 변경할 수 있다.
    - [Show third party URL badges](https://developers.google.com/web/updates/2017/05/devtools-release-notes#badges): 네트워크 탭에서 잘 알려진 제 3자 도메인의 아이콘을 같이 표시한다.
  - **Sources**
    - Enable JavaScript source maps: 자바스크립트 소스 맵을 활성화 한다.
    - Autocompletion: 자동 완성 기능을 사용한다.
  - **Elements**
    - Show rulers: 눈금자를 표시한다.
    - Color format: 색상값을 어떻게 표시할 지 지정한다. 기본값은 `작성된 대로(As authored)`.
  - **Network**
    - Enable request blocking: 특정 요청을 제한하는 기능을 활성화 한다.
  - **Console**
    - Show timestamps: 콘솔 로그 왼쪽에 해당 출력이 일어난 시간을 표시한다.
    - Group similar: 같은 출력이 반복되는 경우, 왼쪽에 반복된 출력 회수를 표시하고 중복하여 출력하지 않는다.
    - [Eager evaluation](https://developers.google.com/web/updates/2018/05/devtools#eagerevaluation): 콘솔 명령어 입력 후, 엔터를 치기 전에 이제까지 입력된 내용을 바탕으로 미리 수행한 결과를 보여준다.
  - **Debugger**
    - Disable JavaScript: 자바스크립트를 실행하지 않는다.


이 글에서 언급된 내용은 크롬 개발자 도구의 극히 일부에 불과하므로 궁금한 내용은 항상 [구글 크롬 개발자 도구 도움말](https://developers.google.com/web/tools/chrome-devtools/)을 참조하는 것이 좋다.

마지막 팁: 개발자 도구 내에서도 `⌘ + +/-` 또는 `Ctrl + +/-`를 통해 일반 페이지와 마찬가지로 확대/축소가 가능하다.
![Zoom in Devtool](./images/2018-12/chrome-dev-tool-101-zoom.png)
