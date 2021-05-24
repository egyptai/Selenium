# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:09:53 2021

@author: dms10
"""
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#################################################################
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#################################################################

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://flight.naver.com/flights/"
driver.get(url)
try:
    driver.find_element_by_link_text("가는날 선택").click()
#5/29~6/30일 선택
    driver.find_elements_by_link_text("29")[0].click()
    driver.find_elements_by_link_text("29")[0].click()
    
    # 여행지 선택
    driver.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/dl").click() 
    
     
    # 항공권 검색 클릭
    driver.find_element_by_link_text("항공권 검색").click()
