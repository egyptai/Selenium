# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:10:03 2021

@author: dms10
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://naver.com"
driver = webdriver.Chrome(r"C:\Users\dms10\WebCrolling\chromedriver.exe")

driver.get(url)
element = driver.find_element_by_id("query")
element.send_keys("컴퓨터")
element.send_keys(Keys.ENTER)
