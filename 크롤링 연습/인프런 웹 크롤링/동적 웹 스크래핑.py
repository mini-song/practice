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
#headless
#-> 창을 안띄움 서버에서 크롤링하거나... 메모리 소모를 줄여줌

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size = 1920x1080")
options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://play.google.com/store/movies/top"
#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36","Accept-Language":"ko-KR,ko"}
browser.get(url)


soup= BeautifulSoup(res.text,'lxml')
soup

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})

len(movies)




