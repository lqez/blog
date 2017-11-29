Title: php : implode
Time: 17:06:00

php 내장 함수인 implode는 배열을 손쉽게 단일 값으로 바꾸어 주는 편리한 함수지만, 문자열을 합치는데 있어 다소 아쉬운 점이 있어,
implode_str이라는 함수를 만들어 즐겨 쓰고 있다.

> function implode_str( $separator, $arr, $pad = "'", $tail_pad = NULL )

{

if( $tail_pad == NULL ) $tail_pad = $pad;

>

> $res = '';

$c = count($arr);

>

> foreach( $arr as &$node )

$res .= $pad.$node.$tail_pad.((--$c>0)?$separator:NULL);

>

> return $res;

}

>

> //가능하다면 $arr대신 &$arr을 사용하는 것이 좋을 듯.

이를 이용하면, array(1,2,3,4,5)를 받아 <td>1</td>...<td>5</td>으로 손쉽게 변환할 수 있다.

SQL문에 넣을 때에도 implode_str( ',', [array], '\'' )등으로 활용할 수 있다.

