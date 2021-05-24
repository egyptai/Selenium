# -*- coding: utf-8 -*-
"""
Created on Mon May 24 11:46:58 2021

@author: dms10
"""

import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://naver.net"
driver = webdriver.Chrome()

try:
    driver.get(url)
    
    element = driver.find_element_by_class_name("link_login")
    element.click()
    
    pyperclip.copy("본인ID")
    driver.find_element_by_id("id").send_keys(Keys.CONTROL, 'v')
    pyperclip.copy("본인PW")
    driver.find_element_by_id("pw").send_keys(Keys.CONTROL, 'v')
    driver.find_element_by_id("pw").send_keys(Keys.Enter)
    
except Exception as e:
    print(e)