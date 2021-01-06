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

url = "https://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url,headers = headers)
#user Agent -> 익스플로어 or 크롬에 따라 다르게 표현
#user Agent string이라고 검색

res.raise_for_status()

# +
#res.text
# -

with open('mygoogle.html', 'w' ,encoding = 'utf-8') as f:
    f.write(res.text)

'''
import re
p=re.compile("ca.e")
re.compile("^de")
re.compile("ce&")


m = p.match("cafeless") #-> cafe 뒷부분에 다른 말이 와도 매치됨 
#match는 앞에
if m:
    print(m.group())
else:
    print("matchx")
    
# search는 중간에 있어도 ㄱㅊ
'''

from bs4 import BeautifulSoup


url ="https://comic.naver.com/webtoon/weekday.nhn"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

soup.title.get_text()

soup.a.get_text() #-> a중에 제일빠른애 나옴

a=soup.find_all

rank1=soup.find("li",attrs={"class":"rank01"})

rank1.get_text()

# 형제관계 previous silbing도 가능


rank1.find_next_sibling("li").get_text()

rank1.find_next_siblings

abc=soup.find_all("a", attrs={"class":"title"})

for i in abc:
    print(i.get_text())

url = "https://comic.naver.com/webtoon/list.nhn?titleId=703846&weekday=tue"
res= requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

soup

ads=soup.find_all("td",attrs={"class":"title"})

for i in ads:
    print(i.a.get_text())

# +
#https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor=


#get 방식 -> ? 옆에 페이지, 뭐 maxprice 이런것들 입력해서 내가 원하는 값 얻을 수 있음

# -

for i in range(1,6):
    
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='.format(i)
    import re
    import requests
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    items=soup.find_all("li",attrs={"class":re.compile("^search-product")})
    for i in items:
        ad_badge = i.find("span",attrs={"class":"ad-badge-text"})
        if ad_badge:
            print("광고상품")
            continue
        #continue는 포문 다음으로 넘김 근데 pass는 계속 진행됨 차이 잘 알기
        name = i.find("div",attrs={"class":"name"}).get_text()
        price = i.find("strong",attrs={"class":"price-value"}).get_text()
        rating = i.find("em",attrs={"class":"rating"})
        if rating:
            rating2 = rating.get_text()
        else:
            rating2 ="평점 없음"
        rate_cnt = i.find("span",attrs={"class":"rating-total-count"})
        if rate_cnt:
            rate_cnt2 = rate_cnt.get_text()
        #else:
        #    rate_cnt2 ="평점 없음"
        print("제품명 :{0}, 가격 :{1}, 평점 : {2}, 평점참여자수 :{3}".format(name,price,rating2,rate_cnt2))
    



items

for i in items:
    ad_badge = i.find("span",attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("광고상품")
        continue
    #continue는 포문 다음으로 넘김 근데 pass는 계속 진행됨 차이 잘 알기
    name = i.find("div",attrs={"class":"name"}).get_text()
    price = i.find("strong",attrs={"class":"price-value"}).get_text()
    rating = i.find("em",attrs={"class":"rating"})
    if rating:
        rating2 = rating.get_text()
    else:
        rating2 ="평점 없음"
    rate_cnt = i.find("span",attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt2 = rate_cnt.get_text()
    #else:
    #    rate_cnt2 ="평점 없음"
    print("제품명 :{0}, 가격 :{1}, 평점 : {2}, 평점참여자수 :{3}".format(name,price,rating2,rate_cnt2))
    link = i.find("a", attrs={"class":"search-product-link"})['href']
    
    print("바로가기 주소 :",link)
    print("-"*30)






