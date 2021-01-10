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

# +
import numpy as np
import pandas as pd


df=pd.read_csv('kaggel-survey-2020/kaggle_survey_2020_responses.csv')

# -

df.info()

df.columns

df.value_counts

# +
import seaborn as sns
import matplotlib.pyplot as plt

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')
plt.style.use("seaborn-whitegrid")
# -

df.shape

df.head()

question =df.iloc[0] #index 0=가로 삭제
question

answer = df.drop([0],axis=0) # drop은 축 설정 가능

answer

Q1 = answer['Q1'].value_counts(normalize=True).sort_index() #sort 편하게 하는 방법은 몰랐음
#비율로 볼수도 있음normalize를 사용하면

Q1

Q1_1 = answer['Q1'].value_counts().sort_values() #빈도수를 가지고 정렬가능
Q1_1 

Q1.plot()

#sns.countplot(data=answer.sort_values('Q1'),x='Q1',palette='Blues_r').set_title('Q1') #sort 할수 있음
sns.countplot(data=answer.sort_values('Q1'),x='Q1').set_title('Q1')

Q1.plot.bar()

Q1.plot.barh()

Q2= answer['Q2'].value_counts().sort_values()
Q2

Q2.plot()


#함수로 표현
def count_plot_Q1_Q6(q_no,fsize=(10,6)): #기본값 정해주기
    order = answer[q_no].value_counts().index #순서만 따오기 
    #order = answer[q_no].value_counts().sort_index().index.tolist() #변수 오름차순
    plt.figure(figsize=fsize)
    sns.countplot(data=answer,y=q_no, order=order).set_title(question[q_no])
#order 자체에는 리스트 형태의 순서를 다 정해주는 그런 느낌
#따라서 리스트를 받아와야함


count_plot_Q1_Q6('Q1')

count_plot_Q1_Q6('Q2')

count_plot_Q1_Q6('Q3', fsize=(10,12))
#이렇게 기본값이 있는데 사이즈 넘겨주는 방법도 가능하구나

count_plot_Q1_Q6('Q4')

count_plot_Q1_Q6('Q5')

count_plot_Q1_Q6('Q6')

# # 단일문항이 아닐때 처리방법
# * 5지 선다 내용이 Dummy 처럼 기술 되어 있을때 or 중복 항목이 선택 가능할때 

count_plot_Q1_Q6('Q7_Part_3')

# # Filter

# +
question_Q7 = question.filter(regex="Q7") #Q7으로 시작하는 질문들

answer_Q7 = answer.filter(regex="Q7")
answer_Q7
# -

question_Q7

answer_Q7.notnull().sum()

answer_Q7.describe()

answer_Q7_count=answer_Q7.describe().loc[["top","count"]].T.set_index("top")
answer_Q7_count

answer_Q7.describe().loc[["top","count"]].T.set_index("top").plot.bar()

answer_Q7_count.index

sns.barplot(data=answer_Q7_count,x='count', y=answer_Q7_count.index,palette="Dark2")

# +
# count_plot_Q1_Q6??
# -

sns.countplot(data=answer,x='Q1')

# +
Q1Q2 = pd.crosstab(answer['Q1'],answer['Q2'])

Q1Q2[['Man','Woman']].plot.bar(rot=0) #rot - > 글자 회전 각도

Q1Q2[['Man','Woman']].sort_index(ascending=False).plot.bar(rot=0) #rot - > 글자 회전 각도

#Man도 data frame 형태로 가지고 오고 싶으면[['Man']]만 쓰면 된다. 
# -

sns.countplot(data=answer,x='Q1',hue='Q2')

plt.figure(figsize=(10,6))
sns.countplot(data=answer.sort_values('Q1'),x='Q1',hue='Q2').set_title("Age & gender")

q2q7 = answer.filter(regex="Q7|Q2$") #q7 포함 q2로 끝나는 것만 

q2q7.describe().loc['top'] #응답값 가져오기 loc -> 가로 선택

q2q7_cols = q2q7.describe().loc['top'].tolist()



# +
q2q7_count = q2q7.groupby('Q2').count()
del q2q7_cols[0]
q2q7_count.columns = q2q7_cols

q2q7_count.T

# -

q2q7_count.loc[['Man','Woman']].T

q2q7_count.loc[['Man','Woman']].T.sort_values("Woman").plot.barh()
#sort Values 쓰려면 위에 가로줄에 있어야된다.

# # 연봉

sns.countplot(data=answer.sort_values('Q24'),x='Q24',)


answer['Q24']

answer['Q24'].value_counts().plot.bar()


