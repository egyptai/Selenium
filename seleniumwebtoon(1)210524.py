# -*- coding: utf-8 -*-
"""
Created on Mon May 24 14:46:02 2021

@author: dms10
"""
'''
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

'''
'''
print(soup.find("a", attrs = {"class":"Nbtn_upload"}))
print(soup.find(attrs = {"class":"Nbtn_upload"}))

print(soup.title)
print(soup.title.get_text())
print(soup.a)
print(soup.a.attrs)
print(soup.a["href"])

r1 = soup.find("li", attrs = {"class":"rank01"})
print(r1.a.get_text())
r2 = r1.next_sibling.next_sibling
print(r2.a.text)
r3 = r2.next_sibling.next_sibling
print(r3.a.text)

pr2 = r3.previous_sibling.previous_sibling
print(pr2.a.text)

print(r1.parent)

r1 = soup.find("li", attrs = {"class":"rank01"})
print(r1.a.get_text())
r2 = r1.find_next_sibling("li")
print(r2.a.get_text())


r1 = soup.find("li", attrs ={"class":"rank01"})
print(r1.a.get_text())
r2 = r1.find_next_siblings("li")

print(r2)
'''
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=662774&weekday=wed"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
'''
# 네이버웹툰 목록 전부 가지고 오기
webtoons = soup.find_all("td", attrs={"class":"title"} ) # 리스트 반환
for webtoon in webtoons:
    link = webtoon.a["href"]
    print(webtoon.a.text, "https://comic.naver.com/"+ link)
'''
webtoons = soup.find_all("dic", attrs={"class":"rating_type"})
for webtoon in webtoons:
    rate = webtoon.strong.get_text()
    print(rate)