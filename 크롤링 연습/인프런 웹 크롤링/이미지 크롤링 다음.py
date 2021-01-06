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


res





for o in range(2015,2020):
    url= 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q={0}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84'.format(o)
    soup =  BeautifulSoup(res.text,'lxml')
    res= requests.get(url)
    images = soup.find_all("img",attrs={"class":"thumb_img"})
    for idx, i in enumerate(images): #인덱스 처리 
        if i['src'].startswith("//"):
            image_res = requests.get("https:"+i['src'])
        else:

            image_res = requests.get(i['src'])
        with open("movie{0}_{1}.jpg".format(idx+1,o),"wb") as f:
            f.write(image_res.content) #주소로 바로 연결 -> 안에 있는 내용물 -> 파일로
        if idx ==4:
            break;




