# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:42:30 2021

@author: dms10
"""

import selenium

from selenium import webdriver

url = "http://naver.com"
driver = webdriver.Chrome(r"chromedriver.exe")
driver.get(url)
element = driver.find_element_by_class_name("Link_again")
element.click()