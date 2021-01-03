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

import pandas as pd
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver

# +
import requests
from bs4 import BeautifulSoup

target = input("검색어를 입력하세요:")

for page in range(1,5,1):
    req = requests.get(f'https://search.naver.com/search.naver?&where=news&query={target}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=30&start=11&refresh_start=0',
                       headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"})
 
      
    browser = webdriver.Chrome('chromedriver.exe')
    
    
    html = browser.page_source
    print(html)
    
    tag = soup.select("ul.type01 > li")
    for a in tag:
        title = a.select_one("ul.type01 > li a._sp_each_title").text
        print(title)


# +
# Okt 형태소 분석기 호출, 트위터에서 만든 오픈소스 한국어 분석기
from konlpy.tag import Okt
okt = Okt()

nouns = okt.nouns(title) #명사 분석
nouns

# +
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import urllib.request

import json
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime as dt
# -

b = list()
url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={target}'
browser  = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(2)
for page in range(1,10):
    browser.find_elements_by_xpath(f'//*[@id="main_pack"]/div[1]/div[2]/a[{str(page)}]')[0].click()
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    tag = soup.select("ul.type01 > li")
    for a in tag:
        title = a.select_one("ul.type01 > li a._sp_each_title").text
        b.append(title)









