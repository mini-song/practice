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
from selenium import webdriver
#기다려주기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://flight.naver.com/flights/")
browser.maximize_window()


#elem = browser.find_element_by_class_name("link_login")
#elem.click()
#browser.back()
#browser.forward()
#browser.refresh()


#browser.back()


#elem = browser.find_element_by_class_name("txt_trip.ng-binding")
elem = browser.find_element_by_link_text("가는날 선택")


#from selenium.webdriver.common.keys import Keys
#elem.send_keys("나도코딩")
elem.click()
browser.find_elements_by_link_text("28")[0].click()
browser.find_elements_by_link_text("10")[1].click()                   
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()
browser.find_element_by_link_text('항공권 검색').click()
elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))

elem=browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
print(elem.text)
    
# -


