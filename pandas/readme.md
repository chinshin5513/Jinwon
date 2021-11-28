### 0. 판다스 공부하면서 참고한 자료들 

[youtubelink] https://www.youtube.com/watch?v=bI7nnhXsBy8&list=PLaTc2c6yEwmry4B78IJwD47gE8b_ZEsVR

[youtubelink] https://www.youtube.com/watch?v=lG8pEwvYwCw 

[Pandas_Cheat_Sheet.pdf] https://github.com/chinshin5513/Jinwon/files/7544472/Pandas_Cheat_Sheet.pdf

[도서] Muller, A., (2021), Introduction to Machine Learning with Python, O'Reilly


### 1. 판다스의 특징
* 판다스(Pandas)는 데이터 처리와 분석에 특화된 파이썬 라이브러리이다. 데이터의 구성과 조작은 엑셀, SQL과 매우 유사하다.
* SQL처럼 join과 query 등이 가능하며, 넘파이(NumPy)와 달리 열의 타입이 달라도 가능하다.
* 또한, SQL, 엑셀, csv 등 다양한 파일을 데이터베이스로 읽을 수 있어 매우 강력한 툴이라고 할 수 있다.

판다스를 사용하기 위해서는 아래와 같이 라이브러리를 임포트하여 사용할 수 있다.
보통 배열과 차원을 다루는 넘파이와 함께 사용하여, 더 많은 작업에 활용할 수 있다.
```python
import pandas as pd
print(pd.__version__)
import numpy as np
```

### 2. 판다스의 객체
+ 표(Table) : 데이터 프레임(2. DataFrame)
+ 열(Columns) : 시리즈(1. Series)
+ 행(row) : 인덱스(3. Index)


#### 2.1. 시리즈(Series)
* 표(Table)는 행(column)과 열(row)로 구성되는데, 시리즈는 행에 해당하는 데이터이다. (세로)

```Python
s = pd.Series([0, 0.25, 0.5, 0.75, 1])
print(s)  # 시리즈를 만드는 과정
s.values  # 시리즈의 값을 볼 때
s.index  
s[1]  # 인덱싱
s[1:4]  # 슬라이싱
```

* 시리즈의 인덱스를 별도로 지정할 수 있음
```Python
s = pd.Series([0, 0.25, 0.5, 0.75, 1],
               index=['a','b','c','d','e'])
s['c']  # 인덱스명으로 인덱싱
s[['b', 'c', 'd']]
'b' in s   # Boolean 연산으로 True 산출

# 연속되지 않은 값으로도 인덱스 이름 지정 가능
s = pd.Series([0, 0.25, 0.5, 0.75, 1],
               index=[2, 4, 6, 8, 10])
```

* unique 메소드를 사용하면 중복된 값을 제거하고 하나씩 산출할 수 있다.
* value_counts 메소드를 사용하면 각 값이 갖는 수량을 얻을 수 있다. (excel의 count, counta 함수)
```Python
s = pd.Series([0, 0, 0, 1, 1],
               index=['a','b','c','d','e'])
s.unique()
s.value_counts()
```

* isin 메소드를 사용하면 각 값이 들어 있는지 아닌지를 Boolean 연산으로 알려 준다.
```Python
s = pd.Series([0, 0.25, 0.5, 0.75, 1],
               index=[2, 4, 6, 8, 10])
s.isin([0.25, 0.75])
```     

* 튜플 형태를 바탕으로 시리즈를 만들 수 있다.
```Python
pop_tuple = {'서울특별시': 9720846,
             '부산광역시': 3404423,
             '인천광역시': 2947217,
             '대구광역시': 2427954,
             '대전광역시': 1417041,
             '광주광역시': 1455048}
population = pd.Series(pop_tuple)
print(population)
print(population['서울특별시'])
print(population['부산광역시', '대전광역시'])
```

#### 2.2. 데이터 프레임(DataFrame)
* 표(Table)는 행(column)과 열(row)로 구성되는데, 데이터 프레임은 여러 개의 행을 포함하는 객체이다.

