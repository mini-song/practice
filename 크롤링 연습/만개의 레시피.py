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
qwe =[['ab'],['b'],['c','a'],['d']]

for i in qwe:
    for j in i:
        if 'a' in j:
            print('포함',j)
        elif 'b' in j:
            print("포함",j)
        else:
            print('미포함',j)
# -

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm

# +
from selenium import webdriver

#내부적 설계
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("windows-size=1920*1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://www.10000recipe.com/ranking/home_new.html"
browser.get(url)
import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source,'lxml')
#'ImZGtf mpg5gc'
movies = soup.find("div",attrs={'class':'view2_summary st3'})
title=soup.find("h3").text
ingredient = soup.find("div",attrs={'class':'ready_ingre3'})
#a=browser.find_element_by_xpath("//*[@id='contents_area']/div[2]/h3")
#print(a)
browser.quit()


# -

number_list=soup.find_all("div",attrs={'class':'common_sp_thumb'})

len(number_list)

number_list

ranking_url=[]

for i in number_list:
    print('https://www.10000recipe.com'+i.find('a')['href'])
    ranking_url.append('https://www.10000recipe.com'+i.find('a')['href'])

csv_list = [['title','재료']]

# + 확실히 ChromDriver 보다 이렇게 진행하는게 속도가 빠르다

'''
url = 'https://www.10000recipe.com/recipe/6899265'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html,'html.parser')
movies = soup.find("div",attrs={'class':'view2_summary st3'})
ingredient = soup.find("div",attrs={'class':'ready_ingre3'})
browser.quit()
재료=[]
title=soup.find("h3").text
t=ingredient.find_all('a')
for i in t:
    재료.append(i.text.strip().replace(" ","").replace("\n"," "))
하나=[]
하나.append(title)
하나.append(재료)
csv_list.append(하나)
'''



for url_ in tqdm(ranking_url):
    try:
        url = url_
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        movies = soup.find("div",attrs={'class':'view2_summary st3'})
        ingredient = soup.find("div",attrs={'class':'ready_ingre3'})
        browser.quit()
        재료=[]
        title=soup.find("h3").text
        t=ingredient.find_all('a')
        for i in t:
            재료.append(i.text.strip().replace(" ","").replace("\n"," "))
        하나=[]
        하나.append(title)
        하나.append(재료)
        csv_list.append(하나)
    except Exception:
        pass

csv_list

csv_list

import pandas as pd

바꾸자=pd.DataFrame(csv_list)

바꾸자


바꾸자.to_csv('웹스크래핑.csv',encoding='utf-8-sig',header=False)



# +
url_1000개=[]

for i in tqdm(range(1,26)):
    try:
        url = 'https://www.10000recipe.com/recipe/list.html?cat3=70&order=reco&page='+str(i)
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        소고기_number_list=soup.find_all("div",attrs={'class':'common_sp_thumb'})
        for i in 소고기_number_list:
            url_1000개.append('https://www.10000recipe.com' + i.find('a')['href'])
        browser.quit()
        print(len(url_1000개))
    except Exception:
        pass

# +
#test_=url_1000개[1:100]

# +
#https://www.10000recipe.com/recipe/6883714

# +


import re
testt = ['https://www.10000recipe.com/recipe/6852019']
csv_list=[['title','재료','태그','url','이미지주소']]



for url_ in tqdm(url_1000개):
    
    url = url_
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    #movies = soup.find("div",attrs={'class':'view2_summary st3'})
    try:
        ingredient = soup.find("div",attrs={'class':'ready_ingre3'})
    except Exception:
        pass
    browser.quit()
    재료=[]
    title=soup.find("h3").text
    try:
        t=ingredient.find_all('a')
    
        s=soup.find("div", attrs={'class':"view_tag"})
        tag=[]
        for i in s:
            tag.append(i.text.replace('#',''))
    except Exception:
        pass
    스위치=0
    for i in tag:
    
        if '자취' in i:
            print(i)
            스위치=스위치+1
        elif '간단' in i:
            print(i)
            스위치=스위치+1
        else:
            pass

    
    if 스위치 >=1:
        for i in t:
            재료.append(i.text.strip().replace("\n","").split(" ")[0])
        
        하나=[]
        image = soup.find("div",attrs={'class':'centeredcrop'}).find('img')['src']
        하나.append(title)
        하나.append(재료)
        하나.append(tag)
        하나.append(url)
        하나.append(image)
        csv_list.append(하나)
    else:
        pass

# -

csv_list

# +
import pandas as pd

바꾸자=pd.DataFrame(csv_list)
바꾸자.to_csv('웹스크래핑_0224.csv',encoding='utf-8-sig',header=False)


# +
url = 'https://www.10000recipe.com/recipe/list.html?cat3=70&order=reco&page=1'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html,'html.parser')
소고기_number_list=soup.find_all("div",attrs={'class':'common_sp_thumb'})

browser.quit()
# -

len(url_1000개)

len(url_1000개)

# +
import re
csv_list=[['title','재료','태그','url']]



for url_ in tqdm(url_1000개):
    
    url = url_
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    #movies = soup.find("div",attrs={'class':'view2_summary st3'})
    try:
        ingredient = soup.find("div",attrs={'class':'ready_ingre3'})
    except Exception:
        pass
    browser.quit()
    재료=[]
    title=soup.find("h3").text
    try:
        t=ingredient.find_all('a')
    
        s=soup.find("div", attrs={'class':"view_tag"})
        tag=[]
        for i in s:
            tag.append(i.text.replace('#',''))
    except Exception:
        pass
    스위치=0
    for i in tag:
    
        if '자취' in i:
            print(i)
            스위치=스위치+1
        elif '간단' in i:
            print(i)
            스위치=스위치+1
        else:
            pass

    
    if 스위치 >=1:
        for i in t:
            재료.append(i.text.strip().replace("\n","").split(" ")[0])
        
        하나=[]
        
        하나.append(title)
        하나.append(재료)
        하나.append(tag)
        하나.append(url)
        csv_list.append(하나)
    else:
        pass
# +
import pandas as pd

바꾸자=pd.DataFrame(csv_list)
바꾸자.to_csv('웹스크래핑_1000개 필터.csv',encoding='utf-8-sig',header=False)



# +
from konlpy.tag import *

hannanum = Hannanum()
kkma = Kkma()
komoran = Komoran()
#mecab = Mecab()
okt = Okt()
# -

hannanum.nouns('차돌박이 참나물 샐러드 , 쉽고 간단하지만 폼나고 맛있다.')

kkma.nouns('차돌박이 참나물 샐러드 , 쉽고 간단하지만 폼나고 맛있다.')

komoran.nouns('차돌박이 참나물 샐러드 , 쉽고 간단하지만 폼나고 맛있다.')

okt.nouns('차돌박이 참나물 샐러드 , 쉽고 간단하지만 폼나고 맛있다.')

from eunjeon import Mecab

tagger=Mecab()

tagger.nouns('차돌박이 참나물 샐러드 , 쉽고 간단하지만 폼나고 맛있다.')

# +
import requests
import json

api_key="http://api.adams.ai/datamixiApi/tms?query=프랑스의 시골파이 - 아쉬 빠흐멍띠에 -.&lang=kor&analysis=pos&key=5407184264015720799"

#api_key ="http://svc.saltlux.ai:31781?&key=0857f633-ca21-4b7a-8e7b-873e224ba430&serviceId=01135983394&argument=오늘날씨가 좋네요."
# -

r2  = requests.get(api_key)

r2.json()


