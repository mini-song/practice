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

import requests
from bs4 import BeautifulSoup
import csv 

# +
csv2 = []
f = open('csvresult.csv',"w",encoding='utf-8', newline="") #뉴라인 안하면 엔터계속됨
#인코딩 utf-8-sig 도 활용가능 
#csv 쓰는게 리스트당 한줄이라고 생각하면 편함

writer = csv.writer(f)

for o in range(1,5):
    
    res = requests.get('https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={0}'.format(o))
    soup = BeautifulSoup(res.text,'lxml')
    data = soup.find('table', attrs={"class":'type_2'}).find_all('tr')
    #태그 정보와 class 정보가 한줄에 다 들어있으니까 우선적으로 찾아야함 
    for i in data:
        a=i.find_all('td')
        b=[]
        if len(a) <= 1: #의미 없는 부분이 어느 for문에서 작용하는지 잘 생각하면 좋을듯
            continue
        else:
            
            for x in a:
                b.append(x.get_text().strip())
            writer.writerow(b)
            csv2.append(b)
import pandas as pd
df = pd.DataFrame(csv2)
df.to_csv('result.csv',header=False,index=False)
# -




