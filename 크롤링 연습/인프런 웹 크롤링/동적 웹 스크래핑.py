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

# # 셀레니움 사용 x 

# +
#options = webdriver.ChromeOptions()
#options.headless = True
#options.add_argument("window-size = 1920x1080")
#options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
#browser = webdriver.Chrome(options=options)
#browser.maximize_window()


url = "https://play.google.com/store/movies/top"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
           "Accept-Language":"ko-KR,ko"} #Korean 언어에 대한 페이지 호출
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.text,'lxml')
movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
for i in movies:
    print(i.find("div", attrs={"class":"WsMG1c nnK0zc"}).text)
# -


# # 동적 웹스크래핑 -> 셀레니움 이용

# +
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://play.google.com/store/movies/top"
browser.get(url)
#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
#           "Accept-Language":"ko-KR,ko"} #Korean 언어에 대한 페이지 호출
#해상도 높이 만큼 스크롤 내리기
#browser.execute_script("window.scrollTo(0,1080)")


#화면 가장 아래로 내리기

prev_height = browser.execute_script("return document.body.scrollHeight")
import time 
interval = 2 

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(interval)
    #현재 문서 높이 저장
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height ==prev_height:
        break
    prev_height = current_height

#할인된 애들만

import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source,'lxml')
#'ImZGtf mpg5gc'
movies = soup.find_all("div",attrs={'class':'Vpfmgd'})
for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    original_price= movie.find("span",attrs={'class':"VfPpfd ZdBevf i5DZme"})
    discount_price = movie.find("span",attrs={'class':"SUZt4c djCuy"})
    if discount_price:
        discount_price= discount_price.get_text()
        
    else:
        #print(title, " 할인되지 않은 영화제외")
        continue
    print(title)
    print("할인전:",original_price.get_text())
    print("할인후:",discount_price)
browser.quit()

# -
# # Headless 크롬

# +
from selenium import webdriver

#내부적 설계
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("windows-size=1920*1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://play.google.com/store/movies/top"
browser.get(url)
#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
#           "Accept-Language":"ko-KR,ko"} #Korean 언어에 대한 페이지 호출
#해상도 높이 만큼 스크롤 내리기
#browser.execute_script("window.scrollTo(0,1080)")


#화면 가장 아래로 내리기

prev_height = browser.execute_script("return document.body.scrollHeight")
import time 
interval = 2 

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(interval)
    #현재 문서 높이 저장
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height ==prev_height:
        break
    prev_height = current_height

#할인된 애들만

import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source,'lxml')
#'ImZGtf mpg5gc'
movies = soup.find_all("div",attrs={'class':'Vpfmgd'})
for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    original_price= movie.find("span",attrs={'class':"VfPpfd ZdBevf i5DZme"})
    discount_price = movie.find("span",attrs={'class':"SUZt4c djCuy"})
    if discount_price:
        discount_price= discount_price.get_text()
        
    else:
        #print(title, " 할인되지 않은 영화제외")
        continue
    print(title)
    print("할인전:",original_price.get_text())
    print("할인후:",discount_price)
browser.get_screenshot_as_file("결과.png")
browser.quit()


