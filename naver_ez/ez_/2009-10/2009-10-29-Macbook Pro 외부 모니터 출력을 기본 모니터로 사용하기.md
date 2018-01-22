Title: Macbook Pro 외부 모니터 출력을 기본 모니터로 사용하기
Time: 14:13:00

유니바디 Macbook Pro에서기본 제공되는 부트캠프 드라이버로는, 이전 MBP와는 다르게 외부 모니터를 기본 모니터로 설정할 수가없었다.

이를 해결하기 위해서는 아래의 레지스트리 값을 추가해야 한다.

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Video{...}\0000

보통 2~5개의 Video 장치가 설정되어 있으므로, 현재 사용중인 디스플레이 어댑터를 찾아야 한다.

그 안에 아래와 같은 두 개의키를 추가한다.

"DualViewAllow2ndViewAsPrimary"=dword:00000001

"DualViewMobile"=dword:00000002

재시작 후에 외장 모니터를 기본 모니터로 선택할 수 있게 된다.

