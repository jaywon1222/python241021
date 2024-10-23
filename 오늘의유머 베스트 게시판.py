#Chap09_클리앙중고장터검색.py
# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

for n in range(1,11):
        #오늘의 유머베스트 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=humorbest&page=' + str(n)
        print(data)
        #헤더추가
        req= urllib.request.Request(data, headers = hdr)
        request = urllib.request.Request(data, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req).read()

        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        # <span class="subject_fixed" data-role="list-title-text" title="맥북프로 M2 13인치 24/512 실버">
		# 		맥북프로 M2 13인치 24/512 실버
		# </span>
        for item in list:
            try:
                title = item.text.strip()
                print(title)
            except:
                    pass




