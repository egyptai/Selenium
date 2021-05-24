# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:28:18 2021

@author: dms10
"""
from bs4 import BeautifulSoup as bs
import requests
url1 = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method='\
            'download&searchType=13'
krx = requests.get(url1)
soup = bs(krx.text, "html.parser")
ex1 = soup.find_all("td", style = "mso-number-format:'@';text-align:center;")
for i in range(len(ex1)):
    print(ex1[i].text)
