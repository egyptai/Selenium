# -*- coding: utf-8 -*-
"""
Created on Mon May 24 14:19:05 2021

@author: user
"""

# 네이버 항공권 아라님 + 추가내용(웹드라이버 자동으로 찾기, 국내 & 해외 구분)

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:32:53 2021

@author: ASIAE1
"""


from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

#####
from webdriver_manager.chrome import ChromeDriverManager


url = "https://flight.naver.com/flights/"

####
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

try:
    ####
    dest_list = ['CJU', 'PUS', 'USN', 'KWJ']
    
    driver.find_element_by_link_text("가는날 선택").click()
    driver.find_elements_by_link_text("29")[0].click()
    driver.find_elements_by_link_text("10")[1].click()

    
    # # 여행지 선택(xpath)
    # 1. 방콕 (방콕은 일단 주석처리하고 파리를 해보겠습니다.) 
    # driver.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[3]/div/dl/dd[1]').click()
    
    # 2. 파리 
    driver.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[8]/div/span').click()
    
    # # 항공권 검색 클릭(find_elements_by_link_text)
    driver.find_element_by_xpath('//*[@id="searchArea"]/a').click()

######
    dest = driver.find_element_by_xpath("//*[@id='l_1']/div/div[2]/div[1]/span")
    if (dest.text in dest_list):
        tmpPath = "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"     # 국내
    else:
        tmpPath = "//*[@id='content']/div[3]/div[1]/div[7]/ul/li[1]"  # 해외

    WebDriverWait(driver, 50).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR ,'#content > div:nth-child(3) > div.trip_itinerary.ng-scope > div.trip_banner.ng-scope > div.apply_filter_box > em')))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    

    final=driver.find_element_by_css_selector('#content > div:nth-child(3) > div.trip_itinerary.ng-scope > div:nth-child(7) > ul > li:nth-child(1)')
    
   
   #결과값을 출력합니다 
    print(final.text)
   

except Exception as e:
    print(e)
finally:
    print("success")









