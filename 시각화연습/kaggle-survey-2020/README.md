# 인프런 무료제공 강의 Kaggle 설문 조사 자료 시각화 연습
* Seaborn , plt
        
      - iloc, loc 에 대한 복습
      - answer = df.drop([0],axis=0)  #drop 축 설정에 대한 복습
      - answer['Q1'].value_counts().plot() 빈도수별로 모아서 plot 찍으면 바로 찍히는 것(범주형 자료에서 활용가능)
      - Q1.plot.barh() #축 바꿔서 찍기
      - sns.countplot(data=answer,x='Q1').set_title('Q1') #sns로 countplot 찍기 보통 plt를 활용해서 sns에 대해 제대로 배웠다
      - sns.countplot(data=answer.sort_values('Q1'),x='Q1').set_title('Q1') #정렬가능 values/index
      - DataFrame Filter에 대해 처음 알게 되었다. groupby만 알고 있었는데 새롭다.
      - question_Q7 = question.filter(regex="Q7") #다양한 정규식을 통해 특정 칼럼을 포함한 행을 뽑을 수 있다.
      - answer_Q7.notnull().sum() 결측치만 제외하고 빈도수를 시리즈로 반환
      - dataframe['A'] 하면 시리즈로 가져와서 dataframe에서 지원하는 함수를 못써서 다시 반환해주는 경우가 있었는데
      - dataframe[['A']]로 해결 할 수 있다는 것을 처음 알게 되었다.
* 부족한 부분
** groupby에 대해서 많이 학습하지 못한 것 같아서 더 찾아서 해봐야 될 것 같다.
** 행, 열 합치기 자유자재로 연습할 수 있게 강의 찾아보기
