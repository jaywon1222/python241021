#Chap09_Selenium을사용하는경우.py
# pip install clipboard 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

driver = webdriver.Chrome()
#driver.get('https://nid.naver.com/nidlogin.login')
driver.get('https://www.ycs.or.kr/fmcs/133?referer=%2Ffmcs%2F4')

# 로그인 창에 아이디/비밀번호 입력
loginID = "hanul17"
clipboard.copy(loginID)
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH,'//*[@id="user_id"]').send_keys(Keys.CONTROL, 'v')

loginPW = "kimjuwon2@12"
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="user_password"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@class="submit"]').click()

while True:
    pass 