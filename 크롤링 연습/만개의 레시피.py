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

for i in tqdm(range(1,11)):
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
url = 'https://www.10000recipe.com/recipe/list.html?cat3=70&order=reco&page=1'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html,'html.parser')
소고기_number_list=soup.find_all("div",attrs={'class':'common_sp_thumb'})

browser.quit()
# -

len(url_1000개)

url_1000개[230]

# +

csv_list=[['title','재료','태그']]
for url_ in tqdm(url_1000개):
    try:
        url = url_
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html,'html.parser')
        #movies = soup.find("div",attrs={'class':'view2_summary st3'})
        ingredient = soup.find("div",attrs={'class':'ready_ingre3'})
        browser.quit()
        재료=[]
        title=soup.find("h3").text
        t=ingredient.find_all('a')
        s=soup.find("div", attrs={'class':"view_tag"})
        tag=[]
        for i in s:
            tag.append(i.text.replace('#',''))
        for i in t:
            재료.append(i.text.strip().replace(" ","").replace("\n"," "))
        하나=[]
        하나.append(title)
        하나.append(재료)
        하나.append(tag)
        csv_list.append(하나)
    except Exception:
        pass
# +
import pandas as pd

바꾸자=pd.DataFrame(csv_list)
바꾸자.to_csv('웹스크래핑_400.csv',encoding='utf-8-sig',header=False)

# -



