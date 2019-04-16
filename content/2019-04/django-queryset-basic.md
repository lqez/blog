Title: Django QuerySet 기능 간단하게 살펴보기
Date: 2019-04-17
Lang: ko
Slug: django-queryset-basic

[Django QuerySet](https://docs.djangoproject.com/en/2.2/ref/models/querysets/)를
이용해 데이터베이스의 값을 묶어 합을 내거나 숫자를 세는 등의 작업을 수행할 수 있다.

학생들의 시험 점수 기록을 바탕으로, QuerySet의 한계와 문제 해결 과정을 알아보자.

```Python
class Score(models.Model):
    student_id = models.CharField(max_length=50, help_text="학생 번호")
    student_name = models.CharField(max_length=50, help_text="학생 이름")
    subject_name = models.CharField(max_length=40, help_text="과목 이름")
    score = models.IntegerField(help_text="시험 성적")
```

위와 같은 모델이 있다고 할 때, 모든 기록을 가져오는 것은 쉽다.

```Python
qs = Score.objects.all()

for row in qs.values_list():
    print(row)

# 실행 결과
(1, '10001', '관우', '봉술', 100)
(2, '10001', '관우', '성악', 25)
(3, '10002', '장비', '봉술', 95)
(4, '10002', '장비', '음주', 100)
(5, '10003', '유비', '봉술', 10)
(6, '10003', '유비', '음주', 25)
```

### Aggregate

전체 시험 성적을 대상으로 최고 점수나 평균 점수를 구하는 것은
[`aggregate`](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/)로 가능하다.

```Python
>>> from django.db.models import Avg, Max
>>> Score.objects.aggregate(Avg('score'))
{'score__avg': 59.166666666666664}
>>> Score.objects.aggregate(Max('score'))
{'score__max': 100}
```

특정 과목에 대한 평균을 구할 때는 [`filter`](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#filter)를 사용한다.

```Python
>>> from django.db.models import Avg
>>> Score.objects.filter(subject_name='봉술').aggregate(Avg('score'))
{'score__avg': 68.33333333333333}
```

그럼 과목별 평균을 구하고 싶을 때는 어떻게 해야할까?
위 쿼리에서 `filter` 부분을 모든 과목으로 바꿔가며 확인할 수도 있겠지만, `annotate` 기능을 사용하면 간단하게 해결할 수 있다.


### Annotate

과목별 최고 점수를 구하기 위해서는 [`values`](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#values)와
[`annotate`](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#annotate)를 섞어 사용한다.

```Python
from django.db.models import Avg
qs = Score.objects.values('subject_text') \
                  .annotate(Avg('score'))

for row in qs:
    print(row)

# 실행 결과
{'subject_name': '봉술', 'score__avg': 68.33333333333333}
{'subject_name': '성악', 'score__avg': 25.0}
{'subject_name': '음주', 'score__avg': 62.5}
```

위에서 QuerySet으로 수행한 것을 대략적인 SQL 문법으로 옮겨보면 다음과 같다.

```SQL
SELECT subject_name, AVG(score) FROM ScoreTable
    GROUP BY subject_name
```

`annotate`는 수행될 때 `values`로 지정된 필드를 SQL의 [`GROUP BY`](https://dev.mysql.com/doc/mysql/en/group-by-modifiers.html)로 전달하여, 해당 필드끼리 묶은 결과를 구한다.
과목별 최고 점수를 가진 사람을 구하는 과정을 통해 `annotate`의 한계를 확인해보자.

```Python
from django.db.models import Max
qs = Score.objects.values('subject_text') \
                  .annotate(Max('score'))

for row in qs:
    print(row)

# 실행 결과
{'subject_name': '봉술', 'score__max': 100}
{'subject_name': '성악', 'score__max': 25}
{'subject_name': '음주', 'score__max': 100}
```

### Problem

최고 점수를 낸 사람을 같이 보고 싶은 경우에는 어떻게 해야할까? `values`에 학생 이름을 추가로 넣으면 의도한 결과가 나오지 않는다.

```Python
from django.db.models import Max
qs = Score.objects.values('subject_text', 'student_name') \
                  .annotate(Max('score'))

for row in qs:
    print(row)

# 실행 결과
{'subject_name': '봉술', 'student_name': '관우', 'score__max': 100}
{'subject_name': '봉술', 'student_name': '유비', 'score__max': 10}
{'subject_name': '봉술', 'student_name': '장비', 'score__max': 95}
{'subject_name': '성악', 'student_name': '관우', 'score__max': 25}
{'subject_name': '음주', 'student_name': '유비', 'score__max': 25}
{'subject_name': '음주', 'student_name': '장비', 'score__max': 100}
```

왜 이런 결과가 나왔을까? 작성된 SQL문을 보면 그 이유를 알 수 있다.

```SQL
SELECT subject_name, student_name, MAX(score) FROM ScoreTable
    GROUP BY subject_name, student_name
```

그렇다면 `values`를 `annotate` 뒤에 추가로 놓으면 결과가 달라질까?

```Python
from django.db.models import Max
qs = Score.objects.values('subject_text') \
                  .annotate(Max('score')) \
                  .values('subject_text', 'student_name', 'score__max')

for row in qs:
    print(row)

{'subject_name': '봉술', 'student_name': '관우', 'score__max': 100}
{'subject_name': '봉술', 'student_name': '유비', 'score__max': 10}
{'subject_name': '봉술', 'student_name': '장비', 'score__max': 95}
{'subject_name': '성악', 'student_name': '관우', 'score__max': 25}
{'subject_name': '음주', 'student_name': '유비', 'score__max': 25}
{'subject_name': '음주', 'student_name': '장비', 'score__max': 100}
```

결과는 그대로다. `annotate`와 `values` 구문은 배치된 순서에 따라 작동이 달라지는데,
`values`가 `annotate`보다 앞서 있는 경우는 앞선 예제에서와 같이 결과를 묶는데 사용된다.
하지만 `annotate`가 앞선 반대 경우에는 전체 쿼리셋에 대해 annotation이 적용된다.
즉, 이 경우에 `values`는 결과를 묶는데 사용되지 않고, 어떤 필드를 출력하는지만 결정하게 된다.

* [Order of annotate() and values() clauses](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#order-of-annotate-and-values-clauses)

이는 SQL의 오래된 문제와도 같다. 과목별 최고 점수를 얻은 학생은 사실 한 명이 아니라 더 있을 수도 있다.
예제에서도 만약 `장비`의 봉술 점수가 95점이 아니라 100점이었다면, 최고 점수를 획득한 사람으로 `관우`와 `장비` 중 누굴 출력해야 할까?
엄격한 룰을 가진 데이터베이스 엔진에서는 아래와 같은 SQL을 수행하지 않고 에러를 출력할 것이다.

```SQL
/* 비결정적인 애매한 쿼리 */
SELECT subject_name, student_name, MAX(score) FROM ScoreTable
    GROUP BY subject_name
```

* [Select first row in each GROUP BY group?](https://stackoverflow.com/questions/3800551/select-first-row-in-each-group-by-group) 
* [Get records with highest/smallest whatever per group](https://stackoverflow.com/questions/8748986/get-records-with-highest-smallest-whatever-per-group)

하지만 MySQL과 같은 대중적인 데이터베이스에서도 이런 애매한 구문이 문제 없이 수행되는 경우가 많다 보니,
이런 경우를 Django ORM에서 적당히 처리하지 못하는 것에 대해 불편하다고 느낄 수도 있다.


### Solution

#### Loop

첫번째 방법은 과목별 최고 점수를 구한 뒤, 각 결과를 순회하며 해당 과목의 해당 점수를 가진 결과 중,
가장 첫번째 결과에 해당하는 값을 추가로 넣는 방법이다.
직관적으로 이해할 수 있는 쉬운 코드이지만, 과목별로 쿼리를 추가적으로 요청해야 하는 부담이 있다.

```Python
from django.db.models import Max
qs = Score.objects.values('subject_name') \
                  .annotate(Max('score'))

for row in qs:
    row['student_name'] = \
        Score.objects.filter(
            subject_name=row['subject_name'],
            score=row['score__max']
        ).first().student_name
    print(row)

# 실행 결과
{'subject_name': '봉술', 'score__max': 100, 'student_name': '관우'}
{'subject_name': '성악', 'score__max': 25, 'student_name': '관우'}
{'subject_name': '음주', 'score__max': 100, 'student_name': '장비'}
```

#### Subquery

두번째는 `Subquery`를 이용해 각 과목별 최고 점수를 가져오는 서브쿼리를 통해 한 번의 쿼리 요청으로 전체 결과를 얻어오는 방법이다.
서브쿼리가 데이터베이스 상에서 발생하기 때문에 첫번째 방법에 비해 상대적으로 적은 비용으로 같은 결과를 얻을 것으로 예상된다.

```Python
from django.db.models import Subquery, OuterRef
qs = Score.objects.filter(
    id=Subquery(
        Score.objects.filter(subject_name=OuterRef('subject_name'))
            .order_by('-score')
            .values('id')[:1])
    ).values('subject_name', 'student_name', 'score')

for row in qs:
    print(row)

# 실행 결과
{'subject_name': '봉술', 'student_name': '관우', 'score': 100}
{'subject_name': '성악', 'student_name': '관우', 'score': 25}
{'subject_name': '음주', 'student_name': '장비', 'score': 100}
```

위 쿼리셋을 통해 작성된 SQL문은 대략적으로 아래와 같다.

```SQL
SELECT A.subject_name, A.student_name, A.score FROM ScoreTable A
    WHERE A.id = (
        SELECT B.id FROM ScoreTable B
            WHERE B.subject_name = A.subject_name
            ORDER BY B.score DESC
            LIMIT 1
    )
```

#### Raw query

세번째는 Django ORM을 통하지 않고 바로 SQL문을 실행하는 방법이다.
이는 해당 데이터베이스가 위에서 언급했던 *애매한* 결과를 문제삼지 않는 경우에 사용할 수 있다.
하지만 데이터베이스와 데이터가 저장된 순서에 따라 같은 동작이 보장되지 않으므로 추천하지 않는다.

```Python
qs = Score.objects.raw('''
    SELECT id, subject_name, student_name, MAX(score) FROM ScoreTable
        GROUP BY subject_name
''')

for row in qs:
    print(', '.join(
        ['{}: {}'.format(field, getattr(row, field))
            for field in ['subject_name', 'student_name', 'score']]
    ))

# 실행 결과
subject_name: 봉술, student_name: 관우, score: 100
subject_name: 성악, student_name: 관우, score: 25
subject_name: 음주, student_name: 장비, score: 100
```

### Many to one relationships

같은 문제를 일반적으로 많이 사용하는 [Many-to-one 관계](https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_one/)의 모델에서도 만날 수 있다.
다음과 같은 모델이 있을 경우 앞서 제시했던 방법을 어떻게 적용하는지 확인해보자.
`Contractor` 모델은 계약을 맺는 업자 정보를 담고 있고, `Contract`는 업자들이 맺은 계약지와 그 수량을 담고 있다고 가정한다.

```Python
class Contractor(models.Model):
    name = models.CharField(max_length=150, help_text="업자명")
    address = models.CharField(max_length=150, help_text="업자 주소")


class Contract(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    location = models.CharField(max_length=150, help_text="계약지")
    amount = models.IntegerField(help_text="계약 수량")


# Contract 데이터 예시
qs = Contract.objects.values_list(
    'contractor__name', 'location', 'amount')

for row in qs:
    print(row)

('Park', '서울', 10)
('Park', '인천', 90)
('Park', '부산', 30)
('Kim', '서울', 50)
('Kim', '인천', 10)
('Kim', '부산', 100)
```

가장 간단하게 계약자별 총 계약 수량이나 가장 큰 계약 건을 구하고 싶을 경우 아래와 같이 요청한다.

```Python
# 계약자별 총 계약 수량
>>> Contractor.objects.values_list('name', Sum('contract__amount'))
<QuerySet [('Park', 130), ('Kim', 160)]>

# 계약자별 가장 큰 계약 건
>>> Contractor.objects.values_list('name', Max('contract__amount'))
<QuerySet [('Park', 90), ('Kim', 100)]>
```

그렇다면, 각 계약자별 가장 큰 계약 건을 체결한 계약지가 어디인지 알아보려면 어떻게 해야 할까?
앞서 겪었던 문제가 똑같이 발생한다. 우선 `values_list`에 계약지를 추가해보자.

```Python
# 잘못된 쿼리셋
from django.db.models import Max
qs = Contractor.objects.values_list(
    'name', 'contract__location', Max('contract__amount'))

for row in qs:
    print(row)

# 실행 결과
('Park', '부산', 30)
('Park', '서울', 10)
('Park', '인천', 90)
('Kim', '부산', 100)
('Kim', '서울', 50)
('Kim', '인천', 10)
```

SQL문은 작성 의도와는 무관하게 아래와 같이 생성되었다.

```SQL
SELECT Contractor.name, Contract.location, MAX(Contract.amount)
    FROM Contractor
        LEFT OUTER JOIN Contract ON (
            Contractor.id = Contract.contractor_id
        ) GROUP BY Contractor.id, Contractor.name, Contractor.address, Contract.location
```

앞서 문제를 해결했던 세 가지 방법 중, 전체를 순회하거나 SQL을 직접 작성하는 방법은 다시 언급할 필요가 없으니,
두번째 방법인 `Subquery`를 사용해본다. 앞선 예제와 달리 `Contractor` 모델이 아닌 `Contract` 모델에서 시작하는 것이 중요하다.

```Python
# 계약자별 가장 큰 계약 건의 위치와 수량을 구하기
from django.db.models import Subquery, OuterRef
qs = Contract.objects.filter(
    id=Subquery(
        Contract.objects.filter(contractor=OuterRef('contractor'))
            .order_by('-amount')
            .values('id')[:1])
    ).values('contractor__name', 'location', 'amount')

for row in qs:
    print(row)

# 실행 결과
{'contractor__name': 'Park', 'location': '인천', 'amount': 90}
{'contractor__name': 'Kim', 'location': '부산', 'amount': 100}
```

마지막으로, 각 지역별 가장 큰 계약 건의 계약자와 수량을 구해보자.
앞선 예제에서 `contractor` 부분만 `location`으로 변경하는 것으로 쉽게 처리할 수 있다.
2개 이상의 필드에 대해서도 같은 방법으로 문제를 해결할 수 있다.
예를 들어, 지역 뿐 아니라 계약된 아이템에 대해서도 구별해서 확인하고자 한다면
`filter(location=OuterRef('location), item=OuterRef('item'))`과 같이 필터 조건을 변경하면 된다.

```Python
# 지역별 가장 큰 계약 건의 계약자와 수량을 구하기
from django.db.models import Subquery, OuterRef
qs = Contract.objects.filter(
    id=Subquery(
        Contract.objects.filter(location=OuterRef('location'))
            .order_by('-amount')
            .values('id')[:1])
    ).values('location', 'contractor__name', 'amount')

for row in qs:
    print(row)

# 실행 결과
{'location': '인천', 'contractor__name': 'Park', 'amount': 90}
{'location': '서울', 'contractor__name': 'Kim', 'amount': 50}
{'location': '부산', 'contractor__name': 'Kim', 'amount': 100}
```
