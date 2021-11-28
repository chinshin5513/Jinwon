# 판다스의 객체
# 1. 시리즈(Series) : 표에서 열에 해당하는 부분(세로로 하나의 열이 있음)

import pandas as pd
print(pd.__version__)
import numpy as np

# 시리즈 만드는 방법
s = pd.Series([0, 0.25, 0.5, 0.75, 1])
print(s)  # 시리즈를 만드는 과정
s.values  # 시리즈의 값을 볼 때
s.index  
s[1]  # 인덱싱 (한 지점을 지정해서 검색)
s[1:4]  # 슬라이싱 (여러 구간을 지정해서 검색)


# 시리즈의 인덱스를 붙이는 것도 가능함
s = pd.Series([0, 0.25, 0.5, 0.75, 1],
               index=['a','b','c','d','e'])
s['c']  # 인덱스명으로 인덱싱
s[['b', 'c', 'd']]
'b' in s   # Boolean 연산으로 True 산출

# 연속되지 않은 값으로도 인덱스 이름 지정 가능
s = pd.Series([0, 0.25, 0.5, 0.75, 1],
               index=[2, 4, 6, 8, 10])

# uiique 메소드를 사용하면 중복된 값을 제거하고 하나씩 산출할 수 있다.
# value_counts 메소드를 사용하면 각 값이 갖는 수량을 얻을 수 있다. (excel의 count, counta 함수)
s = pd.Series([0, 0, 0, 1, 1],
               index=['a','b','c','d','e'])
s.unique()
s.value_counts()


# isin 메소드를 사용하면 각 값이 들어 있는지 아닌지를 Boolean 연산으로 알려 준다.
s = pd.Series([0, 0.25, 0.5, 0.75, 1],
               index=[2, 4, 6, 8, 10])
s.isin([0.25, 0.75])

# 튜플 형태를 바탕으로 시리즈를 만들 수 있다.
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

