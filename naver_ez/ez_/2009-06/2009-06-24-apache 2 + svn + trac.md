Title: apache 2 + svn + trac
Time: 02:01:00

회사 프로젝트건 개인 프로젝트건 보통 svn에 trac을 같이 쓰는 편인데,

여러 리포지터리+여러 트랙환경에 인증 과정이 포함되면 중복되는 구문들이 생겼었다.

이를 해결하기 위해 LocationMatch를 써보았는데, 맘에 쏙 들지는 않지만 중복을 좀 줄일 수 있게 된다.

> <Location /svn>

DAV svn

SVNParentPath /home/users/studio/svn

</Location>

>

> <Location /trac>

SetHandler mod_python

PythonInterpreter main_interpreter

PythonHandler trac.web.modpython_frontend

PythonOption TracEnvParentDir /home/users/studio/trac

PythonOption TracUriRoot /trac

</Location>

>

> <LocationMatch **/[(trac)|(svn)]+/fleet**>

AuthType Basic

AuthName "fleet.studio.amiryo"

AuthUserFile /home/users/studio/passwd.svn.fleet

Require valid-user

</LocationMatch>

우선 svn과 trac서비스를 parent 레벨에서 처리하도록 하고, LocationMatch 지시어를 통해 인증을 하나로 통합하였다.

