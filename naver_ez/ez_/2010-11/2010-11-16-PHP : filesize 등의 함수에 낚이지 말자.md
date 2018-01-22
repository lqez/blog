Title: PHP : filesize 등의 함수에 낚이지 말자
Time: 11:09:00

filesize는 POSIX C의 _stat에 대응되는 함수로 여겨질 수 있겠지만, 내부적인 캐시를 가지고 있어 주기적으로 사용하면 잠재적인
문제를 일으킬 수 있다.

  

따라서, 주기적으로 파일 크기를 확인해야할 때에는 clearstatcache() 함수를 통해, 다음의 함수군에서 사용하는 캐시를 초기화하는
작업이 반드시 필요하다.

  

발췌: [http://php.net/manual/en/function.clearstatcache.php](http://php.net/manu
al/en/function.clearstatcache.php)

> Affected functions include stat(), lstat(), file_exists(), is_writable(),
is_readable(), is_executable(), is_file(), is_dir(), is_link(), filectime(),
fileatime(), filemtime(), fileinode(), filegroup(), fileowner(), filesize(),
filetype(), and fileperms().

