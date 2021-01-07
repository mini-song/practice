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

spool2=[]
today_=datetime.datetime.now()
import datetime
import time
friends_id = ['minisong','준선이는승현이꺼','분홍콩','동혁이에오','연습용 오른']
csv_list =[]
import requests
import json
for friend in friends_id:
    

    api_key = 'RGAPI-f93869d5-e1f2-499c-b735-f037d0c780b9'
    sohwan = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +friend +'?api_key=' + api_key
    r = requests.get(sohwan)
    r
    tier_url = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + r.json()['id'] +'?api_key=' + api_key
    r2  = requests.get(tier_url)
    print(datetime.datetime.now(),friend,r2.json()[1]['tier'],r2.json()[1]['rank'],r2.json()[1]['leaguePoints'])
    
    spool = r2.json()[1]['tier'] + " " + r2.json()[1]['rank'] + " "+ str(r2.json()[1]['leaguePoints'])+" 점"
    spool2.append(spool)
spool2.append(today_)
csv_list.append(spool2)

f = open('친구들 롤 티어 동향.csv','r')
rdr = csv.reader(f)
f = open('친구들 롤 티어 동향.csv','a',newline='',encoding='utf-8') #원본을 훼손할 위험이 있으니 다른 파일에 저장하는 것을 추천합니다.
wr = csv.writer(f)
wr.writerows(csv_list)
f.close()

# +
#나중에 감시용도로 발전 시키거나 시각화 or 상위 티어 큐 분석해서 친구들 챔프 동향에 맞게 
# 추천해주는 걸로 발전 시킬 수도 있을 것 같다.
# -


#처음 생성
friends_id.append('오늘 날짜')
import pandas as pd
df = pd.DataFrame(csv_list)
df.to_csv('친구들 롤 티어 동향.csv',index=False,header=friends_id,encoding='utf-8')

# +
grandmaster = 'https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=' + api_key
r = requests.get(grandmaster)
league_df = pd.DataFrame(r.json())

league_df.reset_index(inplace=True)
league_entries_df = pd.DataFrame(dict(league_df['entries'])).T 
league_df = pd.concat([league_df, league_entries_df], axis=1) 
league_df = league_df.drop(['index', 'queue', 'name', 'leagueId', 'entries', 'rank'], axis=1)
league_df.info()
league_df.to_csv('챌린저데이터.csv',index=False,encoding = 'cp949')#
# -

league_df

# +
#https://shinminyong.tistory.com/11 참고하였습니다.

# 나중에 상위 큐 점수 동향 // 메타 챔피언 분석 -> 프로 프렌차이즈화 구단 자동으로 아마추어 고수 스카웃 하는 BI 의사결정에 
# 도움을 주는 것으로 바꿀 수 있지 않을까
