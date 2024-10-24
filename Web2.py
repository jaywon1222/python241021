 
from bs4 import BeautifulSoup
import requests

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






















    #Chap09_당근마켓크롤링하기.py
# import urllib.request
# from bs4 import BeautifulSoup

# url = "https://www.daangn.com/hot_articles"
# page = urllib.request.urlopen(url).read() 

# soup = BeautifulSoup(page, 'html.parser')

# posts = soup.find_all("div", attrs={"class":"card-desc"})
# for post in posts:
#    title = post.find("h2", attrs={"class":"card-title"})
#    price = post.find("div", attrs={"class":"card-price"})
#    addr = post.find("div", attrs={"class":"card-region-name"})
#    print("{0} , {1} , {2}".format(title.text, price.text, addr.text))









 
 
#  <div class="card-desc">
#       <h2 class="card-title">호박 고구마10k</h2>
#       <div class="card-price ">
#         9,000원
#       </div>
#       <div class="card-region-name">
#         서울 중랑구 면목동
#       </div>

