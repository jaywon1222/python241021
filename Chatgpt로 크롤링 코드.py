import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 크롤링할 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 웹 페이지 요청
response = requests.get(url)

# 요청이 성공했는지 확인
if response.status_code == 200:
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 신문기사 제목을 포함하는 태그를 찾기
    titles = soup.find_all('a', class_='news_tit')  # class 이름은 실제 페이지에 따라 다를 수 있음

    # Excel 파일 생성
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "News Titles"

    # 헤더 추가
    sheet.append(["Title"])

    # 제목을 Excel 파일에 추가
    for title in titles:
        sheet.append([title.get_text()])

    # Excel 파일 저장
    workbook.save("results.xlsx")
    print("결과가 results.xlsx 파일로 저장되었습니다.")
else:
    print("웹 페이지 요청에 실패했습니다.")
