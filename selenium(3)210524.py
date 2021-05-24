# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:33:12 2021

@author: dms10
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = "http://naver.com"
driver = webdriver.Chrome(r"C:\Users\dms10\WebCrolling\chromedriver.exe")

driver.get(url)
element = driver.find_element_by_tag_name("a")
elements = driver.find_elements_by_tag_name("a")

for idx, e in enumerate(elements):
    ele = e.get_attribute('href')
    print(ele)
    time.sleep(0.5)
    