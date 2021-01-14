# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 타이타닉 dataset으로 연습

import pandas as pd

df2 = pd.read_csv('test.csv')
df = pd.read_csv('train.csv')

df

df.info()

df.describe()

df['Embarked'].value_counts(dropna=False) #결측치 세기

df['Embarked'].value_counts(normalize=True) #비율로 표시

df['Embarked'].unique()


# # loc 과 iloc 차이 
# + row를 호출할때는 차이가 없다.
# + column을 호출할때 차이가 발생

df.loc[1:]#row

df.iloc[1:]#row

df.loc[:2,['Survived','Pclass']] #loc은 column명을 제시

df.iloc[:2,1:3] #iloc은 index에 대해

df[3:5] #index로 인덱싱 가능/ 하지만 df[3]은 에러가 row 인덱싱

# # DataFrame Filter

df.filter(regex='S')

# # 결측치 처리
# + 평균값으로 대치
# + 이전값/이후값으로 대치
# + 그룹평 평균으로 대치
# + 데이터 전체 삭제하기
# + replace의 범용적 사용

# # 중복값 처리 

df.duplicated(['Fare'], keep='first')


df.duplicated(['Fare','Pclass'], keep='first')
#두개의 Column도 가능하다

df3=df
df3.drop_duplicates(['Fare'], keep='first')
#중복되는 값 다 제거
#나중에 꼭 쓸수 있는 곳이 있을 것 같다
#row의 개수가 248개로 줄었다

# # group by


