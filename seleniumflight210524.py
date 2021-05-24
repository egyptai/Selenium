# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:09:53 2021

@author: dms10
"""
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
except Exception as e:
    print(e)
finally:
    print("success")
#    driver.quit()
