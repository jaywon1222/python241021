#Web1.py 웹크롤링
from bs4 import BeautifulSoup

#웹페이지를 로딩
page = open("Chap09_test.html","rt", encoding="utf-8").read()

soup = BeautifulSoup(page, "html.parser")

# print(soup.prettify())

# print(soup.find("p"))

for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)

print(soup.find_all(id="first"))



