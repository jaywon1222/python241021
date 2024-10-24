#DemoForm2.py
 
from bs4 import BeautifulSoup
import requests

#Chap10_DemoForm2.ui(화면을 XML문서 저장) + Chap10_DemoForm2.py(로직 코딩) 
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#디자인 문서를 로딩(파일명이 변경됨)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#윈도우 클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)

        #검색이 용이한 객체 생성
        soup = BeautifulSoup(response.text, "html.parser")

        f=open("daangn.txt","a+", encoding="utf-8")
        posts = soup.find_all("div", attrs={"class":"card-desc"})

        for post in posts:
            titleElem = post.find("h2", attrs={"class":"card-title"})
            priceElem = post.find("div", attrs={"class":"card-price"})
            regionElem = post.find("div", attrs={"class":"card-region-name"})
            title = titleElem.text.replace("\n","").strip()
            price = priceElem.text.replace("\n","").strip()
            region = regionElem.text.replace("\n","").strip()

            print(f"{title}, {price}, {region}")
            f.write(f"{title},{price},{region}\n")

        f.close()

        self.label.setText("당근마켓 크롤링을 완료했습니다")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭")

#모듈을 직접 실행했는지를 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()

