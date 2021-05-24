# -*- coding: utf-8 -*-
"""
Created on Mon May 24 14:46:02 2021

@author: dms10
"""
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

'''
print(soup.find("a", attrs = {"class":"Nbtn_upload"}))
print(soup.find(attrs = {"class":"Nbtn_upload"}))
'''

print(soup.title)
print(soup.title.get_text())
print(soup.a)
print(soup.a.attrs)
print(soup.a["href"])