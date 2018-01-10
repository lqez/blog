Title: Python : Dict 관련 두서 없는 글
Time: 12:09:00

그간 주로 써온 PHP는 언어적으로 array와 map의 구분이 없어, Arrays 오브젝트를 다음과 같이 사용했었다. 따지고 보면 그냥
리스트가 없고, array에 대해서는 암시적으로 키를 zero-based로 할당해주는 것과 같다. (즉, 아래 예에서 $vars =
array( 0 => 'foo', 1 => 'bar' ); 가 된다 )

Array 형태

Map / Dictionary 형태

$vars = array( 'foo', 'bar' );

$vars = array( 'foo' => 'bar', 'lqez' => 'surplus' );

  

허나, Python은 언어에서 7종의 시퀀스 타입과 Set, 그리고 Dict를 모두 지원한다. (참고:[http://docs.python.o
rg/library/stdtypes.html](http://docs.python.org/library/stdtypes.html)) PHP와
비교해보면 정말 과할정도로 많아, 익히기는 어렵지만 익히고 나면 적재적소에 사용하는 매력이 있을 것 같다.

  

키와 값을 가지는 Dict를 순회하는 방법은 <strike>세 가지</strike> 다섯 가지가 있다.

키를 가져온 후, 다시 값을 가져오기

값만 가져오기

키와 값을 동시에 가져오기

for k in dict.keys():

sum = sum + dict[k]

  

# 홍민희님이 제안해주신 방법

for k in dict:

sum = sum + dict[k]

for v in dict.values():

sum = sum + v

  

# 홍민희님이 제안해주신 방법

for v in dict.itervalues():

sum = sum + v

for k,v in dict.iteritems():

sum = sum + v

  

  

허나, 파이썬 2.7 버전에서 도입된 OrderedDict 가 아니라면, 파이썬의 Dict는 입력된 순서에 맞춰 키-값 조합을 보관하지
않는다.

(2.4 ~ 2.6 버전을 위한 OrderedDict 백포트는 다음에서 찾아볼 수 있다 :[http://code.activestate.com
/recipes/576693/](http://code.activestate.com/recipes/576693/))

순서대로 출력되지 않는 Dict

sorted 함수를 통해 정렬해서 출력하기

dict= {}

  
dict['apple']='This is an apple.'

dict['orange']='This is an orange.'

dict['banana']='That is a banana.'

  
forkindict.keys():

printdict[k]

dict= {}

  
dict['apple']='This is an apple.'

dict['orange']='This is an orange.'

dict['banana']='That is a banana.'

  
forkinsorted(dict.keys()):

printdict[k]

This is an orange.

This is an apple.

That is a banana.

This is an apple.

That is a banana.

This is an orange.

  

  

  

  

**실험**

Dict를 순회하는 속도를 측정하기 위해 다음의 데이터를 준비한다.

  * 하드웨어 환경 : Macbook Pro 13" mid-2010 / Intel Core 2 Duo 2.4Ghz

소프트웨어 환경 : Mac OS X 10.6 / Python 2.6

  * 데이터
    * 백만 개의 키-값 조합이 들어있는 Dict
    * 백만 개의 값이 들어있는 List  

  

1차

2차

3차

평균

List 대비

List

0.080682

0.081702

0.078514

0.08030

100

dict.iteritems()

0.156956

0.154061

0.154906

0.15531

193

sorted(dict.iteritems())

3.298344

3.333042

3.226044

3.28581

4092

dict.keys()

0.168049

0.168540

0.163370

0.16665

208

sorted(dict.keys())

0.293548

0.293534

0.287409

0.29150

363

dict.values()

0.160950

0.161102

0.156514

0.15952

199

  

가장 빠를 것으로 예상되는 List와 비교해 각 방식의 속도를 측정해보았다.

특이한 것은 sorted(...)의 결과인데, dict.iteritems()를 정렬해서 값을 가져올 경우가 List 대비 40배나 느리다.

(첨부 파일 참조)

  

**2011.11.04 재실험**

Dict를 순회하는 속도를 측정하기 위해 다음의 데이터를 준비한다.

  * 하드웨어 환경 : Macbook Air 11" late-2010 / Intel Core 2 Duo 1.4Ghz

소프트웨어 환경 : Mac OS X 10.7 / Python 2.7

  * 데이터
    * 백만 개의 키-값 조합이 들어있는 Dict
    * 백만 개의 값이 들어있는 List  

  

1차

2차

3차

평균

List 대비

List

0.143053

0.140797

0.14658

0.143477

100

dict.iteritems()

0.338968

0.324415

0.336775

0.333386

232

sorted(dict.iteritems())

1.310241

1.199754

1.221143

1.243713

867

dict.keys()

0.249128

0.258532

0.253958

0.253873

177

sorted(dict.keys())

0.412872

0.412485

0.415573

0.413643

288

dict.values()

0.233161

0.236768

0.239946

0.236625

165

dict

0.146412

0.149717

0.149587

0.148572

104

dict.itervalues()

0.147343

0.14861

0.156398

0.150784

105

sorted(dict)

0.314669

0.313033

0.320005

0.315902

220

  

  

  

**결론**

  * 키 - 값 조합으로 쓸 것이 아니라면 역시 리스트가 빠르다.
  * 입력된 순서를 유지하고 싶으면 OrderedDict 를 사용한다.
  * 정렬된 순서로 순회하고 싶으면, iteritems()를 정렬하지 말고, keys()의 결과를 정렬하는 것이 훨씬 빠르다.
  * keys()나 values()는 리스트를 생성하여 리턴하는 함수이므로, 그냥 dict 자체나 dict.itervalues()를 쓰는 것이 빠르다. ( 홍민희님 댓글에서 참조 )
  * iteritems(), keys(), values()의 속도는 모두 비슷하다.

  

# 2011.11.04 수정

더 나은 방법을 제안해주신 홍민희([@hongminhee](http://twitter.com/#!/hongminhee))님에게 감사드립니다.

  

