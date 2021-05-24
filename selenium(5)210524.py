# -*- coding: utf-8 -*-
"""
Created on Mon May 24 11:39:42 2021

@author: dms10
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = "http://naver.net"
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    #네이버 이동
    driver.get(url)

    # 로그인 버튼 클릭
    element = driver.find_element_by_class_name("link_login")
    element.click()

    # id, pass 입력(틀린)
    driver.find_element_by_id("id").send_keys("swthinking")
    driver.find_element_by_id("pw").send_keys("ddd")

    
    driver.find_element_by_id("log.login").click()
    # web scraping 작업 시작
except Exception as e:
    print(e)