```Python
pd.DataFrame([{'A':2, 'B':4, 'D':3}, {'A':4, 'B':5, 'C':7}])
# 없는 값들은 자동으로 NaN이 채워져 데이터프레임을 생성해 준다(Not a Number)

pd.DataFrame(np.random.rand(5, 5),
             columns = ['A', 'B', 'C', 'D', 'E'],
             index = [1, 2, 3, 4, 5])
```

```Python
male_tuple = {'서울특별시': 4732755,
              '부산광역시': 1668618,
              '인천광역시': 1473813,
              '대구광역시': 1198815,
              '대전광역시': 734441,
              '광주광역시': 720060}
male = pd.Series(male_tuple)
print(population)

female_tuple = {'서울특별시': 4988571,
                '부산광역시': 1735805,
                '인천광역시': 1470404,
                '대구광역시': 1229139,
                '대전광역시': 736599,
                '광주광역시': 734988}
female = pd.Series(female_tuple)
print(population)

```

* 세 개의 시리즈를 바탕으로 데이터 프레임 만들기
```Python
korea_df = pd.DataFrame({'인구수': population,
                         '남자인구수': male,
                         '여자인구수': female})
print(korea_df)
```

* 데이터프레임에 관련된 사항을 질의할 때
```Python
korea_df.index  # 인덱스를 볼 때 (서울, 부산, 인천, 대구, 대전, 광주)
korea_df.columns  # 컬럼만 볼 때 (인구수, 여자인구수, 남자인구수)

korea_df['여자인구수']  # 여자 인구수 컬럼의 데이터만 질의할 때
korea_df['서울특별시':'대전광역시']  # 서울, 부산, 인천, 대구, 대전 인덱스의 데이터를 질의할 때
```

#### 2.3. 인덱스(Index)
* 표(Table)는 행(column)과 열(row)로 구성되는데, 인덱스는 열을 포함하는 객체이다. (가로)

##### 2.3.1. 인덱스의 종류(클래스)
+ Index : 일반적인 인덱스 객체이며, NumPy 배열 형식으로 축의 이름을 표현
+ Int64Index : 정수 값을 위한 Index
+ MultiIndex : 단일 축에 여러 단계 색인을 표현하는 계층적인 Index 객체
+ DatetimeIndex : NumPy의 Datetime64 타입으로 타임스탬프 저장
+ PeriodIndex : 기간 데이터를 위한 Index

```Python
idx = pd.Index([2, 4, 6, 8, 10])
idx[1] 
idx[1:4:2]
idx[-1]
idx[::2]  # 기본적인 파이썬 슬라이싱 문법을 적용할 수 있음

print(idx) 
print(idx.size)  # 인덱스가 몇 개인지 알 수 있음
print(idx. shape)  # 인덱스 모양
print(idx.ndim)  # 인덱스 차원
print(idx.dtype)  # 인덱스의 데이터타입
```

##### 2.3.2. 인덱스의 연산
+ append
+ difference
+ intersection
+ union
+ isin
+ delete
+ drop
+ insert
+ is_monotonic
+ is_unique
+ unique

```Python
idx1 = pd.Index([1, 2, 4, 6, 8])  # 인덱스 1
idx2 = pd.Index([2, 4, 5, 6, 7])  # 인덱스 2

print(idx1.append(idx2))  # 인덱스 1에 인덱스 2를 붙이는 형태 
print(idx1.difference(idx2))   # 인덱스 1에 인덱스2에 있는 것을 뺌(차집합) == print(idx1 - idx2)
print(idx1.intersection(idx2))  # 인덱스 1과 인덱스2 중 공통된 것만 추출(교집합) == print(idx1 & idx2)
print(idx1.union(idx2))  # 인덱스 1과 인덱스 2를 묶어 집합으로 만들어 추출(합집합) == print(idx1 | idx2)
print(idx1 ^ idx2)  # 인덱스 1과 인덱스 2의 여집합을 추출

print(idx1.delete(0))  # 위치를 지정하여 인덱스 값을 삭제(첫 번째 인덱스 값 삭제)
print(idx1.drop(2))  # 값을 지정하여 인덱스 값을 삭제(2가 들어간 인덱스 값을 삭제)
```


### 3. 인덱싱
+ 

