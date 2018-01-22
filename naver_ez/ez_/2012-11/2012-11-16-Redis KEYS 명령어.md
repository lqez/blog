Title: Redis KEYS 명령어
Time: 11:48:00

[@charsyam](http://twitter.com/charsyam) 님이 redis 매뉴얼에 "Don't use KEYS in your
regular application code." 라고 적혀 있다하시길래, ([링크](http://redis.io/commands/keys))

이왕 이렇게 된 거 redis 소스도 한 번 보자 싶은 기분에 클론해서 살펴봄.

KEYS 명령어는,

  * 일단 dictNext를 통해 선형으로 탐색하고,
  * stringmatchlen이라는 glob-style의 문자열 비교를 하는데, 이게 문자열 길이에 따른 O(n)의 시간 소요,
  * 일치하는 경우에 리턴값을 생성하기 위해 createStringObject 를 통해 문자열 복제를 하는데, 이 때 zmalloc 을 사용함.

  

따라서, KEYS 명령어는 해시맵 등을 통해 효과적으로 키를 찾지 않기 때문에 Production에는 사용하지 말라고 얘기하는 것 같다.

혹시나 싶어, GET 명령어도 선형 탐색을 하는 건 아니겠지 싶어 찾아보니, GET은 dict.c의 dictFind를 사용하고 있다.
(안심?-.-)

  

Redis 소스 중, db.c 에서 KEYS 명령어 부분 발췌.

> void keysCommand(redisClient *c) {

>

> dictIterator *di;

>

> dictEntry *de;

>

> sds pattern = c->argv[1]->ptr;

>

> int plen = sdslen(pattern), allkeys;

>

> unsigned long numkeys = 0;

>

> void *replylen = addDeferredMultiBulkLength(c);

>

> di = dictGetSafeIterator(c->db->dict);

>

> allkeys = (pattern[0] == '*' && pattern[1] == '\0');

>

> while((de = dictNext(di)) != NULL) {

>

> sds key = dictGetKey(de);

>

> robj *keyobj;

>

> if (allkeys || stringmatchlen(pattern,plen,key,sdslen(key),0)) {

>

> keyobj = createStringObject(key,sdslen(key));

>

> if (expireIfNeeded(c->db,keyobj) == 0) {

>

> addReplyBulk(c,keyobj);

>

> numkeys++;

>

> }

>

> decrRefCount(keyobj);

>

> }

>

> }

>

> dictReleaseIterator(di);

>

> setDeferredMultiBulkLength(c,replylen,numkeys);

>

> }

  

  

