# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:46:55 2021

@author: dms10
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager

url = "http://daum.net"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
element = driver.find_element_by_class_name("link_login")
element.send_keys("인기영화")


element = driver.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]") 
                                        
element.click()