```Python
s = pd.Series([0, 0.25, 0.5, 0.75, 1],
               index=['a', 'b', 'c', 'd', 'e'])
s['b']  #
'b' in s
s.keys()  # 전체 인덱스 값을 조회할 수 있음
s.items()  # zip으로 묶여서 나옴
list(s.items())  # key와 value가 튜플로 중첩리스트되어 출력, 딕셔너리와 유사

s['f']  # 없는 인덱스를 새로 만들어서 냄
print(s)

s['a':'d']  # 슬라이싱(인덱스 이름)
s[0:3]  # 슬라이싱(위치값)
s[['a', 'b', 'd']

s[(s > 0.4) & (s < 0.8)]  # 특정 조건을 주어 필터링 하기
``` 

#### 3.1. 시리즈 인덱싱
```Python
s = pd.Series(['a','b','c','d','e'],
               index = [1, 3, 5, 7, 9])
               
s[1]  # 1을 이름으로 갖는 인덱스의 값을 슬라이싱 → 'a'
s[2:4]

s.iloc[1]  # 정수값으로 인덱스 위치를 접근(2번째 위치이므로 'b')
s.iloc[2:4]  # 슬라이싱도 가능

s.reindex(range(10))  # 인덱스 이름을 새로 바꾸는 것
s.reindex(ranage(10), method='bfill')  # 비어있는 값을 이전의 값으로 채우는 명령어(backfill)
```

#### 3.2. 데이터프레임 인덱싱
```Python
korea_df
korea_df['남자인구수']
korea_df.남자인구수  # 키값으로 접근하는 것도 가능
korea_df.여자인구수  # 키값으로 접근하는 것도 가능
korea_df['남여비율'] = (korea_df['남자인구수'] / korea_df['인구수']) * 100
korea_df.남여비율
korea_df['성비'] = (korea_df['남자인구수'] *100 / korea_df['여자인구수'])
korea_df.남여비율

korea_df.T  # 전치
korea_df.value[0]  # 값 한 줄만 뽑아내기

korea_df.loc[:'인천광역시', :'남자인구수']  # 슬라이싱
korea_df.loc[(korea_df.여자인구수 > 1000000)]  # 질의와 필터링, 여자 인구가 100만명 이상인 도시
korea_df.loc[(korea_df.인구수 < 3000000)]  # 질의와 필터링, 전체 인구가 300만명 이하인 도시
korea_df.loc[(korea_df.성비 > 100)]  # 질의와 필터링
korea_df.loc[(korea_df.인구수 > 1000000) & (korea_df.성비 > 100)]  # AND 연산도 가능


#### 3.3. 다중인덱싱(Multi indexing)
* 1차원의 시리즈와 2차원의 데이터프레임을 활용하여 고차원의 데이터를 처리하는데 유용한 인덱싱

korea_df
idx_tuples = [('서울특별시', 2010), ('서울특별시', 2020),
              ('부산광역시', 2010), ('부산광역시', 2020),
              ('인천광역시', 2010), ('인천광역시', 2020),
              ('대구광역시', 2010), ('대구광역시', 2020),
              ('대전광역시', 2010), ('대전광역시', 2020),
              ('광주광역시', 2010), ('광주광역시', 2020)]
print(idx_tuples)

pop_tuples = [10312545, 9720846,
               3567910, 3404423,
               2758296, 2947217, 
               2511676, 2427954, 
               1503664, 1471040, 
               1454636, 1455048]
population = pd.Series(pop_tuples, index=idx_tuples)  # 인덱스 생성, 멀티인덱스 아님

midx = pd.MultiIndex.from_tuples(idx_tuples)  # 멀티인덱스를 바로 만들어주는 함수
population = population.index(midx)

# 인덱싱
population[:, 2020]
population['대전광역시', :]

# 언스택: 멀티인덱싱을 전형적인 데이터프레임으로 변환해 줌
korea_mdf = population.unstack()  
# 스택: 데이터프레임을 다중인덱싱으로 변환하여 줌
korea_mdf = population.stack()

male_tuples = [5111259, 4732275,
               1773170, 1668618,
               1390356, 1476813,
               1255245, 1198815,
                753648,  734441,
                721780,  720060]
               
korea_mdf = pd.DataFrame({'총인구수': population,
                          '남자인구수': male_tuples})

female_tuples = 


```




- - -


배우는 것이 생기면 계속 업데이트 예정
